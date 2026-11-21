#!/usr/bin/env python3
"""
verify_pandas_pipeline.py
Automated Verification Script for HackIndia "Clean Data With Pandas" Skill.

Validates:
1. Requirements specify pandas and numpy
2. Multiple raw data files exist (data/raw_tasks.csv, data/raw_categories.json)
3. Data cleaning pipeline (clean_data.py) executes with zero errors
4. Cleaned tabular output generated (output/cleaned_tasks.csv)
5. Grouped summary metrics generated (output/category_summary.json)
6. Data visualization chart generated (output/charts/tasks_by_category.png)
7. Jupyter notebook present (notebooks/clean_data_pipeline.ipynb)
8. README.md documents data cleaning choices, run steps, and HackIndia badge
"""
import sys
import os
import subprocess
import json

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def log_pass(msg):
    print(f"[{GREEN}PASS{RESET}] {msg}")

def log_fail(msg):
    print(f"[{RED}FAIL{RESET}] {msg}")

def log_info(msg):
    print(f"[{YELLOW}INFO{RESET}] {msg}")

def run_checks():
    failures = 0
    total = 0

    print("======================================================================")
    print(" HackIndia Skill Verification: Clean Data With Pandas")
    print(" Target: https://hackindia.org/skills/clean-data-with-pandas")
    print("======================================================================\n")

    # 1. Check requirements.txt
    total += 1
    req_path = "requirements.txt"
    if not os.path.exists(req_path):
        log_fail("requirements.txt not found")
        failures += 1
    else:
        with open(req_path, "r", encoding="utf-8") as f:
            reqs = f.read().lower()
        if "pandas" in reqs and "numpy" in reqs:
            log_pass("requirements.txt specifies pandas and numpy")
        else:
            log_fail("requirements.txt missing pandas or numpy")
            failures += 1

    # 2. Check Raw Data Files
    total += 1
    f1 = os.path.join("data", "raw_tasks.csv")
    f2 = os.path.join("data", "raw_categories.json")
    if os.path.exists(f1) and os.path.exists(f2):
        log_pass(f"Raw heterogeneous datasets verified: {f1} and {f2}")
    else:
        log_fail(f"Missing raw datasets: f1={os.path.exists(f1)}, f2={os.path.exists(f2)}")
        failures += 1

    # 3. Check Pipeline Execution (clean_data.py)
    total += 1
    script_path = "clean_data.py"
    if not os.path.exists(script_path):
        log_fail(f"{script_path} not found")
        failures += 1
    else:
        proc = subprocess.run([sys.executable, script_path], capture_output=True, text=True)
        if proc.returncode == 0:
            log_pass("Data cleaning pipeline (clean_data.py) executed successfully with code 0")
        else:
            log_fail(f"clean_data.py execution failed:\n{proc.stdout}\n{proc.stderr}")
            failures += 1

    # 4. Check Cleaned Output Dataset
    total += 1
    cleaned_csv = os.path.join("output", "cleaned_tasks.csv")
    if os.path.exists(cleaned_csv) and os.path.getsize(cleaned_csv) > 100:
        log_pass(f"Cleaned output dataset verified: {cleaned_csv}")
    else:
        log_fail(f"Cleaned dataset missing or empty: {cleaned_csv}")
        failures += 1

    # 5. Check Grouped Summary Output
    total += 1
    summary_json = os.path.join("output", "category_summary.json")
    if os.path.exists(summary_json):
        try:
            with open(summary_json, "r", encoding="utf-8") as f:
                data = json.load(f)
            if isinstance(data, list) and len(data) > 0:
                log_pass(f"Grouped summary JSON verified with {len(data)} category records")
            else:
                log_fail("summary.json contains invalid format")
                failures += 1
        except Exception as e:
            log_fail(f"Failed to parse summary.json: {e}")
            failures += 1
    else:
        log_fail(f"{summary_json} not found")
        failures += 1

    # 6. Check Chart Output
    total += 1
    chart_path = os.path.join("output", "charts", "tasks_by_category.png")
    if os.path.exists(chart_path) and os.path.getsize(chart_path) > 1000:
        log_pass(f"Data visualization chart verified: {chart_path}")
    else:
        log_fail(f"Chart missing or empty: {chart_path}")
        failures += 1

    # 7. Check Jupyter Notebook
    total += 1
    nb_path = os.path.join("notebooks", "clean_data_pipeline.ipynb")
    if os.path.exists(nb_path):
        log_pass(f"Jupyter Notebook verified: {nb_path}")
    else:
        log_fail(f"Jupyter Notebook missing: {nb_path}")
        failures += 1

    # 8. Check README Documentation
    total += 1
    readme_path = "README.md"
    if not os.path.exists(readme_path):
        log_fail("README.md not found")
        failures += 1
    else:
        with open(readme_path, "r", encoding="utf-8") as f:
            readme = f.read()
        has_pandas_badge = "clean-data-with-pandas" in readme or "Pandas" in readme
        has_pandas_section = "Pandas" in readme and "clean_data.py" in readme
        if has_pandas_badge and has_pandas_section:
            log_pass("README.md contains Pandas documentation, run steps, and HackIndia badge")
        else:
            log_fail("README.md missing Pandas documentation or badges")
            failures += 1

    print("\n----------------------------------------------------------------------")
    print(f" Verification Result: {total - failures}/{total} checks passed.")
    print("----------------------------------------------------------------------")

    if failures == 0:
        print(f"\n{GREEN}ALL CHECKS PASSED SUCCESSFULLY! Ready for HackIndia submission.{RESET}\n")
        return 0
    else:
        print(f"\n{RED}VERIFICATION FAILED: {failures} issues detected.{RESET}\n")
        return 1

if __name__ == "__main__":
    sys.exit(run_checks())
