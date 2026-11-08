# AgentVerse Autonomous AI Agent & ML Pipeline

[![HackIndia Python Skill](https://img.shields.io/badge/HackIndia%20Skill-Write%20a%20runnable%20Python%20tool-orange.svg)](https://hackindia.org/skills/write-a-runnable-python-tool)
[![HackIndia ML Skill](https://img.shields.io/badge/HackIndia%20Skill-Ship%20your%20first%20ML%20repo-purple.svg)](https://hackindia.org/skills/ship-your-first-ml-repo)
[![HackIndia Claude Code Skill](https://img.shields.io/badge/HackIndia%20Skill-Ship%20faster%20with%20Claude%20Code-blueviolet.svg)](https://hackindia.org/skills/ship-faster-with-claude-code)
[![HackIndia Design Skill](https://img.shields.io/badge/HackIndia%20Skill-Design%20a%20usable%20hackathon%20app-crimson.svg)](https://hackindia.org/skills/design-a-usable-hackathon-app)
[![HackIndia JavaScript Skill](https://img.shields.io/badge/HackIndia%20Skill-Write%20JavaScript%20without%20guessing-yellow.svg)](https://hackindia.org/skills/write-javascript-without-guessing)
[![HackIndia RAG Skill](https://img.shields.io/badge/HackIndia%20Skill-Build%20a%20grounded%20document%20QA%20app-teal.svg)](https://hackindia.org/skills/build-a-grounded-document-qa-app)
[![HackIndia Safe Tool Calling Agent Skill](https://img.shields.io/badge/HackIndia%20Skill-Build%20a%20safe%20tool--calling%20agent-darkred.svg)](https://hackindia.org/skills/build-a-safe-tool-calling-agent)
[![HackIndia Honest Model Results](https://img.shields.io/badge/HackIndia%20Skill-Report%20model%20results%20honestly-blue.svg)](https://hackindia.org/skills/report-model-results-honestly)
[![HackIndia Docker Skill](https://img.shields.io/badge/HackIndia%20Skill-Dockerize%20a%20web%20app-2496ED.svg?logo=docker&logoColor=white)](https://hackindia.org/skills/dockerize-a-web-app)
[![Python Version](https://img.shields.io/badge/Python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue.svg)](https://www.python.org/)
[![Node.js Version](https://img.shields.io/badge/Node.js-18%20%7C%2020%20%7C%2022%20%7C%2024-green.svg)](https://nodejs.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Unit Tests](https://img.shields.io/badge/Unit%20Tests-30%20Passed%20(Python%20%2B%20Node.js)-brightgreen.svg)](tests/)

**Submitted Skills:**
1. [Write a runnable Python tool](https://hackindia.org/skills/write-a-runnable-python-tool)
2. [Ship your first ML repo](https://hackindia.org/skills/ship-your-first-ml-repo)
3. [Ship faster with Claude Code](https://hackindia.org/skills/ship-faster-with-claude-code)
4. [Design a usable hackathon app](https://hackindia.org/skills/design-a-usable-hackathon-app)
5. [Write JavaScript without guessing](https://hackindia.org/skills/write-javascript-without-guessing)
6. [Build a grounded document QA app](https://hackindia.org/skills/build-a-grounded-document-qa-app)
7. [Build a safe tool-calling agent](https://hackindia.org/skills/build-a-safe-tool-calling-agent)
8. [Report model results honestly](https://hackindia.org/skills/report-model-results-honestly)
9. [Dockerize a web app](https://hackindia.org/skills/dockerize-a-web-app)

**Hackathon:** HackIndia AI Agents Hackathon - AgentVerse 2026  
**Developer:** Adarsh Pandey ([@adarsh-pandey-cse](https://github.com/adarsh-pandey-cse))  
**Repository (Team Fork):** [https://github.com/Adarsh-pandey-cse/hackindia-ai-agents-hackathon-agentverse-2026-adarsh-pandeys-team](https://github.com/Adarsh-pandey-cse/hackindia-ai-agents-hackathon-agentverse-2026-adarsh-pandeys-team)  
**Hackathon Team Repository:** [https://github.com/HackIndiaXYZ/hackindia-ai-agents-hackathon-agentverse-2026-adarsh-pandeys-team](https://github.com/HackIndiaXYZ/hackindia-ai-agents-hackathon-agentverse-2026-adarsh-pandeys-team) (PR [#1](https://github.com/HackIndiaXYZ/hackindia-ai-agents-hackathon-agentverse-2026-adarsh-pandeys-team/pull/1))  
**Standalone Repository:** [https://github.com/Adarsh-pandey-cse/hackindia-ai-agents-hackathon-agentverse-2026](https://github.com/Adarsh-pandey-cse/hackindia-ai-agents-hackathon-agentverse-2026)  
**Hackathon Team:** Adarsh Pandey's Team (`hackindia-ai-agents-hackathon-agentverse-2026-adarsh-pandeys-team`)  

---

## 📌 Project Overview

![System Architecture](assets/architecture_diagram.png)

**AgentVerse Autonomous AI Agent & ML Pipeline** is a complete, multi-tiered engineering system designed for AI agents hackathon workflows:

1. **Autonomous Intelligence Agent CLI (`main.py`):** Ingests structured task feeds (`.json` or `.csv`), queries live external REST APIs (GitHub, CoinGecko, HTTPBin) with automatic offline mock fallbacks, applies Python data-shaping comprehensions, and writes structured JSON & Markdown reports. Built for the **[Write a runnable Python tool](https://hackindia.org/skills/write-a-runnable-python-tool)** skill.
2. **Scikit-Learn Machine Learning Pipeline (`train_ml_model.py`):** Trains, evaluates, and exports a production predictive model that forecasts agent task execution success/failure based on runtime workload metrics. Features stratified train/test split, feature scaling, model family benchmark comparisons, serialization to `.joblib`, and metric reports. Built for the **[Ship your first ML repo](https://hackindia.org/skills/ship-your-first-ml-repo)** skill.
3. **Claude Code & Agent Context Integration:** Full project context orchestration via `CLAUDE.md`, `@AGENTS.md` import, safe shared settings in `.claude/settings.json`, and `.cursorrules` to guarantee secure, repeatable, and collaborative AI development. Built for the **[Ship faster with Claude Code](https://hackindia.org/skills/ship-faster-with-claude-code)** skill.
4. **Interactive UI/UX & Design System (`web/index.html` & `docs/screens/`):** Accessible, responsive 3-screen interface showcasing visual hierarchy, 8px spacing scale, readable typography, WCAG AAA contrast, human-friendly empty states, and explicit error recovery copy. Built for the **[Design a usable hackathon app](https://hackindia.org/skills/design-a-usable-hackathon-app)** skill.
5. **Modular JavaScript Engine (`src/` & `web/js/`):** Clean, non-guessing JavaScript architecture using modern ES modules, pure functions, immutable array operations (`map`, `filter`, copy-before-sort), robust `async/await` network queries with `response.ok` checks, Node.js CLI script, and automated test suite. Built for the **[Write JavaScript without guessing](https://hackindia.org/skills/write-javascript-without-guessing)** skill.
6. **Grounded Document QA RAG App (`app.py`, `ingest.py`, `evaluate.py`):** Production Retrieval-Augmented Generation application that ingests multi-page documents, indexes text chunks with rich source/page metadata, retrieves evidence, constructs grounded prompts, generates answers with verbatim source citations (`[source: <chunk_id>, page: <page>]`), flags broken citations, strictly refuses out-of-scope queries to prevent hallucination, and includes an automated grounding evaluation (`eval/grounding_eval.md`). Built for the **[Build a grounded document QA app](https://hackindia.org/skills/build-a-grounded-document-qa-app)** skill.
7. **Safe Tool-Calling Agent (`src/agent_loop.py`, `src/tools/`, `safe_agent_cli.py`):** Production tool-calling system featuring explicit tool JSON schemas, complete call-result loop, interactive human approval gates for high-risk operations (email dispatch, database mutation), hard limits (`max_turns`, `max_tool_calls`, `max_seconds`, consecutive failure stops), and documented trade-offs explaining when a deterministic script is superior. Built for the **[Build a safe tool-calling agent](https://hackindia.org/skills/build-a-safe-tool-calling-agent)** skill.

---

## ⚡ JavaScript Architecture & Implementation (HackIndia JS Skill)

A modular, robust JavaScript subsystem powering both the browser application and the Node.js agent execution engine.

### Features
- **Asynchronous Data Ingestion:** Fetches task feeds asynchronously using `fetch()` and `async/await` with offline fallback resilience.
- **Strict Data Validation:** Catches missing attributes and null/undefined values before execution without guessing or assuming loose truthiness.
- **Dynamic Card & Table Rendering:** Generates clean, accessible DOM elements with visual hierarchy and badge indicators.
- **Real-Time Filtering & Immutability:** Filters tasks by keyword and priority while keeping original data stores completely immutable.
- **Accessible State Handling:** Displays responsive empty states for zero-result queries and clear, human-readable error banners for invalid inputs.

### JavaScript Used
- **Modules (`src/` and `web/js/`):** Code is split into focused ES modules with single responsibilities:
  - `src/data.js`: Pure data functions, validation, immutable filtering, and ID-based updates.
  - `src/api.js`: Network queries with `fetch()`, `async/await`, `response.ok` status validation, abort controller timeouts, and fallback handling.
  - `src/render.js`: DOM rendering functions for task rows, empty states, and error alerts.
  - `src/main.js`: Browser entry point wiring event listeners, state updates, and rendering.
  - `src/agent_cli.js`: Standalone Node.js CLI runner executing tasks from the terminal.
- **Functions:** Every function has a single job with explicit inputs, outputs, and zero unintended side effects.
- **Arrays & Objects:** Workload records stored as arrays of objects; updates target specific tasks by unique `id` rather than fragile array indices.
- **fetch & async/await:** Network queries explicitly check `response.ok` before reading JSON payloads and safely catch timeouts.

### How to Run JavaScript

#### Option 1: Run Interactive Browser App
```bash
# Launch using Python local server
python web_app.py

# Or launch using Node.js / npx serve
npx serve web -p 8080
```
Open **`http://localhost:8080`** in any browser.

#### Option 2: Run Node.js CLI Agent
```bash
node src/agent_cli.js
# Or via npm
npm run cli
```

#### Option 3: Run Automated JavaScript Unit Tests
```bash
node --test tests/test_agent.js
# Or via npm
npm test
```

Expected test output:
```text
✔ validateTask: accepts valid task object
✔ validateTask: catches missing properties and null values
✔ filterTasks: filters by search query and priority without mutating original
✔ sortTasksByPriority: sorts high to low immutably
✔ updateTaskById: updates by ID rather than index
✔ normalizeTasks: parses both arrays and nested query_tasks payloads
✔ queryExternalApi: handles network call or falls back to mock resilience
ℹ tests 7 | pass 7 | fail 0
```

### Known Issues
- Local task updates reset upon full browser page refresh (persists in-memory for the active session).
- Search currently matches across `topic`, `category`, and `id` properties.

---

## 🎨 Interface design proof

**Project:** AgentVerse Autonomous AI Agent & ML Pipeline  

### Working screens / flows:

#### 1. Agent Control Dashboard & Analytics View (`docs/screens/home.png`)
- **Clear main action:** `"Run Workload Analysis"` (High-contrast Saffron `#f97316` button prominently placed in the hero action banner).
- **Cards & Layout:** Key performance indicators (Model Accuracy 96.25%, Total Workloads 1,200, API Latency 879ms, Active Agents 3) formatted in elevated surface cards using consistent 8px/16px/24px spacing grid.
- **Readable telemetry:** Execution queue with readable status pills (`HIGH`, `MEDIUM`, `COMPLETED`).

![Dashboard View](docs/screens/home.png)

---

#### 2. Task Explorer & Real-Time Search Results (`docs/screens/search-empty.png`)
- **Interactive Filtering:** Filter by keyword topic and priority level.
- **Empty state shown:** Triggered when no tasks match the filter criteria (e.g. searching `"quantum-crypto-2030"`).
- **Empty copy:** *"No matching agent tasks found. No active tasks match your search query 'quantum-crypto-2030' with priority 'HIGH'. Try searching with broader terms, clearing the filter, or ingesting a new dataset."*
- **Clear recovery action:** Prominent `[ ↺ Reset All Filters ]` button immediately restores the complete active task feed.

![Empty State View](docs/screens/search-empty.png)

---

#### 3. Dataset Diagnostics & Validation Form (`docs/screens/report-error.png`)
- **Error state shown:** High-contrast, accessible red alert box (`#450a0a` background with `#dc2626` border) displayed when payload validation fails.
- **Error copy:** *"Validation Error: Missing Required Field 'topic'. The task dataset in 'data/invalid_task_payload.json' is missing the mandatory 'topic' property in item index 2. Autonomous agent dispatch requires 4 mandatory attributes: 'id', 'category', 'topic', and 'priority'."*
- **Contextual Form Guidance:** Form fields clearly display inline validation alerts (*"⚠ Field cannot be empty. Please enter an analytical prompt."*).
- **Actionable Next Steps:** Direct recovery action buttons: `[ Load Valid Sample (JSON) ]` and `[ Inspect Schema Docs ]`.

![Error State View](docs/screens/report-error.png)

---

### Design checks:
- **Visual Hierarchy:** Primary action is visually unmistakable. Main headings (26px/20px bold) are distinctly larger than subheadings (16px) and body text (15px).
- **Consistent Spacing:** Built on a standardized 4px/8px/16px/24px spacing scale; all cards, headings, and buttons align to clear, consistent edges.
- **Readable Typography:** 15px/16px base body font size with 1.5 line height, ensuring effortless scanning across devices.
- **Accessible Contrast:** Meets WCAG AAA contrast guidelines with light text (`#f9fafb`) on dark slate (`#111827`), high-contrast saffron accent (`#f97316`), and dedicated error contrast (`#fca5a5` on `#450a0a`).
- **Responsive Width:** Layouts adapt seamlessly from 360px mobile viewports to 1440px desktop displays.

### Screenshots:
- [`docs/screens/home.png`](docs/screens/home.png)
- [`docs/screens/search-empty.png`](docs/screens/search-empty.png)
- [`docs/screens/report-error.png`](docs/screens/report-error.png)

---

## 📂 Repository Structure

```text
.
├── README.md                          # Comprehensive project documentation & evaluation proof
├── package.json                       # Node.js project manifest, ES module setup & scripts
├── requirements.txt                   # Pinned runtime dependencies (scikit-learn, joblib, requests, etc.)
│
├── [ JAVASCRIPT SUBSYSTEM (SRC & WEB) ]
├── src/
│   ├── data.js                        # Task validation, filtering, mapping & immutable sorting
│   ├── api.js                         # Asynchronous fetch client, response.ok checks & mock engine
│   ├── render.js                      # DOM rendering functions for cards, empty & error states
│   ├── main.js                        # Browser application coordinator & event bindings
│   └── agent_cli.js                   # Runnable Node.js CLI agent runner
├── web/
│   ├── index.html                     # Interactive 3-screen dashboard (Dashboard, Empty State, Error State)
│   └── js/                            # Browser-ready ES modules (synced with src/)
├── web_app.py                         # Lightweight local server to launch interactive web app
├── generate_screenshots.py            # Automated script to generate design proof screenshots
├── docs/
│   └── screens/
│       ├── home.png                   # Screen 1: Agent Dashboard & Control Center
│       ├── search-empty.png           # Screen 2: Task Explorer & Accessible Empty State
│       └── report-error.png           # Screen 3: Diagnostics & Accessible Error State
│
├── [ CLAUDE CODE & AGENT CONTEXT ]
├── CLAUDE.md                          # Operating guide for Claude Code (imports @AGENTS.md)
├── AGENTS.md                          # Autonomous agent operating rules and security policies
├── .cursorrules                       # Assistant guidelines for Cursor and AI pair programmers
├── .claude/
│   └── settings.json                  # Shared project settings (denies reading .env files)
│
├── [ PYTHON AGENT TOOL ]
├── main.py                            # Runnable CLI entry point with argparse options and exit codes
├── agent.py                           # Core autonomous intelligence agent & data-shaping engine
├── api_client.py                      # External REST API client with automatic mock fallbacks
├── walkthrough.ipynb                  # Interactive Python tool walkthrough notebook
├── data/
│   ├── sample_input.json              # Sample input dataset (JSON format)
│   └── sample_input.csv               # Sample input dataset (CSV format)
│
├── [ MACHINE LEARNING PIPELINE ]
├── train_ml_model.py                  # Scikit-learn model training, evaluation & export script
├── ml_training_walkthrough.ipynb      # Interactive ML training & evaluation Jupyter Notebook
├── data/
│   └── agent_workload_dataset.csv     # 1,200 sample agent workload dataset (6 features)
├── models/
│   ├── agent_workload_classifier.joblib  # Serialized champion scikit-learn classifier
│   └── scaler.joblib                  # Serialized StandardScaler
│
├── [ OUTPUTS & TELEMETRY ]
├── output/
│   ├── agent_results.json             # Generated agent structured JSON report
│   ├── agent_summary.md               # Generated agent executive Markdown report
│   ├── execution_proof.log            # Runtime telemetry log
│   ├── ml_evaluation_report.json      # ML test evaluation metrics (JSON)
│   └── ml_evaluation_summary.md       # ML test evaluation summary (Markdown)
│
└── [ AUTOMATED TESTS ]
└── tests/
    ├── test_agent.py                  # Python agent tool unit tests (5/5 passed)
    ├── test_ml_model.py               # Scikit-learn ML pipeline unit tests (2/2 passed)
    └── test_agent.js                  # Node.js JavaScript module unit tests (7/7 passed)
```

---

## 🛡️ Claude Code Integration & Safe Settings

This repository is structured for safe and rapid development with Claude Code, fulfilling all requirements of the **HackIndia Claude Code** curriculum:

1. **Context Management (`CLAUDE.md`):**
   - Placed at repository root `./CLAUDE.md`.
   - Imports `@AGENTS.md` so Claude Code automatically loads core repository architecture, guidelines, and operating constraints.
   - Defines verified commands for running, testing, and linting the codebase.
2. **Safe Shared Permissions (`.claude/settings.json`):**
   - Configures deny-first security rules preventing Claude Code from reading sensitive files:
     ```json
     {
       "permissions": {
         "deny": [
           "Read(./.env)",
           "Read(./.env.*)"
         ]
       }
     }
     ```
3. **Clean Git Isolation (`.gitignore`):**
   - Explicitly excludes `.env`, `.env.*`, and `.claude/settings.local.json` to keep personal overrides out of the public repo.
4. **Code Review & Pull Request:**
   - Multi-file modifications follow plan-first conventions.
   - All changes reviewed and pushed via clean commits and Pull Request [#1](https://github.com/HackIndiaXYZ/hackindia-ai-agents-hackathon-agentverse-2026-adarsh-pandeys-team/pull/1) on `HackIndiaXYZ`.

---

## 🚀 Setup Instructions

### 1. Prerequisites
- **Python 3.9+** (Tested on Python 3.12.10)
- **Node.js 18+** (Tested on Node.js v24.14.1)
- `pip` & `npm`
- `git`

### 2. Clone the Repository
```bash
git clone https://github.com/Adarsh-pandey-cse/hackindia-ai-agents-hackathon-agentverse-2026-adarsh-pandeys-team.git
cd hackindia-ai-agents-hackathon-agentverse-2026-adarsh-pandeys-team
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
# Python dependencies
pip install -r requirements.txt

# Node.js dependencies (zero external dependencies required)
npm test
```

---

## 💻 Running the Projects

### Part 1: Interactive Web App & UI Dashboard
Launch the local web server to inspect all 3 screens and flows:
```bash
python web_app.py
```
Open **`http://localhost:8080`** in any browser.

---

### Part 2: Autonomous Agent CLI Tool (`main.py`)
Run the Python agent tool with zero configuration:
```bash
python main.py
```

View CLI options:
```bash
python main.py --help
```

Run with custom CSV input and priority filtering:
```bash
python main.py --input data/sample_input.csv --priority HIGH
```

---

### Part 3: Node.js CLI Agent (`src/agent_cli.js`)
Run the JavaScript agent directly in Node.js:
```bash
node src/agent_cli.js
```

---

### Part 4: Machine Learning Training & Evaluation (`train_ml_model.py`)
Run the complete scikit-learn training and evaluation pipeline:
```bash
python train_ml_model.py
```

---

## 🤖 Machine Learning Model & Evaluation Details (HackIndia Honest Results Skill)

### Model Evaluation

**Dataset:**  
Used 1,200 labelled agent task executions collected from our benchmark workload dataset (`data/agent_workload_dataset.csv`). Target label: `1` (successful execution within SLA) vs `0` (failure/timeout). Features include prompt length, external API query count, priority weight, memory context footprint, execution timeout, and network latency.

**Split method:**  
80/20 stratified split with a fixed random seed (`random_state=42`).  
- Train: 960 rows.  
- Validation / Test: 240 held-out rows.

**Baseline:**  
Majority-class baseline predicts `1` (success) for every workload. Baseline accuracy: **81.25%** (195 / 240).

**Model result:**  
Validation accuracy: **96.25%** (outperforms majority-class baseline by +15.00%).  
Key metric: macro **F1-score = 0.9771** (Precision: 0.9697, Recall: 0.9846), chosen prior to model tuning because workload success classes are imbalanced (81.25% success vs 18.75% failure).

**Confusion matrix:**  
Rows are actual labels. Columns are predicted labels (`0` = failure, `1` = success).

```
                      Predicted 0 (Failure)   Predicted 1 (Success)
Actual 0 (Failure)                  39 (TN)                  6 (FP)
Actual 1 (Success)                   3 (FN)                192 (TP)
```

**Limitation:**  
The model was evaluated exclusively on structured agent workload telemetry with prompt lengths up to 4,000 tokens and network latency between 20ms and 800ms. It may perform worse on multi-modal streaming inputs or under extreme network packet loss where timeout behaviors deviate from normal distributions. For this reason, we would not use it as an unmonitored hard-kill mechanism without human supervisor review.

---

### Candidate Model Comparison on Test Split
We benchmarked three diverse scikit-learn model families:

| Model Family | Hyperparameters | Test Accuracy | Test F1-Score | Status |
| :--- | :--- | :---: | :---: | :---: |
| **Logistic Regression** | `max_iter=1000, random_state=42` | **96.25%** | **0.9771** | **Champion Model Selected** |
| **Random Forest** | `n_estimators=100, max_depth=10, random_state=42` | 94.58% | 0.9666 | Candidate |
| **Decision Tree** | `max_depth=5, random_state=42` | 94.58% | 0.9666 | Candidate |

---

## 📚 Grounded Document QA RAG App (HackIndia RAG Skill)

Ask questions from the sample documents and get answers with citations.

### Features
- **Loads documents from `data/sample_docs/`:** Ingests `college_faq.txt` and `refund_policy.txt`.
- **Splits documents and creates embeddings:** Chunks pages into structured records with rich metadata (`chunk_id`, `source`, `page`, `word_count`).
- **Retrieves evidence for each question:** High-speed vector similarity and keyword search ranking the most relevant chunks.
- **Answers with source citations:** Every factual claim cites the exact chunk and page: `[source: <chunk_id>, page: <page>]`.
- **Strict Anti-Hallucination Guardrail:** If evidence is missing, the app strictly refuses to guess and answers: *"I could not find this in the provided documents."*
- **Broken Citation Verification:** Validates generated citation tags against retrieved chunk IDs, flagging any fabricated or out-of-retrieval citations.
- **Automated Grounding Evaluation:** Benchmark runner evaluating accuracy, citation precision, and refusal behavior (`eval/grounding_eval.md`).

### Setup & Quickstart
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Adarsh-pandey-cse/hackindia-ai-agents-hackathon-agentverse-2026-adarsh-pandeys-team.git
   cd hackindia-ai-agents-hackathon-agentverse-2026-adarsh-pandeys-team
   ```
2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # Linux/macOS:
   source .venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Copy environment template:**
   ```bash
   cp .env.example .env
   ```
   *(Optional: Set `OPENAI_API_KEY` or `GEMINI_API_KEY`. Runs 100% offline with zero external network dependencies out of the box).*
5. **Run document ingestion:**
   ```bash
   python ingest.py
   ```
   *Extracts 10 structured chunks from `data/sample_docs/` into `data/chunks.json` and creates a persistent vector index.*
6. **Start the app:**
   ```bash
   # Interactive Mode:
   python app.py

   # Single Query Mode:
   python app.py --query "What is the refund window?"
   ```
7. **Run the grounding evaluation:**
   ```bash
   python evaluate.py
   ```

### Try these questions
- What is the refund window?
- Who can apply for the hostel Wi-Fi pass?
- Can I pay semester fees using UPI, and what happens if I pay late?
- What administrative processing fee is deducted from approved refund requests?
- Are students permitted to park personal electric scooters inside hostel bedrooms? *(Tests anti-hallucination refusal)*

### Grounding Evaluation
See [`eval/grounding_eval.md`](eval/grounding_eval.md) for benchmark questions, answers, citations, and grounding validation results (100% pass rate across 6 test cases).

---

## 🛡️ Safe Tool-Calling Agent (HackIndia Skill)

### Project: Campus Event & Reimbursement Assistant

### What it does
Helps students discover campus events, verify rules, calculate travel/registration reimbursements against institutional expense caps, draft formal communications, and request human supervisor approval before executing external dispatches or database modifications.

### How to run
1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Add required environment variables (optional):**
   ```bash
   cp .env.example .env
   ```
   *(Works 100% offline out-of-the-box with deterministic mock planning and tool execution).*
3. **Run the agent with sample requests:**
   ```bash
   # Multi-turn event discovery & draft registration (Interactive Human Approval Gate):
   python safe_agent_cli.py --goal "Find AI events in Bengaluru and draft registration"

   # Calculate reimbursement with automatic approval for CI/testing:
   python safe_agent_cli.py --goal "Calculate reimbursement for travel expenses: 450, 1200, 350" --auto-approve

   # Test simulated human rejection on risky operations:
   python safe_agent_cli.py --goal "Find AI events and send registration email" --reject-risky

   # Inspect registered tool schemas and risk classifications:
   python safe_agent_cli.py --list-tools
   ```

### Safety features
- **Tool schemas are in:** [`src/tools/schemas.py`](src/tools/schemas.py) (strict JSON schemas, typing, and risk levels: `low` vs `high`).
- **Call-result loop is in:** [`src/agent_loop.py`](src/agent_loop.py) (`SafeToolCallingAgent` handles model tool requests, validation, tool feedback, and loop termination).
- **Approval gate is used before:** `send_registration_email` (external communication) and `update_student_record` (database mutation).
- **Hard limits used:**
  - `max_turns = 8`: Stops runaway iteration loops.
  - `max_tool_calls = 12`: Enforces strict API / tool execution budget.
  - `max_seconds = 30.0s`: Hard timeout wall.
  - `max_failures = 2`: Halts execution immediately upon consecutive tool errors.
- **Risky actions are not run without human approval:** If a human supervisor rejects a gated action, execution halts safely without modifying state.

### When I would replace this with a script
I would use a script if the workflow steps are fixed: reading a CSV, calculating expense totals, filling an HTML template, and generating a PDF report. I use an agent only when the request needs runtime judgement, such as interpreting ambiguous user intents, choosing dynamically which tool to call based on prior tool outputs, or asking follow-up questions.
See detailed architecture analysis in [`docs/agent_vs_script.md`](docs/agent_vs_script.md).

---

## 🐳 Run Locally with Docker (HackIndia Docker Skill)

Package the web app and database so it runs the exact same way on any machine.

### 1. Clone the repo
```bash
git clone https://github.com/Adarsh-pandey-cse/hackindia-ai-agents-hackathon-agentverse-2026-adarsh-pandeys-team.git
cd hackindia-ai-agents-hackathon-agentverse-2026-adarsh-pandeys-team
```

### 2. Create the environment file
```bash
cp .env.example .env
```

### 3. Start the app and database
```bash
docker compose up --build
```

### 4. Open the app
- **Interactive Web UI:** [http://localhost:3000](http://localhost:3000)
- **Health Check API:** [http://localhost:3000/health](http://localhost:3000/health) (expected response: `{"status":"ok"}`)

### Architecture & Security Details
- **Base image:** Official `python:3.12-slim` image for a fast, minimal container footprint.
- **Dependency caching:** `requirements.txt` is copied and installed before application code to leverage Docker layer caching.
- **Port isolation:** Exposes and maps only the web application port (`3000:3000`); the Postgres database container (`db`) communicates exclusively over the internal Docker network (`db:5432`) without publishing public host ports.
- **Data persistence:** PostgreSQL container data is safely persisted across restarts using the named volume `agentverse_postgres_data`.
- **Environment isolation:** Production secrets excluded from image via `.dockerignore`; runtime config safely injected from `.env.example`.

---

## 🧪 Running Unit Tests

The test suite validates Python CLI, ML Pipeline, RAG QA System, Safe Tool-Calling Agent, and Node.js subsystems (30 tests total):

### Python Tests (Agent Tool + ML Pipeline + RAG QA System + Safe Tool-Calling Agent)
```bash
python -m unittest discover tests
```
Expected: `Ran 23 tests ... OK`

### JavaScript Tests (Node.js Modules)
```bash
npm test
```
Expected: `ℹ tests 7 | pass 7 | fail 0`

---

## 📜 HackIndia Verification Checklist

### Skill 1: Write a runnable Python tool
- [x] **Public repository:** Publicly accessible on GitHub.
- [x] **Commits by `@adarsh-pandey-cse`:** Authored by Adarsh Pandey (`adarshpandey.cse@gmail.com`).
- [x] **Runnable Python script:** `main.py` is fully executable with `--help` and CLI flags.
- [x] **Clear setup steps:** Step-by-step virtualenv, pip install, and execution documented.
- [x] **`requirements.txt`:** Pinned runtime dependencies included.
- [x] **Sample input:** Provided in `data/sample_input.json` and `data/sample_input.csv`.
- [x] **Proof script reads data:** File ingestion logic in `agent.py`.
- [x] **Proof script calls API or mock API:** `api_client.py` makes live HTTP requests with mock fallback.
- [x] **Proof script writes useful output:** Outputs saved to `output/agent_results.json` and `output/agent_summary.md`.
- [x] **Jupyter Notebook included:** [`walkthrough.ipynb`](walkthrough.ipynb) with executed cell outputs.

### Skill 2: Ship your first ML repo
- [x] **Public repository:** Fork and standalone repositories publicly available.
- [x] **Commits by `@adarsh-pandey-cse`:** Verified git author email `adarshpandey.cse@gmail.com`.
- [x] **Scikit-learn model trained & evaluated:** `train_ml_model.py` trains and evaluates with `scikit-learn`.
- [x] **Dataset source:** Documented in `README.md` and saved as `data/agent_workload_dataset.csv`.
- [x] **Train / test split:** Explicit 80/20 stratified split using `train_test_split(..., test_size=0.2)`.
- [x] **Model choice:** Random Forest, Decision Tree, and Logistic Regression compared; Logistic Regression champion.
- [x] **Evaluation results:** Accuracy (96.25%), F1-Score (0.9771), Precision (0.9697), Recall (0.9846), Confusion Matrix.
- [x] **Clear run steps:** Documented step-by-step run command `python train_ml_model.py`.
- [x] **Jupyter notebook or dependencies in `requirements.txt`:** `scikit-learn>=1.4.0` in `requirements.txt` AND full [`ml_training_walkthrough.ipynb`](ml_training_walkthrough.ipynb) notebook included.

### Skill 3: Ship faster with Claude Code
- [x] **Public repository:** Publicly accessible on GitHub.
- [x] **Commits by `@adarsh-pandey-cse`:** All commits authored by Adarsh Pandey (`adarshpandey.cse@gmail.com`).
- [x] **Claude Code context file (`CLAUDE.md`):** Complete project context, tech stack, commands, conventions, and review checklist.
- [x] **`@AGENTS.md` imported:** `CLAUDE.md` imports `@AGENTS.md` for shared agent operating rules.
- [x] **Safe shared settings (`.claude/settings.json`):** Denies read permissions to `.env` and `.env.*`.
- [x] **`.gitignore` protection:** Excludes `.env`, `.env.*`, and `.claude/settings.local.json`.
- [x] **Multi-agent rules (`.cursorrules`):** Pair programming guidelines included.
- [x] **Reviewed code changes:** Clean commit log and active Pull Request [#1](https://github.com/HackIndiaXYZ/hackindia-ai-agents-hackathon-agentverse-2026-adarsh-pandeys-team/pull/1) on HackIndiaXYZ.

### Skill 4: Design a usable hackathon app
- [x] **Public repository:** Publicly accessible on GitHub.
- [x] **Commits by `@adarsh-pandey-cse`:** Authored and committed by Adarsh Pandey.
- [x] **At least 3 working screens or flows:** Control Dashboard, Task Explorer (Empty State), and Diagnostics (Error State).
- [x] **Clear visual hierarchy:** Primary actions, headings, and metrics visually prioritized.
- [x] **Standardized spacing:** 8px grid spacing scale consistently applied.
- [x] **Readable type & WCAG AAA contrast:** 15px/16px body, high contrast colors.
- [x] **Empty state with recovery action:** No results screen provides explanatory copy and reset button.
- [x] **Error state with understandable copy:** Form error gives actionable guidance and repair options.
- [x] **`docs/screens/` folder with screenshots:** `home.png`, `search-empty.png`, `report-error.png`.
- [x] **`## Interface design proof` in README:** Matches HackIndia template and requirements.

### Skill 5: Write JavaScript without guessing
- [x] **Public repository:** Publicly accessible on GitHub.
- [x] **Commits by `@adarsh-pandey-cse`:** Authored and committed by Adarsh Pandey.
- [x] **Modules in `src/` & `web/js/`:** Split across `data.js`, `api.js`, `render.js`, `main.js`, `agent_cli.js`.
- [x] **Functions with single responsibility:** Pure data operations, rendering, and API queries separated.
- [x] **Arrays and objects:** Task records represented as objects in arrays, updated by unique `id`.
- [x] **`fetch` and `async/await`:** Asynchronous data fetching with `response.ok` checks and fallback resilience.
- [x] **Clear README run steps:** Step-by-step browser, CLI, and test execution documented.
- [x] **Automated test suite (`tests/test_agent.js`):** 7/7 unit tests passing on Node.js (`npm test`).

### Skill 6: Build a grounded document QA app
- [x] **Public repository:** Publicly accessible on GitHub.
- [x] **Commits by `@adarsh-pandey-cse`:** Authored and committed by Adarsh Pandey.
- [x] **Dependency on `chromadb` (or similar):** Listed in `requirements.txt`.
- [x] **Document ingestion pipeline (`ingest.py`):** Parses text into structured chunks with `chunk_id`, `source`, `page`, and word count metadata.
- [x] **Sample documents in `data/sample_docs/`:** `college_faq.txt` and `refund_policy.txt` included.
- [x] **Example questions & cited answers:** Documented in `examples/questions.json` and `examples/cited_answers.md`.
- [x] **Grounded QA application (`app.py`):** Labeled evidence prompt, inline citations `[source: <chunk_id>, page: <page>]`, broken citation detection.
- [x] **Hallucination refusal guardrail:** Returns *"I could not find this in the provided documents."* on out-of-domain queries.
- [x] **Automated grounding evaluation (`evaluate.py`):** Verifies citation validity, answer accuracy, and refusal behavior, saving results to `eval/grounding_eval.md`.
- [x] **Unit tests (`tests/test_rag.py`):** Automated tests covering ingestion, retrieval, prompt formatting, citations, and refusal (7/7 passed).

### Skill 7: Build a safe tool-calling agent
- [x] **Public repository:** Publicly accessible on GitHub.
- [x] **Commits by `@adarsh-pandey-cse`:** Authored and committed by Adarsh Pandey.
- [x] **Dependency on `langgraph` (or similar):** Listed in `requirements.txt`.
- [x] **Tool schemas:** Registered in `src/tools/schemas.py` with parameter typing and risk classifications.
- [x] **Call-result loop:** Orchestrated in `src/agent_loop.py` (`SafeToolCallingAgent`).
- [x] **Human approval gates:** Implemented for high-risk write operations (`send_registration_email`, `update_student_record`).
- [x] **Hard limits:** Guardrails enforced for `max_turns`, `max_tool_calls`, `max_seconds`, and failure stops.
- [x] **Agent vs script trade-offs note:** Documented in `README.md` and detailed in `docs/agent_vs_script.md`.
- [x] **CLI runner (`safe_agent_cli.py`):** Interactive execution with `--auto-approve`, `--reject-risky`, and `--list-tools`.
- [x] **Unit tests (`tests/test_safe_agent.py`):** 9/9 unit tests passing for schemas, loops, approvals, and limits.

### Skill 8: Report model results honestly
- [x] **Public repository:** Publicly accessible on GitHub.
- [x] **Commits by `@adarsh-pandey-cse`:** Authored and committed by Adarsh Pandey.
- [x] **Dependency on ML framework:** Pinned in `requirements.txt` (`scikit-learn>=1.4.0`) and full notebook code (`ml_training_walkthrough.ipynb`).
- [x] **Model evaluation section:** Includes Dataset, Split method, Baseline, Model result, Confusion matrix, and Limitation.
- [x] **Dataset reported honestly:** 1,200 labelled task executions in `data/agent_workload_dataset.csv`.
- [x] **Split method:** 80/20 stratified split (`random_state=42`) with held-out test set (240 samples).
- [x] **Baseline comparison:** Compares model against majority-class baseline (81.25% vs 96.25%).
- [x] **Confusion matrix:** Label order, actual vs predicted rows/columns explicitly documented.
- [x] **Key metric:** Macro F1-score (0.9771) prioritized due to class imbalance.
- [x] **Honest limitation:** Real-world network and context boundary constraints documented.

### Skill 9: Dockerize a web app
- [x] **Public repository:** Publicly accessible on GitHub.
- [x] **Commits by `@adarsh-pandey-cse`:** Authored and committed by Adarsh Pandey.
- [x] **`Dockerfile`:** Uses official `python:3.12-slim` base image, sets `WORKDIR`, leverages dependency caching, exposes port 3000, and defines startup command.
- [x] **`docker-compose.yml`:** Multi-container orchestration for `app` and `db` (Postgres) with named volume persistence.
- [x] **`.dockerignore`:** Excludes `node_modules`, virtualenvs, `.git`, cache files, and private secrets.
- [x] **Port isolation:** Exposes web application port (`3000`), keeping the database secure inside internal network.
- [x] **Health check:** Verified `/health` endpoint returning `{"status":"ok"}`.
- [x] **Setup instructions in README:** Explicit 4-step setup (`clone`, `cp .env.example .env`, `docker compose up --build`, access URL).

---

## 📄 License

This project is open-source under the [MIT License](LICENSE).
