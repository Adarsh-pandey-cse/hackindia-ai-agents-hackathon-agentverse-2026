"""
Unit Tests for AgentVerse Autonomous AI Agent.
Validates data ingestion, comprehensions, mock API calls, and report generation.
Run via: python -m unittest discover tests
"""

import os
import shutil
import unittest
from agent import AutonomousAnalysisAgent, TaskItem

class TestAutonomousAgent(unittest.TestCase):
    """Test suite for agent functionality."""

    def setUp(self):
        self.test_output_dir = "tests/test_output"
        os.makedirs(self.test_output_dir, exist_ok=True)
        self.agent = AutonomousAnalysisAgent(config_path="data/sample_input.json", force_mock=True)

    def tearDown(self):
        if os.path.exists(self.test_output_dir):
            shutil.rmtree(self.test_output_dir)

    def test_load_json_data(self):
        """Verify reading and parsing JSON input dataset (Lesson 5)."""
        tasks = self.agent.load_input_data("data/sample_input.json")
        self.assertGreater(len(tasks), 0)
        self.assertIsInstance(tasks[0], TaskItem)
        self.assertEqual(tasks[0].task_id, "TASK-001")

    def test_load_csv_data(self):
        """Verify reading and parsing CSV input dataset (Lesson 5)."""
        tasks = self.agent.load_input_data("data/sample_input.csv")
        self.assertGreater(len(tasks), 0)
        self.assertEqual(tasks[0].task_id, "TASK-004")

    def test_comprehensions(self):
        """Verify list and set comprehensions (Lesson 2)."""
        self.agent.load_input_data("data/sample_input.json")
        categories = self.agent.get_categories()
        self.assertIn("ai_tech_trends", categories)
        self.assertIn("market_indicators", categories)

        high_priority = self.agent.filter_by_priority("HIGH")
        self.assertTrue(all(t.priority == "HIGH" for t in high_priority))

    def test_mock_api_execution(self):
        """Verify API calling with mock fallback (Lesson 6)."""
        self.agent.load_input_data("data/sample_input.json")
        results = self.agent.execute_tasks()
        self.assertEqual(len(results), len(self.agent.tasks))

        status_map = self.agent.get_task_status_map()
        self.assertIn("TASK-001", status_map)
        self.assertEqual(status_map["TASK-001"], "simulated_success")

    def test_save_outputs(self):
        """Verify writing output files to disk (Lesson 5 & 7)."""
        self.agent.load_input_data("data/sample_input.json")
        self.agent.execute_tasks()
        output_paths = self.agent.save_outputs(output_dir=self.test_output_dir)

        self.assertTrue(os.path.exists(output_paths["json"]))
        self.assertTrue(os.path.exists(output_paths["markdown"]))
        self.assertGreater(os.path.getsize(output_paths["json"]), 100)
        self.assertGreater(os.path.getsize(output_paths["markdown"]), 100)

if __name__ == "__main__":
    unittest.main()
