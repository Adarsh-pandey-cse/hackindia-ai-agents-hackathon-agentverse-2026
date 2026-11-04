"""
AgentVerse Grounded Document QA - Document Ingestion Pipeline
Processes documents from data/sample_docs/, breaks them into structured chunks
with rich metadata (source, page, chunk_id), and saves indexed data.
"""

import os
import re
import json
import argparse
from pathlib import Path
from typing import List, Dict, Any

try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    import joblib
    HAS_SKLEARN = True
except ImportError:
    HAS_SKLEARN = False

try:
    import chromadb
    HAS_CHROMADB = True
except ImportError:
    HAS_CHROMADB = False


def clean_text(text: str) -> str:
    """Normalize whitespace and strip unnecessary control characters."""
    return re.sub(r'\s+', ' ', text).strip()


def parse_document_into_pages(filepath: Path) -> List[Dict[str, Any]]:
    """
    Parse a document into page-level segments.
    Detects '--- Page N ---' markers or falls back to synthetic pagination.
    """
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    filename = filepath.name
    page_blocks = []

    # Check for page markers
    page_matches = list(re.finditer(r'---\s*Page\s*(\d+)\s*---', content, re.IGNORECASE))
    if page_matches:
        for i, match in enumerate(page_matches):
            page_num = int(match.group(1))
            start_pos = match.end()
            end_pos = page_matches[i + 1].start() if i + 1 < len(page_matches) else len(content)
            page_text = content[start_pos:end_pos].strip()
            if page_text:
                page_blocks.append({
                    "page": page_num,
                    "text": page_text,
                    "source": filename
                })
    else:
        # Fallback synthetic pagination: roughly 250 words per page
        words = content.split()
        page_size = 250
        page_num = 1
        for i in range(0, len(words), page_size):
            chunk_words = words[i:i + page_size]
            page_blocks.append({
                "page": page_num,
                "text": " ".join(chunk_words),
                "source": filename
            })
            page_num += 1

    return page_blocks


def chunk_page_text(page_data: Dict[str, Any], max_chunk_words: int = 150) -> List[Dict[str, Any]]:
    """
    Split page text into distinct chunks with unique chunk_id metadata.
    Preserves paragraph or rule boundaries where possible.
    """
    source = page_data["source"]
    page_num = page_data["page"]
    raw_text = page_data["text"]

    # Base name for chunk IDs (e.g. college_faq_p1_c1)
    base_id = re.sub(r'[^a-zA-Z0-9]+', '_', Path(source).stem).strip('_')

    # Try splitting by paragraph or numbered items
    paragraphs = [p.strip() for p in re.split(r'\n\s*\n|\n(?=\d+\.\s)', raw_text) if p.strip()]

    chunks = []
    current_chunk = []
    current_count = 0
    chunk_index = 1

    for para in paragraphs:
        para_words = para.split()
        if current_count + len(para_words) > max_chunk_words and current_chunk:
            combined_text = clean_text(" ".join(current_chunk))
            chunk_id = f"{base_id}_p{page_num}_c{chunk_index}"
            chunks.append({
                "chunk_id": chunk_id,
                "source": source,
                "page": page_num,
                "text": combined_text,
                "word_count": len(combined_text.split())
            })
            chunk_index += 1
            current_chunk = [para]
            current_count = len(para_words)
        else:
            current_chunk.append(para)
            current_count += len(para_words)

    if current_chunk:
        combined_text = clean_text(" ".join(current_chunk))
        chunk_id = f"{base_id}_p{page_num}_c{chunk_index}"
        chunks.append({
            "chunk_id": chunk_id,
            "source": source,
            "page": page_num,
            "text": combined_text,
            "word_count": len(combined_text.split())
        })

    return chunks


def ingest_documents(docs_dir: str = "data/sample_docs",
                     output_chunks_path: str = "data/chunks.json",
                     chroma_dir: str = "data/chroma_db") -> List[Dict[str, Any]]:
    """
    Main ingestion function that reads sample docs, produces chunk records,
    builds indices, and writes output files.
    """
    docs_path = Path(docs_dir)
    if not docs_path.exists():
        raise FileNotFoundError(f"Source documents directory not found: {docs_dir}")

    all_chunks: List[Dict[str, Any]] = []
    supported_extensions = {".txt", ".md", ".json"}

    files = sorted([f for f in docs_path.iterdir() if f.is_file() and f.suffix.lower() in supported_extensions])
    if not files:
        raise ValueError(f"No valid text documents found in {docs_dir}")

    print(f"[*] Starting ingestion from {docs_path.resolve()}...")
    print(f"[*] Found {len(files)} document(s): {[f.name for f in files]}")

    for filepath in files:
        pages = parse_document_into_pages(filepath)
        for page_data in pages:
            page_chunks = chunk_page_text(page_data)
            all_chunks.extend(page_chunks)

    # Save chunks to JSON
    out_file = Path(output_chunks_path)
    out_file.parent.mkdir(parents=True, exist_ok=True)
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(all_chunks, f, indent=2, ensure_ascii=False)

    print(f"[+] Successfully extracted {len(all_chunks)} chunks with metadata.")
    print(f"[+] Chunks saved to: {out_file}")

    # Build and cache TF-IDF vector index for instant offline retrieval
    if HAS_SKLEARN and all_chunks:
        corpus = [c["text"] for c in all_chunks]
        vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
        tfidf_matrix = vectorizer.fit_transform(corpus)
        index_data = {
            "vectorizer": vectorizer,
            "matrix": tfidf_matrix,
            "chunk_ids": [c["chunk_id"] for c in all_chunks]
        }
        tfidf_path = out_file.parent / "tfidf_index.joblib"
        joblib.dump(index_data, tfidf_path)
        print(f"[+] TF-IDF index cached at: {tfidf_path}")

    # Optional ChromaDB indexing if installed
    if HAS_CHROMADB and all_chunks:
        try:
            client = chromadb.PersistentClient(path=chroma_dir)
            collection = client.get_or_create_collection(name="documents")
            ids = [c["chunk_id"] for c in all_chunks]
            documents = [c["text"] for c in all_chunks]
            metadatas = [{"source": c["source"], "page": c["page"]} for c in all_chunks]
            collection.upsert(ids=ids, documents=documents, metadatas=metadatas)
            print(f"[+] ChromaDB collection indexed at: {chroma_dir}")
        except Exception as e:
            print(f"[!] Warning: ChromaDB indexing skipped: {e}")

    return all_chunks


def main():
    parser = argparse.ArgumentParser(description="Ingest documents and generate chunk index with metadata.")
    parser.add_argument("--docs-dir", default="data/sample_docs", help="Directory containing source documents")
    parser.add_argument("--output", default="data/chunks.json", help="Destination path for chunks.json")
    args = parser.parse_args()

    ingest_documents(docs_dir=args.docs_dir, output_chunks_path=args.output)


if __name__ == "__main__":
    main()
