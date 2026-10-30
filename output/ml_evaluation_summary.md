# AgentVerse ML Model - Evaluation Report
**Skill:** HackIndia - Ship your first ML repo  
**Developer:** Adarsh Pandey (@adarsh-pandey-cse)  
**Dataset Source:** `HackIndia AgentVerse Telemetry Benchmark`  
**Split Ratio:** `80% Train / 20% Test (Stratified)`  
**Champion Model:** `LogisticRegression`  
**Trained at:** `2026-10-30T07:51:23.672958+00:00`  

---

## 1. Model Comparison on Test Split

| Model Family | Accuracy | F1-Score |
| :--- | :--- | :--- |
| **RandomForest** | 94.58% | 0.9666 |
| **LogisticRegression** | 96.25% | 0.9771 |
| **DecisionTree** | 94.58% | 0.9666 |

## 2. Champion Model Test Set Metrics

- **Accuracy:** `96.25%`
- **Precision:** `0.9697`
- **Recall:** `0.9846`
- **F1-Score:** `0.9771`

### Confusion Matrix
| | Predicted Negative (0) | Predicted Positive (1) |
| :--- | :--- | :--- |
| **Actual Negative (0)** | `39` (TN) | `6` (FP) |
| **Actual Positive (1)** | `3` (FN) | `192` (TP) |

## 3. Feature Importance Analysis
