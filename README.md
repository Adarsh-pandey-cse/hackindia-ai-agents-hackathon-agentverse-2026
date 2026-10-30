# AgentVerse Autonomous AI Agent

[![HackIndia Skill](https://img.shields.io/badge/HackIndia%20Skill-Write%20a%20runnable%20Python%20tool-orange.svg)](https://hackindia.org/skills/write-a-runnable-python-tool)
[![Python Version](https://img.shields.io/badge/Python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Tests](https://img.shields.io/badge/Unit%20Tests-5%20Passed-brightgreen.svg)](tests/)

**Skill Submission:** [Write a runnable Python tool](https://hackindia.org/skills/write-a-runnable-python-tool)  
**Hackathon:** HackIndia AI Agents Hackathon - AgentVerse 2026  
**Developer:** Adarsh Pandey ([@adarsh-pandey-cse](https://github.com/adarsh-pandey-cse))  
**Repository:** [https://github.com/Adarsh-pandey-cse/hackindia-ai-agents-hackathon-agentverse-2026](https://github.com/Adarsh-pandey-cse/hackindia-ai-agents-hackathon-agentverse-2026)  
**Hackathon Team:** Adarsh Pandey's Team (`hackindia-ai-agents-hackathon-agentverse-2026-adarsh-pandeys-team`)  

---

## 📌 Project Overview

**AgentVerse Autonomous AI Agent** is a production-ready, command-line intelligence tool engineered for AI-adjacent analytical workflows. It ingests structured queries, queries live external REST APIs (with offline mock fallbacks), applies Python data-shaping comprehensions, and writes comprehensive JSON and Markdown reports.

This repository is built to fulfill all requirements of the **HackIndia "Write a runnable Python tool"** skill curriculum:

| Curriculum Lesson | Implementation in this Repository |
| :--- | :--- |
| **Lesson 1: Think in Python data** | Strongly typed data models (`TaskItem`, `AnalysisRecord`) using `@dataclass` |
| **Lesson 2: Shape data with comprehensions** | List, dict, and set comprehensions for filtering, mapping, and deduplication |
| **Lesson 3: Write functions and modules** | Clean architecture separated into `main.py`, `agent.py`, `api_client.py` |
| **Lesson 4: Use virtual environments cleanly** | Standardized `venv` workflow and pinned `requirements.txt` |
| **Lesson 5: Read files and JSON** | Context-managed file ingestion supporting both `.json` and `.csv` datasets |
| **Lesson 6: Call APIs from Python** | Robust REST API integration (GitHub, CoinGecko, HTTPBin) with mock fallbacks |
| **Lesson 7: Make it runnable by others** | Feature-rich CLI built with `argparse`, options, exit codes, and `--help` |
| **Lesson 8: Submit your Python repo** | 100% public GitHub repo authored by `@adarsh-pandey-cse` with verified outputs |

---

## 📂 Repository Structure

```text
.
├── README.md               # Complete project documentation and verification proof
├── requirements.txt        # Pinned Python package dependencies
├── main.py                 # Runnable CLI entry point (argparse)
├── agent.py                # Core autonomous intelligence agent & data engine
├── api_client.py           # REST API client with automatic mock fallbacks
├── walkthrough.ipynb       # Interactive Jupyter Notebook demonstration
├── data/
│   ├── sample_input.json   # Sample input dataset (JSON format)
│   └── sample_input.csv    # Sample input dataset (CSV format)
├── output/
│   ├── agent_results.json  # Generated structured JSON report
│   ├── agent_summary.md    # Generated executive Markdown report
│   └── execution_proof.log # Persistent runtime execution and API telemetry log
└── tests/
    └── test_agent.py       # Automated unit test suite (5 tests, 100% pass)
```

---

## 🚀 Setup Instructions

### 1. Prerequisites
- **Python 3.9+** (Tested on Python 3.12.10)
- `pip` (Python package manager)
- `git`

### 2. Clone the Repository
```bash
git clone https://github.com/Adarsh-pandey-cse/hackindia-ai-agents-hackathon-agentverse-2026.git
cd hackindia-ai-agents-hackathon-agentverse-2026
```

### 3. Create and Activate Virtual Environment
**On Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**On Windows (Command Prompt):**
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

**On macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 💻 How to Run the Tool

### Option A: Standard Run (Zero-config default)
```bash
python main.py
```

### Option B: View Help & CLI Options
```bash
python main.py --help
```

```text
options:
  -h, --help            show this help message and exit
  -i INPUT_FILE, --input INPUT_FILE
                        Path to input task dataset (.json or .csv). Default: data/sample_input.json
  -o OUTPUT_DIR, --output-dir OUTPUT_DIR
                        Directory to save generated JSON, Markdown, and log outputs. Default: output
  -p {ALL,HIGH,MEDIUM,LOW}, --priority {ALL,HIGH,MEDIUM,LOW}
                        Filter tasks by minimum priority level. Default: ALL
  --mock                Force mock API simulation mode (offline / isolated sandbox test)
  -v, --verbose         Enable detailed debug logs
```

### Option C: Run with CSV Input and Priority Filter
```bash
python main.py --input data/sample_input.csv --priority HIGH
```

### Option D: Run in Offline Mock Mode
```bash
python main.py --mock
```

---

## 🧪 Running Unit Tests

The repository includes a comprehensive `unittest` suite testing data loading, comprehensions, mock APIs, and file generation:

```bash
python -m unittest discover tests
```

Expected output:
```text
.....
----------------------------------------------------------------------
Ran 5 tests in 0.003s

OK
```

---

## 📓 Interactive Jupyter Notebook

For evaluators who prefer inspecting or running the pipeline interactively, open [`walkthrough.ipynb`](walkthrough.ipynb):

```bash
pip install jupyter
jupyter notebook walkthrough.ipynb
```

The notebook contains pre-computed cell outputs demonstrating:
1. Ingestion of `data/sample_input.json`
2. Priority filtering via list comprehensions
3. Dispatching API calls and capturing responses
4. Exporting structured JSON and Markdown reports

---

## 📊 Proof of Execution

When executed, the tool outputs real-time logs to console and writes verified outputs to `output/`:

### 1. Terminal Run Output:
```text
========================================================================
  AgentVerse Autonomous AI Agent - HackIndia 2026
  Skill: Write a runnable Python tool
  Developer: @adarsh-pandey-cse (Adarsh Pandey)
========================================================================
[2026-10-30 11:53:30] [INFO] [AgentVerse.Main]: Starting AgentVerse Autonomous Agent session...
[2026-10-30 11:53:30] [INFO] [AgentVerse.Main]: Configuration: input=data/sample_input.json, output_dir=output, mock=False
[2026-10-30 11:53:30] [INFO] [AgentVerse.Main]: [STEP 1/3] Reading data from: data/sample_input.json
[2026-10-30 11:53:30] [INFO] [AgentVerse.Agent]: Loading input dataset from: data/sample_input.json
[2026-10-30 11:53:30] [INFO] [AgentVerse.Agent]: Successfully loaded and validated 3 tasks.
[*] Successfully ingested 3 tasks.
[2026-10-30 11:53:30] [INFO] [AgentVerse.Main]: [STEP 2/3] Calling external REST APIs & mock fallbacks...
[2026-10-30 11:53:30] [INFO] [AgentVerse.Agent]: [1/3] Executing task 'TASK-001': Autonomous AI Agents in 2026 (HIGH)
[2026-10-30 11:53:30] [INFO] [AgentVerse.APIClient]: Dispatching API call for category 'ai_tech_trends' on topic: 'Autonomous AI Agents in 2026'
[2026-10-30 11:53:31] [INFO] [AgentVerse.Agent]: [2/3] Executing task 'TASK-002': Cryptocurrency and Web3 Ecosystem Metrics (MEDIUM)
[2026-10-30 11:53:31] [INFO] [AgentVerse.APIClient]: Dispatching API call for category 'market_indicators' on topic: 'Cryptocurrency and Web3 Ecosystem Metrics'
[2026-10-30 11:53:32] [INFO] [AgentVerse.Agent]: [3/3] Executing task 'TASK-003': Open Source AI Tools & Frameworks (HIGH)
[2026-10-30 11:53:32] [INFO] [AgentVerse.APIClient]: Dispatching API call for category 'developer_ecosystem' on topic: 'Open Source AI Tools & Frameworks'
[2026-10-30 11:53:32] [INFO] [AgentVerse.Agent]: Completed execution of 3 analytical tasks.
[*] Completed 3 API-backed analytical tasks.
[2026-10-30 11:53:32] [INFO] [AgentVerse.Main]: [STEP 3/3] Exporting structured reports to: output
[2026-10-30 11:53:32] [INFO] [AgentVerse.Agent]: Saved JSON results to: output\agent_results.json
[2026-10-30 11:53:32] [INFO] [AgentVerse.Agent]: Saved Markdown report to: output\agent_summary.md
[+] Output JSON Report:     output\agent_results.json
[+] Output Markdown Report: output\agent_summary.md
[+] Execution Proof Log:    output\execution_proof.log

========================================================================
  AGENT EXECUTION COMPLETED SUCCESSFULLY (EXIT CODE 0)
========================================================================
 - [TASK-001] Autonomous AI Agents in 2026               | HTTPBin REST Endpoint (Live Echo API) | 1236.79ms [success]
 - [TASK-002] Cryptocurrency and Web3 Ecosystem Metrics  | CoinGecko REST API               | 718.84ms [success]
 - [TASK-003] Open Source AI Tools & Frameworks          | GitHub Public API                | 682.88ms [success]
```

### 2. Verifiable Output Artifacts:
- **Data Ingestion Proof:** [`data/sample_input.json`](data/sample_input.json) and [`data/sample_input.csv`](data/sample_input.csv)
- **API Call Proof:** Live queries recorded with status codes and latencies in [`output/execution_proof.log`](output/execution_proof.log)
- **Generated JSON Data:** [`output/agent_results.json`](output/agent_results.json)
- **Generated Executive Summary:** [`output/agent_summary.md`](output/agent_summary.md)

---

## 📜 HackIndia Verification Checklist

- [x] **Public repository:** Publicly accessible on GitHub.
- [x] **Commits by `@adarsh-pandey-cse`:** All commits authored by Adarsh Pandey (`adarshpandey.cse@gmail.com`).
- [x] **Runnable Python script:** `main.py` is fully executable with `--help` and CLI flags.
- [x] **Clear setup steps:** Step-by-step virtualenv, pip install, and execution commands documented.
- [x] **`requirements.txt`:** Pinned runtime dependencies included.
- [x] **Sample input:** Provided in `data/sample_input.json` and `data/sample_input.csv`.
- [x] **Proof script reads data:** File parsing logic in `agent.py` loads and validates input files.
- [x] **Proof script calls API or mock API:** `api_client.py` makes live HTTP requests with mock fallback.
- [x] **Proof script writes useful output:** Outputs saved to `output/agent_results.json`, `output/agent_summary.md`, and `output/execution_proof.log`.
- [x] **Jupyter Notebook included:** [`walkthrough.ipynb`](walkthrough.ipynb) with executed cell outputs.

---

## 📄 License

This project is open-source under the [MIT License](LICENSE).
