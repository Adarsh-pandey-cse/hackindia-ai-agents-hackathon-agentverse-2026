# AGENTS.md - Agent Operations & Operating Guide

## Project Overview
**AgentVerse Autonomous AI Agent & ML Pipeline**  
HackIndia AI Agents Hackathon - AgentVerse 2026  
Developer: Adarsh Pandey ([@adarsh-pandey-cse](https://github.com/adarsh-pandey-cse))

This repository contains four production components:
1. **Autonomous Intelligence CLI Tool (`main.py`):** Ingests structured task data (`.json` or `.csv`), executes external REST queries (with automatic mock fallbacks), applies data shaping, and generates structured JSON and Markdown summary reports.
2. **Machine Learning Pipeline (`train_ml_model.py`):** Trains and evaluates a scikit-learn classifier to predict agent workload execution success on unseen test data.
3. **Grounded Document QA RAG Engine (`app.py`, `ingest.py`, `evaluate.py`):** Chunks multi-page texts with metadata, executes vector/keyword retrieval, generates grounded answers with verifiable citations (`[source: <chunk_id>, page: <page>]`), flags broken citations, refuses unanswerable queries, and executes automated grounding evaluations.
4. **Safe Tool-Calling Agent (`src/agent_loop.py`, `src/tools/`, `safe_agent_cli.py`):** Implements tool schemas, call-result loops, human approval gates for high-risk write operations, and hard safety limits (turn budgets, tool call caps, timeouts, failure stops).

---

## Architecture & Code Map
- `main.py`: Entry point for CLI tool. Uses `argparse` with flags `--input`, `--output-dir`, `--priority`, `--mock`, `--verbose`.
- `agent.py`: Core agent logic (`AgentVerseAgent`). Uses `@dataclass` (`TaskItem`, `AnalysisRecord`) and list comprehensions.
- `api_client.py`: External REST client (`ExternalAPIClient`) with live endpoints and instant offline fallback mocks.
- `train_ml_model.py`: Scikit-learn training and evaluation pipeline. Stratified 80/20 train/test split, StandardScaler, model comparison, joblib serialization, JSON/MD metric reports.
- `app.py`: Grounded document question answering system with prompt synthesis, citation verification, and hallucination refusal.
- `ingest.py`: Chunking and metadata extractor for documents in `data/sample_docs/`.
- `evaluate.py`: Automated evaluation runner checking citations, answer correctness, and refusal behavior on benchmark queries.
- `safe_agent_cli.py`: CLI runner for safe tool-calling agent with `--auto-approve`, `--reject-risky`, `--list-tools`.
- `src/agent_loop.py`: Call-result agent loop (`SafeToolCallingAgent`) with limits and approval gates.
- `src/tools/`: Schemas (`schemas.py`) and handlers (`implementations.py`) with risk tagging.
- `docs/agent_vs_script.md`: Architectural documentation on agent vs script trade-offs.
- `tests/`: Automated unit tests (`test_agent.py`, `test_ml_model.py`, `test_rag.py`, `test_safe_agent.py`, `test_agent.js`). Run with `python -m unittest discover tests` and `npm test`.
- `data/`: Dataset storage (`sample_input.json`, `sample_input.csv`, `agent_workload_dataset.csv`, `chunks.json`, `sample_docs/`).
- `examples/`: Sample benchmark questions (`questions.json`) and documented cited answers (`cited_answers.md`).
- `eval/`: Grounding evaluation report (`grounding_eval.md`).
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
