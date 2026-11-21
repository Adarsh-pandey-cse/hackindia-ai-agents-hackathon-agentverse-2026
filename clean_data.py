#!/usr/bin/env python3
"""
clean_data.py
Data Cleaning & Aggregation Pipeline using pandas and NumPy.
Built for HackIndia "Clean Data With Pandas" Skill.

Features:
- Ingestion of multi-format raw datasets (CSV and JSON)
- Handling of null values, string trimming, and datetime parsing
- Record deduplication and data type conversions
- Relational join across entities (pd.merge)
- Aggregation & grouped metric calculations (groupby + agg)
- Automated chart generation (matplotlib / pandas plot)
- Clean tabular export (CSV and JSON)
"""
import os
import json
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Headless backend for automation
import matplotlib.pyplot as plt

def run_pipeline():
    print("======================================================================")
    print(" AgentVerse Data Cleaning Pipeline (pandas & NumPy)")
    print(" Target: https://hackindia.org/skills/clean-data-with-pandas")
    print("======================================================================\n")

    # 1. Load Raw Datasets
    raw_tasks_path = os.path.join("data", "raw_tasks.csv")
    raw_categories_path = os.path.join("data", "raw_categories.json")

    print(f"[*] Ingesting raw tasks: {raw_tasks_path}")
    tasks_df = pd.read_csv(raw_tasks_path)
    print(f"[*] Ingesting raw categories: {raw_categories_path}")
    categories_df = pd.read_json(raw_categories_path)

    print(f"    - Initial tasks shape: {tasks_df.shape}")
    print(f"    - Initial categories shape: {categories_df.shape}")

    # 2. Deduplication
    initial_count = len(tasks_df)
    tasks_df = tasks_df.drop_duplicates(subset=["task_id", "topic"])
    dedup_removed = initial_count - len(tasks_df)
    print(f"[+] Deduplication complete: removed {dedup_removed} duplicate rows.")

    # 3. String Cleaning & Trimming
    print("[*] Cleaning text attributes (whitespace trimming & title casing)...")
    tasks_df["topic"] = tasks_df["topic"].astype(str).str.strip()
    tasks_df["category_id"] = tasks_df["category_id"].astype(str).str.strip()
    tasks_df["status"] = tasks_df["status"].astype(str).str.strip()

    # 4. Impute Missing Values using Pandas & NumPy
    print("[*] Handling null values...")
    # Fill missing priority with 'MEDIUM'
    tasks_df["priority"] = tasks_df["priority"].fillna("MEDIUM")
    tasks_df["priority"] = tasks_df["priority"].replace("", "MEDIUM")

    # Impute missing duration_seconds using median
    median_duration = tasks_df["duration_seconds"].median()
    tasks_df["duration_seconds"] = tasks_df["duration_seconds"].fillna(median_duration)

    # 5. Standardize Datetime Format
    print("[*] Parsing and standardizing datetimes to ISO-8601...")
    tasks_df["created_date"] = pd.to_datetime(tasks_df["created_date"], errors="coerce")
    tasks_df["created_date"] = tasks_df["created_date"].dt.strftime("%Y-%m-%d")

    # 6. Relational Merge (JOIN)
    print("[*] Joining tasks with category metadata (pd.merge)...")
    cleaned_df = pd.merge(tasks_df, categories_df, on="category_id", how="left")
    print(f"    - Merged dataset shape: {cleaned_df.shape}")

    # 7. Add Calculated / Feature Engineering Columns with NumPy
    cleaned_df["duration_minutes"] = np.round(cleaned_df["duration_seconds"] / 60.0, 2)
    cleaned_df["is_high_priority"] = np.where(cleaned_df["priority"] == "HIGH", True, False)

    # 8. Grouped Summary Aggregations
    print("[*] Computing grouped metric aggregations (groupby + agg)...")
    summary_df = cleaned_df.groupby("category_name").agg(
        total_tasks=("task_id", "count"),
        completed_tasks=("status", lambda s: (s == "COMPLETED").sum()),
        avg_duration_sec=("duration_seconds", "mean"),
        max_sla_hours=("sla_hours", "first"),
        complexity_weight=("complexity_weight", "first")
    ).reset_index()

    summary_df["avg_duration_sec"] = np.round(summary_df["avg_duration_sec"], 2)

    # 9. Ensure Output Directories Exist
    output_dir = "output"
    charts_dir = os.path.join(output_dir, "charts")
    os.makedirs(charts_dir, exist_ok=True)

    # 10. Generate Data Visualizations
    chart_path = os.path.join(charts_dir, "tasks_by_category.png")
    print(f"[*] Generating visualization: {chart_path}...")
    fig, ax1 = plt.subplots(figsize=(8, 4.5))

    categories = summary_df["category_name"]
    x = np.arange(len(categories))
    width = 0.35

    bars1 = ax1.bar(x - width/2, summary_df["total_tasks"], width, label="Total Tasks", color="#1e40af")
    bars2 = ax1.bar(x + width/2, summary_df["completed_tasks"], width, label="Completed", color="#16a34a")

    ax1.set_ylabel("Number of Tasks", fontweight="bold")
    ax1.set_title("AgentVerse Task Execution by Category (Cleaned Data)", fontweight="bold")
    ax1.set_xticks(x)
    ax1.set_xticklabels(categories, rotation=15, ha="right", fontsize=9)
    ax1.legend()
    ax1.grid(axis="y", linestyle="--", alpha=0.7)

    plt.tight_layout()
    plt.savefig(chart_path, dpi=200)
    plt.close()
    print(f"[+] Visualization exported successfully: {chart_path}")

    # 11. Export Cleaned Datasets
    cleaned_csv_path = os.path.join(output_dir, "cleaned_tasks.csv")
    cleaned_df.to_csv(cleaned_csv_path, index=False)
    print(f"[+] Cleaned tasks exported to: {cleaned_csv_path}")

    summary_json_path = os.path.join(output_dir, "category_summary.json")
    summary_dict = summary_df.to_dict(orient="records")
    with open(summary_json_path, "w", encoding="utf-8") as f:
        json.dump(summary_dict, f, indent=2)
    print(f"[+] Grouped summary exported to: {summary_json_path}")

    print("\n----------------------------------------------------------------------")
    print(f" Pipeline Success! {len(cleaned_df)} clean tasks processed across {len(summary_df)} categories.")
    print("----------------------------------------------------------------------")
    return cleaned_df, summary_df

if __name__ == "__main__":
    run_pipeline()
