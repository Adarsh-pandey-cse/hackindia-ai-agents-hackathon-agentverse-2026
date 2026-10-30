# AGENTS.md - Agent Operations & Operating Guide

## Project Overview
**AgentVerse Autonomous AI Agent & ML Pipeline**  
HackIndia AI Agents Hackathon - AgentVerse 2026  
Developer: Adarsh Pandey ([@adarsh-pandey-cse](https://github.com/adarsh-pandey-cse))

This repository contains two production components:
1. **Autonomous Intelligence CLI Tool (`main.py`):** Ingests structured task data (`.json` or `.csv`), executes external REST queries (with automatic mock fallbacks), applies data shaping, and generates structured JSON and Markdown summary reports.
2. **Machine Learning Pipeline (`train_ml_model.py`):** Trains and evaluates a scikit-learn classifier to predict agent workload execution success on unseen test data.

---

## Architecture & Code Map
- `main.py`: Entry point for CLI tool. Uses `argparse` with flags `--input`, `--output-dir`, `--priority`, `--mock`, `--verbose`.
- `agent.py`: Core agent logic (`AgentVerseAgent`). Uses `@dataclass` (`TaskItem`, `AnalysisRecord`) and list comprehensions.
- `api_client.py`: External REST client (`ExternalAPIClient`) with live endpoints and instant offline fallback mocks.
- `train_ml_model.py`: Scikit-learn training and evaluation pipeline. Stratified 80/20 train/test split, StandardScaler, model comparison, joblib serialization, JSON/MD metric reports.
- `tests/`: Automated unit tests (`test_agent.py`, `test_ml_model.py`). Run with `python -m unittest discover tests`.
- `data/`: Dataset storage (`sample_input.json`, `sample_input.csv`, `agent_workload_dataset.csv`).
- `output/`: Directory where runtime and evaluation artifacts are written.
- `models/`: Saved model binaries (`agent_workload_classifier.joblib`, `scaler.joblib`).

---

## Operating Rules for Autonomous Agents
1. **Security & Secrets:**
   - NEVER read, write, or commit `.env` or `.env.*` files.
   - Do not hardcode API keys or credentials.
   - Respect `.claude/settings.json` deny boundaries.

2. **Code Standards & Architecture:**
   - Use Python standard library where possible before adding external dependencies.
   - Type hints must be used for public functions and classes.
   - Maintain docstrings and comments.
   - Exit codes: return code 0 on success, non-zero on failure.

3. **Multi-file Modification Protocol:**
   - Propose an explicit, file-based plan before making multi-file modifications.
   - Validate proposed changes against existing test suites.

4. **Testing & Verification:**
   - Always run `python -m unittest discover tests` after code changes.
   - Verify that all unit tests pass before committing.
