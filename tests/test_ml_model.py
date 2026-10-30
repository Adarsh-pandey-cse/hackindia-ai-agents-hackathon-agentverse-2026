"""
Unit Tests for Machine Learning Pipeline.
Validates dataset loading, train/test splitting, scikit-learn model fitting, and metrics.
Skill: 'Ship your first ML repo' (HackIndia 2026)
Run via: python -m unittest discover tests
"""

import os
import unittest
import numpy as np
import joblib
from train_ml_model import load_data, train_and_evaluate

class TestMachineLearningPipeline(unittest.TestCase):
    """Test suite for scikit-learn ML pipeline."""

    def test_dataset_loading(self):
        """Verify dataset ingestion and feature matrix shape."""
        X, y, feature_names = load_data("data/agent_workload_dataset.csv")
        self.assertEqual(X.shape[0], 1200)
        self.assertEqual(X.shape[1], 6)
        self.assertEqual(len(y), 1200)
        self.assertEqual(len(feature_names), 6)

    def test_model_training_and_serialization(self):
        """Verify model training, test split, and saved joblib artifacts."""
        metrics = train_and_evaluate(
            dataset_path="data/agent_workload_dataset.csv",
            output_dir="output",
            model_dir="models"
        )

        self.assertIn("accuracy", metrics["test_evaluation_metrics"])
        self.assertGreater(metrics["test_evaluation_metrics"]["accuracy"], 0.85)
        self.assertGreater(metrics["test_evaluation_metrics"]["f1_score"], 0.85)

        # Verify saved model can be loaded and predict
        model_path = "models/agent_workload_classifier.joblib"
        scaler_path = "models/scaler.joblib"
        self.assertTrue(os.path.exists(model_path))
        self.assertTrue(os.path.exists(scaler_path))

        model = joblib.load(model_path)
        scaler = joblib.load(scaler_path)

        dummy_sample = np.array([[1500.0, 450.0, 3.0, 420.0, 64.0, 0.0]])
        scaled_sample = scaler.transform(dummy_sample)
        pred = model.predict(scaled_sample)
        self.assertIn(pred[0], [0, 1])

if __name__ == "__main__":
    unittest.main()
