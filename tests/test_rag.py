"""
Unit tests for AgentVerse Grounded Document QA RAG system.
Tests ingestion, retrieval, prompt assembly, citation verification, broken citation detection,
and refusal logic.
"""

import unittest
from pathlib import Path

from ingest import ingest_documents, clean_text, parse_document_into_pages
from app import DocumentQASystem, REFUSAL_MESSAGE
from evaluate import run_grounding_evaluation


class TestDocumentQASystem(unittest.TestCase):
    """Test suite for Grounded Document QA App."""

    @classmethod
    def setUpClass(cls):
        """Ensure sample docs are ingested and index is loaded."""
        cls.chunks = ingest_documents(
            docs_dir="data/sample_docs",
            output_chunks_path="data/chunks.json"
        )
        cls.qa = DocumentQASystem(chunks_path="data/chunks.json")

    def test_document_ingestion_and_metadata(self):
        """Verify ingestion produces chunks with complete metadata."""
        self.assertGreater(len(self.chunks), 0)
        for chunk in self.chunks:
            self.assertIn("chunk_id", chunk)
            self.assertIn("source", chunk)
            self.assertIn("page", chunk)
            self.assertIn("text", chunk)
            self.assertIn("word_count", chunk)
            self.assertIsInstance(chunk["page"], int)
            self.assertGreater(chunk["word_count"], 0)
            self.assertTrue(chunk["source"].endswith(".txt"))

    def test_retrieval_ranking(self):
        """Verify vector retrieval correctly ranks relevant chunks on top."""
        query = "What is the refund window for tuition refund?"
        results = self.qa.retrieve(query, top_k=3)
        self.assertGreater(len(results), 0)
        top_chunk = results[0]
        self.assertEqual(top_chunk["chunk_id"], "refund_policy_p1_c1")
        self.assertGreater(top_chunk["score"], 0.25)

    def test_prompt_construction(self):
        """Verify prompt builder structures evidence clearly and separates question."""
        retrieved = self.qa.retrieve("refund window", top_k=2)
        prompt = self.qa.build_prompt("What is the refund window?", retrieved)
        self.assertIn("You are answering questions using only the evidence below.", prompt)
        self.assertIn(REFUSAL_MESSAGE, prompt)
        self.assertIn("Evidence:", prompt)
        self.assertIn("Question: What is the refund window?", prompt)
        self.assertIn("[1] id:", prompt)

    def test_citation_verification_valid_and_broken(self):
        """Verify citation parser correctly distinguishes valid citations from broken ones."""
        retrieved_ids = ["refund_policy_p1_c1", "college_faq_p2_c1"]

        # Text with valid citation
        answer_valid = "Full refund within 7 days [source: refund_policy_p1_c1, page: 1]."
        valid, broken = self.qa.verify_citations(answer_valid, retrieved_ids)
        self.assertIn("refund_policy_p1_c1", valid)
        self.assertEqual(len(broken), 0)

        # Text with broken / hallucinated citation
        answer_broken = "Curfew is 10 PM [source: hostel_rules_p9_c4, page: 9]."
        valid2, broken2 = self.qa.verify_citations(answer_broken, retrieved_ids)
        self.assertEqual(len(valid2), 0)
        self.assertIn("hostel_rules_p9_c4", broken2)

    def test_refusal_on_unanswerable_query(self):
        """Verify system refuses to guess when evidence is absent."""
        query = "Are students permitted to park personal electric scooters inside hostel bedrooms?"
        res = self.qa.answer_query(query)
        self.assertTrue(res["is_refusal"])
        self.assertEqual(res["answer"], REFUSAL_MESSAGE)
        self.assertEqual(len(res["citations"]), 0)
        self.assertEqual(len(res["broken_citations"]), 0)

    def test_answer_generation_grounded(self):
        """Verify answerable question yields grounded answer with valid citation."""
        query = "Who can apply for the hostel Wi-Fi pass and how many devices are allowed?"
        res = self.qa.answer_query(query)
        self.assertFalse(res["is_refusal"])
        self.assertTrue(res["is_grounded"])
        self.assertGreater(len(res["citations"]), 0)
        self.assertIn("college_faq_p2_c1", res["citations"])
        self.assertEqual(len(res["broken_citations"]), 0)

    def test_full_grounding_eval_runner(self):
        """Verify automated evaluation runner achieves 100% pass rate."""
        eval_res = run_grounding_evaluation(
            questions_path="examples/questions.json",
            eval_md_path="eval/grounding_eval.md",
            chunks_path="data/chunks.json"
        )
        self.assertEqual(eval_res["passed"], eval_res["total"])
        self.assertEqual(eval_res["accuracy"], 100.0)
        self.assertEqual(eval_res["broken_citations"], 0)


if __name__ == "__main__":
    unittest.main()
