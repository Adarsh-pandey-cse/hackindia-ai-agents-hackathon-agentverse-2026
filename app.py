"""
AgentVerse Grounded Document QA App (app.py)
Answers user queries grounded strictly in retrieved document evidence,
attaches verifiable source citations, flags broken citations, and refuses
to hallucinate on missing information.
"""

import os
import re
import json
import argparse
from pathlib import Path
from typing import List, Dict, Any, Tuple, Optional

try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    import joblib
    HAS_SKLEARN = True
except ImportError:
    HAS_SKLEARN = False

# Strict refusal sentence as required by HackIndia benchmark
REFUSAL_MESSAGE = "I could not find this in the provided documents."
CITATION_REGEX = re.compile(r'\[source:\s*([a-zA-Z0-9_\-\.]+)(?:,\s*page:?\s*(\d+))?\]', re.IGNORECASE)


class DocumentQASystem:
    """
    Production Grounded RAG QA Engine with verifiable citations
    and anti-hallucination guardrails.
    """

    def __init__(self,
                 chunks_path: str = "data/chunks.json",
                 similarity_threshold: float = 0.22):
        self.chunks_path = Path(chunks_path)
        self.similarity_threshold = similarity_threshold
        self.chunks: List[Dict[str, Any]] = []
        self.vectorizer: Optional[Any] = None
        self.tfidf_matrix: Optional[Any] = None
        self.chunk_ids: List[str] = []
        self.load_index()

    def load_index(self) -> None:
        """Load chunk metadata and retrieval vector index."""
        if not self.chunks_path.exists():
            # Trigger ingestion if not already executed
            from ingest import ingest_documents
            ingest_documents(output_chunks_path=str(self.chunks_path))

        with open(self.chunks_path, "r", encoding="utf-8") as f:
            self.chunks = json.load(f)

        self.chunk_ids = [c["chunk_id"] for c in self.chunks]

        # Load cached TF-IDF index or build in-memory
        tfidf_path = self.chunks_path.parent / "tfidf_index.joblib"
        if HAS_SKLEARN and tfidf_path.exists():
            data = joblib.load(tfidf_path)
            self.vectorizer = data["vectorizer"]
            self.tfidf_matrix = data["matrix"]
        elif HAS_SKLEARN and self.chunks:
            corpus = [c["text"] for c in self.chunks]
            self.vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
            self.tfidf_matrix = self.vectorizer.fit_transform(corpus)

    def retrieve(self, query: str, top_k: int = 3) -> List[Dict[str, Any]]:
        """
        Retrieve top-k relevant chunks for a given query with similarity scores.
        """
        if not self.chunks:
            return []

        # Vector retrieval via TF-IDF cosine similarity
        if HAS_SKLEARN and self.vectorizer is not None and self.tfidf_matrix is not None:
            query_vec = self.vectorizer.transform([query])
            scores = cosine_similarity(query_vec, self.tfidf_matrix).flatten()
            ranked_indices = scores.argsort()[::-1][:top_k]

            results = []
            for idx in ranked_indices:
                score = float(scores[idx])
                chunk = dict(self.chunks[idx])
                chunk["score"] = score
                results.append(chunk)
            return results

        # Fallback lexical token overlap scoring
        query_words = set(re.findall(r'\w+', query.lower()))
        scored = []
        for c in self.chunks:
            chunk_words = set(re.findall(r'\w+', c["text"].lower()))
            overlap = len(query_words & chunk_words)
            score = overlap / max(1, len(query_words))
            c_copy = dict(c)
            c_copy["score"] = score
            scored.append(c_copy)
        scored.sort(key=lambda x: x["score"], reverse=True)
        return scored[:top_k]

    def build_prompt(self, question: str, retrieved_chunks: List[Dict[str, Any]]) -> str:
        """
        Build a grounded prompt separating labeled evidence from the question.
        Instructs the model to refuse to guess if evidence is missing and mandates citations.
        """
        evidence_blocks = []
        for i, chunk in enumerate(retrieved_chunks, start=1):
            block = (
                f"[{i}] id: {chunk['chunk_id']}, source: {chunk['source']}, page: {chunk['page']}\n"
                f"Text: {chunk['text']}"
            )
            evidence_blocks.append(block)

        evidence_text = "\n\n".join(evidence_blocks) if evidence_blocks else "No evidence retrieved."

        prompt = (
            "You are answering questions using only the evidence below.\n"
            f"If the evidence does not contain the answer, say: {REFUSAL_MESSAGE}\n"
            "For every factual claim, add a citation in this format: [source: <chunk_id>, page: <page>].\n\n"
            "Evidence:\n"
            f"{evidence_text}\n\n"
            f"Question: {question}\n"
            "Answer:"
        )
        return prompt

    def verify_citations(self, answer: str, retrieved_chunk_ids: List[str]) -> Tuple[List[str], List[str]]:
        """
        Extract citations and verify each against retrieved chunk IDs.
        Returns (valid_citations, broken_citations).
        """
        matches = CITATION_REGEX.findall(answer)
        valid = []
        broken = []
        for match in matches:
            cited_id = match[0]
            if cited_id in retrieved_chunk_ids:
                valid.append(cited_id)
            else:
                broken.append(cited_id)
        return valid, broken

    def synthesize_answer(self, question: str, retrieved_chunks: List[Dict[str, Any]]) -> str:
        """
        Generate grounded answer strictly backed by retrieved evidence.
        Applies factual sentence extraction or LLM API if configured.
        """
        if not retrieved_chunks:
            return REFUSAL_MESSAGE

        top_chunk = retrieved_chunks[0]
        top_score = top_chunk.get("score", 0.0)

        # Refusal check: query has insufficient relevance to retrieved evidence
        if top_score < self.similarity_threshold:
            return REFUSAL_MESSAGE

        # Optional live LLM API call if OPENAI_API_KEY or GEMINI_API_KEY is present
        api_key = os.getenv("OPENAI_API_KEY") or os.getenv("GEMINI_API_KEY")
        if api_key and api_key != "your_openai_api_key_here":
            try:
                import requests
                # Attempt OpenAI-compatible endpoint if OPENAI_API_KEY set
                if os.getenv("OPENAI_API_KEY"):
                    resp = requests.post(
                        "https://api.openai.com/v1/chat/completions",
                        headers={"Authorization": f"Bearer {api_key}"},
                        json={
                            "model": "gpt-4o-mini",
                            "messages": [
                                {"role": "system", "content": "You are a factual grounded QA assistant. Answer ONLY from evidence. Use exact citations [source: chunk_id, page: page]."},
                                {"role": "user", "content": self.build_prompt(question, retrieved_chunks)}
                            ],
                            "temperature": 0.0
                        },
                        timeout=10
                    )
                    if resp.status_code == 200:
                        return resp.json()["choices"][0]["message"]["content"].strip()
            except Exception:
                pass  # Fall back gracefully to deterministic factual extractor

        # Deterministic Grounded Factual Extraction Engine
        # Find the most relevant sentence from top retrieved chunks
        sentences = []
        for chunk in retrieved_chunks:
            chunk_sentences = re.split(r'(?<=[.!?])\s+', chunk["text"])
            for s in chunk_sentences:
                clean_s = s.strip()
                if len(clean_s) > 15:
                    sentences.append((clean_s, chunk))

        q_lower = question.lower()
        q_tokens = set(re.findall(r'\b[a-z0-9]{3,}\b', q_lower)) - {"what", "when", "where", "which", "who", "whom", "this", "that", "does", "have", "from", "with"}

        # Score sentences against question tokens
        best_sentences = []
        for s_text, chunk in sentences:
            s_tokens = set(re.findall(r'\b[a-z0-9]{3,}\b', s_text.lower()))
            overlap = len(q_tokens & s_tokens)
            if overlap > 0:
                best_sentences.append((overlap, s_text, chunk))

        if not best_sentences:
            return REFUSAL_MESSAGE

        # Sort by relevance overlap
        best_sentences.sort(key=lambda x: x[0], reverse=True)
        top_sent = best_sentences[0]
        overlap_score, sent_text, chunk = top_sent

        # If keyword overlap is too low to answer specific question, refuse
        if overlap_score < 2 and top_score < 0.2:
            return REFUSAL_MESSAGE

        # Construct grounded answer with citation
        chunk_id = chunk["chunk_id"]
        page = chunk["page"]
        
        # Check if multiple high-relevance sentences from the same or different chunks should be joined
        chosen_texts = [sent_text]
        used_chunks = [chunk]
        covered_tokens = set(re.findall(r'\b[a-z0-9]{3,}\b', sent_text.lower()))
        remaining_q_tokens = q_tokens - covered_tokens

        for next_overlap, next_sent, next_chunk in best_sentences[1:]:
            next_tokens = set(re.findall(r'\b[a-z0-9]{3,}\b', next_sent.lower()))
            complementary_overlap = len(remaining_q_tokens & next_tokens)
            if (complementary_overlap > 0 or next_overlap >= overlap_score - 1) and next_sent not in chosen_texts:
                chosen_texts.append(next_sent)
                used_chunks.append(next_chunk)
                remaining_q_tokens -= next_tokens
                if len(chosen_texts) >= 3:
                    break

        answer_parts = []
        for text, ch in zip(chosen_texts, used_chunks):
            # Clean section prefixes like [Section: ...] or numbers
            clean_ans = re.sub(r'^\[Section:[^\]]+\]\s*', '', text)
            clean_ans = re.sub(r'^\d+\.\s*', '', clean_ans).strip()
            if not clean_ans.endswith('.'):
                clean_ans += '.'
            answer_parts.append(f"{clean_ans} [source: {ch['chunk_id']}, page: {ch['page']}]")

        return " ".join(answer_parts)

    def answer_query(self, question: str, top_k: int = 3) -> Dict[str, Any]:
        """
        Execute full QA pipeline: retrieve chunks, build prompt, synthesize answer,
        and verify citation grounding.
        """
        retrieved_chunks = self.retrieve(question, top_k=top_k)
        retrieved_ids = [c["chunk_id"] for c in retrieved_chunks]
        prompt = self.build_prompt(question, retrieved_chunks)
        answer = self.synthesize_answer(question, retrieved_chunks)

        valid_citations, broken_citations = self.verify_citations(answer, retrieved_ids)

        is_refusal = (REFUSAL_MESSAGE in answer)
        is_grounded = bool(valid_citations and not broken_citations) if not is_refusal else True

        return {
            "query": question,
            "answer": answer,
            "retrieved_chunks": retrieved_chunks,
            "retrieved_ids": retrieved_ids,
            "prompt": prompt,
            "citations": valid_citations,
            "broken_citations": broken_citations,
            "is_refusal": is_refusal,
            "is_grounded": is_grounded
        }


