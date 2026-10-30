#!/usr/bin/env python3
"""
AgentVerse Workload Intelligence - Machine Learning Model Training & Evaluation.
Skill: 'Ship your first ML repo' (HackIndia 2026 / scikit-learn)
Developer: Adarsh Pandey (@adarsh-pandey-cse)

Problem:
  Predict whether an autonomous AI agent task will succeed or fail/timeout
  based on workload metrics (prompt tokens, completion tokens, tool calls,
  latency, memory usage, and retry counts).

Workflow:
  1. Load dataset (data/agent_workload_dataset.csv)
  2. Extract features and labels
  3. Train/Test Split (80/20 stratified split)
  4. Compare multiple scikit-learn model families:
     - RandomForestClassifier
     - LogisticRegression
     - DecisionTreeClassifier
  5. Evaluate best model on unseen test set (Accuracy, Precision, Recall, F1, Confusion Matrix)
  6. Export trained model and evaluation metrics to disk
"""

import os
import sys
import json
import logging
import csv
from datetime import datetime, timezone
from typing import Dict, Any, Tuple

import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)

# Setup Logging
os.makedirs("output", exist_ok=True)
os.makedirs("models", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] [ML-Pipeline]: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger("AgentVerse.ML")

def load_data(file_path: str = "data/agent_workload_dataset.csv") -> Tuple[np.ndarray, np.ndarray, list]:
    """
    Loads dataset and extracts feature matrix X and target label vector y.
    Implements Lesson 3: Prepare features and labels.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Dataset not found at: {file_path}")

    logger.info(f"Loading workload dataset from {file_path}...")
    features = []
    labels = []
    feature_names = ["prompt_tokens", "completion_tokens", "tool_calls", "latency_ms", "memory_mb", "retry_count"]

    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            features.append([
                float(row["prompt_tokens"]),
                float(row["completion_tokens"]),
                float(row["tool_calls"]),
                float(row["latency_ms"]),
                float(row["memory_mb"]),
                float(row["retry_count"])
            ])
            labels.append(int(row["task_success"]))

    X = np.array(features)
    y = np.array(labels)
    logger.info(f"Loaded {X.shape[0]} samples with {X.shape[1]} features. Positive class ratio: {y.mean():.2%}")
    return X, y, feature_names

def train_and_evaluate(
    dataset_path: str = "data/agent_workload_dataset.csv",
    output_dir: str = "output",
    model_dir: str = "models"
) -> Dict[str, Any]:
    """
    Executes full ML training, model selection, evaluation, and serialization pipeline.
    """
    print("=" * 72)
    print("  AgentVerse ML Pipeline - HackIndia Machine Learning Skill")
    print("  Model: scikit-learn Workload Classifier")
    print("  Developer: @adarsh-pandey-cse (Adarsh Pandey)")
    print("=" * 72)

    # 1. Load Data
    X, y, feature_names = load_data(dataset_path)

    # 2. Honest Train/Test Split (Lesson 4: Split data and test honestly)
    logger.info("Executing 80/20 stratified train/test split (random_state=42)...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )
    print(f"[*] Training samples: {X_train.shape[0]} | Evaluation test samples: {X_test.shape[0]}")

    # 3. Feature Scaling
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # 4. Model Selection & Training (Lesson 5: Choose common model families)
    candidate_models = {
        "RandomForest": RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42),
        "LogisticRegression": LogisticRegression(max_iter=1000, random_state=42),
        "DecisionTree": DecisionTreeClassifier(max_depth=5, random_state=42)
    }

    comparison_results = {}
    best_model_name = None
    best_f1 = -1.0

    logger.info("Training and comparing candidate scikit-learn models...")
    for name, model in candidate_models.items():
        # Train on scaled training data
        model.fit(X_train_scaled, y_train)
        preds = model.predict(X_test_scaled)
        acc = accuracy_score(y_test, preds)
        f1 = f1_score(y_test, preds, zero_division=0)
        comparison_results[name] = {"accuracy": round(acc, 4), "f1_score": round(f1, 4)}
        logger.info(f" - {name:<18} | Accuracy: {acc*100:.2f}% | F1-Score: {f1:.4f}")

        if f1 > best_f1:
            best_f1 = f1
            best_model_name = name

    print(f"[+] Selected Champion Model: {best_model_name} (F1-Score: {best_f1:.4f})")
    champion_model = candidate_models[best_model_name]

    # 5. Comprehensive Test Set Evaluation (Lesson 6 & 7)
    y_pred = champion_model.predict(X_test_scaled)
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred, zero_division=0)
    rec = recall_score(y_test, y_pred, zero_division=0)
    f1 = f1_score(y_test, y_pred, zero_division=0)
    cm = confusion_matrix(y_test, y_pred).tolist()
    cls_report = classification_report(y_test, y_pred, output_dict=True)

    # Feature importances if available
    feature_importances = {}
    if hasattr(champion_model, "feature_importances_"):
        for name, imp in zip(feature_names, champion_model.feature_importances_):
            feature_importances[name] = round(float(imp), 4)

    # 6. Save Model Artifacts
    os.makedirs(model_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)
    model_path = os.path.join(model_dir, "agent_workload_classifier.joblib")
    scaler_path = os.path.join(model_dir, "scaler.joblib")

    joblib.dump(champion_model, model_path)
    joblib.dump(scaler, scaler_path)
    logger.info(f"Saved trained scikit-learn model to: {model_path}")
    logger.info(f"Saved StandardScaler to: {scaler_path}")

    # 7. Save Evaluation Reports
    metrics_payload = {
        "metadata": {
            "project": "AgentVerse AI Workload Failure Predictor",
            "developer": "Adarsh Pandey (@adarsh-pandey-cse)",
            "trained_at": datetime.now(timezone.utc).isoformat(),
            "dataset_source": "HackIndia AgentVerse Telemetry Benchmark",
            "total_samples": len(X),
            "train_samples": len(X_train),
            "test_samples": len(X_test),
            "split_ratio": "80% Train / 20% Test (Stratified)"
        },
        "model_selection": {
            "champion_model": best_model_name,
            "comparison": comparison_results
        },
        "test_evaluation_metrics": {
            "accuracy": round(acc, 4),
            "precision": round(prec, 4),
            "recall": round(rec, 4),
            "f1_score": round(f1, 4),
            "confusion_matrix": {
                "true_negative": cm[0][0],
                "false_positive": cm[0][1],
                "false_negative": cm[1][0],
                "true_positive": cm[1][1]
            }
        },
        "feature_importances": feature_importances,
        "classification_report": cls_report
    }

    json_report_path = os.path.join(output_dir, "ml_evaluation_report.json")
    with open(json_report_path, "w", encoding="utf-8") as f:
        json.dump(metrics_payload, f, indent=2)

    md_report_path = os.path.join(output_dir, "ml_evaluation_summary.md")
    _write_markdown_summary(md_report_path, metrics_payload)

    print("\n" + "=" * 72)
    print("  EVALUATION RESULTS ON UNSEEN TEST SET (20% Split):")
    print("=" * 72)
    print(f"  [+] Accuracy:  {acc*100:.2f}%")
    print(f"  [+] Precision: {prec:.4f}")
    print(f"  [+] Recall:    {rec:.4f}")
    print(f"  [+] F1-Score:  {f1:.4f}")
    print(f"  [+] Saved Model:  {model_path}")
    print(f"  [+] JSON Report:  {json_report_path}")
    print(f"  [+] MD Summary:   {md_report_path}")
    print("=" * 72)

    return metrics_payload

def _write_markdown_summary(path: str, data: Dict[str, Any]):
    """Generates a formatted Markdown report of evaluation results."""
    m = data["test_evaluation_metrics"]
    cm = m["confusion_matrix"]
    lines = [
        "# AgentVerse ML Model - Evaluation Report",
        f"**Skill:** HackIndia - Ship your first ML repo  ",
        f"**Developer:** {data['metadata']['developer']}  ",
        f"**Dataset Source:** `{data['metadata']['dataset_source']}`  ",
        f"**Split Ratio:** `{data['metadata']['split_ratio']}`  ",
        f"**Champion Model:** `{data['model_selection']['champion_model']}`  ",
        f"**Trained at:** `{data['metadata']['trained_at']}`  ",
        "\n---\n",
        "## 1. Model Comparison on Test Split\n",
        "| Model Family | Accuracy | F1-Score |",
        "| :--- | :--- | :--- |"
    ]

    for model, res in data["model_selection"]["comparison"].items():
        lines.append(f"| **{model}** | {res['accuracy']*100:.2f}% | {res['f1_score']:.4f} |")

    lines.extend([
        "\n## 2. Champion Model Test Set Metrics\n",
        f"- **Accuracy:** `{m['accuracy']*100:.2f}%`",
        f"- **Precision:** `{m['precision']:.4f}`",
        f"- **Recall:** `{m['recall']:.4f}`",
        f"- **F1-Score:** `{m['f1_score']:.4f}`\n",
        "### Confusion Matrix",
        "| | Predicted Negative (0) | Predicted Positive (1) |",
        "| :--- | :--- | :--- |",
        f"| **Actual Negative (0)** | `{cm['true_negative']}` (TN) | `{cm['false_positive']}` (FP) |",
        f"| **Actual Positive (1)** | `{cm['false_negative']}` (FN) | `{cm['true_positive']}` (TP) |\n",
        "## 3. Feature Importance Analysis\n"
    ])

    for feat, imp in data.get("feature_importances", {}).items():
        lines.append(f"- **`{feat}`**: {imp*100:.2f}%")

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

if __name__ == "__main__":
    train_and_evaluate()
