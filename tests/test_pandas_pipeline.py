"""
Unit tests for HackIndia Pandas Data Cleaning Pipeline
"""
import unittest
import os
import subprocess
import sys
import pandas as pd

class TestPandasPipeline(unittest.TestCase):
    def test_pipeline_execution(self):
        result = subprocess.run([sys.executable, "clean_data.py"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, f"clean_data.py failed:\n{result.stdout}\n{result.stderr}")

        # Check outputs
        cleaned_path = os.path.join("output", "cleaned_tasks.csv")
        self.assertTrue(os.path.exists(cleaned_path))
        df = pd.read_csv(cleaned_path)
        self.assertGreater(len(df), 0)
        self.assertIn("category_name", df.columns)
        self.assertIn("duration_minutes", df.columns)

    def test_verify_pandas_pipeline_script(self):
        result = subprocess.run([sys.executable, "verify_pandas_pipeline.py"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, f"verify_pandas_pipeline.py failed:\n{result.stdout}\n{result.stderr}")

if __name__ == "__main__":
    unittest.main()
