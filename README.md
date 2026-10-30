# AgentVerse Autonomous AI Agent

**Hackathon:** HackIndia AI Agents Hackathon - AgentVerse 2026  
**Developer:** Adarsh Pandey ([@adarsh-pandey-cse](https://github.com/adarsh-pandey-cse))  
**Repository:** [Adarsh-pandey-cse/hackindia-ai-agents-hackathon-agentverse-2026](https://github.com/Adarsh-pandey-cse/hackindia-ai-agents-hackathon-agentverse-2026)  
**Hackathon Team:** Adarsh Pandey's Team (`hackindia-ai-agents-hackathon-agentverse-2026-adarsh-pandeys-team`)  

---

## Overview

**AgentVerse Autonomous AI Agent** is an intelligent, automated data-gathering and synthesis pipeline designed for market intelligence, developer ecosystem tracking, and technological trend evaluation. 

The project satisfies all requirements for the HackIndia Python skill verification:
1. **Reads Data:** Ingests structured task parameters from [`data/sample_input.json`](data/sample_input.json).
2. **Calls External & Mock APIs:** Interacts with live REST APIs (GitHub REST API, CoinGecko Market API, and HTTPBin Echo API) with automatic, resilient fallback to mock APIs.
3. **Writes Useful Output:** Generates structured machine-readable JSON data ([`output/agent_results.json`](output/agent_results.json)), an executive Markdown report ([`output/agent_summary.md`](output/agent_summary.md)), and full execution logs ([`output/execution_proof.log`](output/execution_proof.log)).

---

## Project Structure

```text
.
├── README.md               # Documentation and setup instructions
├── requirements.txt        # Python package dependencies
├── main.py                 # Application entry point & orchestration
├── agent.py                # Core autonomous agent & synthesis engine
├── api_client.py           # REST API & mock fallback handler
├── data/
│   └── sample_input.json   # Sample input task configuration
└── output/
    ├── agent_results.json  # Generated JSON report from agent execution
    ├── agent_summary.md    # Generated Markdown executive summary
    └── execution_proof.log # Runtime execution logs and API verification
```

---

## Setup Instructions

### 1. Prerequisites
- **Python 3.9+** (Tested on Python 3.12)
- `pip` package manager

### 2. Create and Activate a Virtual Environment

On Windows (PowerShell):
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

On Linux / macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## How to Run

Execute the main script:
```bash
python main.py
```

### Terminal Output Preview:
```text
======================================================================
  AgentVerse Autonomous AI Agent - HackIndia 2026
  Developer: @adarsh-pandey-cse (Adarsh Pandey)
======================================================================
[2026-10-30 11:30:52] [INFO] [AgentVerse.Main]: Initializing AgentVerse Autonomous Agent session...
[2026-10-30 11:30:52] [INFO] [AgentVerse.Main]: [STEP 1/3] Ingesting sample input dataset from data/sample_input.json
[2026-10-30 11:30:52] [INFO] [AgentVerse.Agent]: Loading input task data from: data/sample_input.json
[2026-10-30 11:30:52] [INFO] [AgentVerse.Agent]: Loaded 3 tasks from input file.
[*] Ingested 3 tasks for processing.
[2026-10-30 11:30:52] [INFO] [AgentVerse.Main]: [STEP 2/3] Calling live REST APIs & mock fallbacks for intelligence gathering
[2026-10-30 11:30:52] [INFO] [AgentVerse.Agent]: [1/3] Processing TASK-001: 'Autonomous AI Agents in 2026' (Priority: HIGH)
[2026-10-30 11:30:54] [INFO] [AgentVerse.Agent]: [2/3] Processing TASK-002: 'Cryptocurrency and Web3 Ecosystem Metrics' (Priority: MEDIUM)
[2026-10-30 11:30:54] [INFO] [AgentVerse.Agent]: [3/3] Processing TASK-003: 'Open Source AI Tools & Frameworks' (Priority: HIGH)
[*] Completed 3 API-backed analytical tasks.
[2026-10-30 11:30:55] [INFO] [AgentVerse.Main]: [STEP 3/3] Exporting structured results & executive markdown report to output/
[+] Output JSON Report:     output\agent_results.json
[+] Output Markdown Report: output\agent_summary.md
[+] Execution Proof Log:    output/execution_proof.log

======================================================================
  AGENT EXECUTION COMPLETED SUCCESSFULLY!
======================================================================
 - [TASK-001] Autonomous AI Agents in 2026: HTTPBin REST Endpoint (Live Echo API) (Status: success)
 - [TASK-002] Cryptocurrency and Web3 Ecosystem Metrics: CoinGecko REST API (Status: success)
 - [TASK-003] Open Source AI Tools & Frameworks: GitHub Public API (Status: success)
```

---

## Proof of Execution

The agent leaves persistent verifiable proof of execution in the `output/` directory:
- **Data Reading Proof:** Loaded 3 tasks from `data/sample_input.json`.
- **API Call Proof:** Live queries made to GitHub API, CoinGecko API, and HTTPBin Echo API with sub-second latencies recorded.
- **Output Writing Proof:** 
  - [`output/agent_results.json`](output/agent_results.json)
  - [`output/agent_summary.md`](output/agent_summary.md)
  - [`output/execution_proof.log`](output/execution_proof.log)

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