def main():
    parser = argparse.ArgumentParser(description="AgentVerse Grounded Document QA App")
    parser.add_argument("--query", "-q", type=str, help="Question to ask the documents")
    parser.add_argument("--k", type=int, default=3, help="Number of chunks to retrieve (default: 3)")
    parser.add_argument("--chunks", default="data/chunks.json", help="Path to chunks.json")
    parser.add_argument("--verbose", "-v", action="store_true", help="Print retrieved chunks and prompt")
    args = parser.parse_args()

    qa = DocumentQASystem(chunks_path=args.chunks)

    if args.query:
        result = qa.answer_query(args.query, top_k=args.k)
        print("\n========================================================")
        print(f"QUESTION: {result['query']}")
        print("========================================================")
        if args.verbose:
            print("\n--- RETRIEVED CHUNKS ---")
            for i, c in enumerate(result["retrieved_chunks"], 1):
                print(f"[{i}] {c['chunk_id']} (score: {c.get('score', 0):.4f}) -> {c['text'][:120]}...")
            print("\n--- GENERATED PROMPT ---")
            print(result["prompt"])
            print("--------------------------------------------------------")
        print("\nANSWER:")
        print(result["answer"])
        print("\nCITATIONS:")
        print(f"Valid: {result['citations']} | Broken: {result['broken_citations']}")
        print(f"Grounded: {result['is_grounded']} | Refusal: {result['is_refusal']}")
        print("========================================================\n")
    else:
        # Interactive Mode
        print("========================================================")
        print(" AgentVerse Grounded Document QA App (Interactive Mode)")
        print(" Type a question, or 'exit' / 'quit' to end.")
        print(" Sample questions:")
        print("  - What is the refund window?")
        print("  - Who can apply for the hostel Wi-Fi pass?")
        print("  - Can I pay semester fees using UPI?")
        print("========================================================\n")

        while True:
            try:
                user_input = input("Question: ").strip()
                if not user_input or user_input.lower() in ("exit", "quit", "q"):
                    print("Exiting. Goodbye!")
                    break

                res = qa.answer_query(user_input, top_k=args.k)
                print("\nAnswer:")
                print(res["answer"])
                print(f"[Citations: {res['citations']} | Grounded: {res['is_grounded']}]\n")
            except (KeyboardInterrupt, EOFError):
                print("\nSession ended.")
                break


if __name__ == "__main__":
    main()
