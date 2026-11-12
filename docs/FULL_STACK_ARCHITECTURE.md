# AgentVerse Weekend Full-Stack Platform Architecture

**HackIndia AI Agents Hackathon - AgentVerse 2026**  
**Skill Track:** `ship-a-weekend-full-stack-repo`  
**Developer:** Adarsh Pandey ([@adarsh-pandey-cse](https://github.com/adarsh-pandey-cse))

---

## 1. Overview & Architectural Philosophy

AgentVerse is an end-to-end autonomous AI agent platform and analytical dashboard engineered to be **reviewer-ready, lightweight, reproducible, and navigable**. It implements a complete full-stack architecture adhering to the seven core engineering principles of the HackIndia Full-Stack Curriculum:

1. **Weekend-Sized Stack:** High-leverage, reliable technologies without bloated dependencies.
2. **Defensible State Boundary:** Rigorous separation of ephemeral UI state, lifted application state, server-side business state, and durable persistence.
3. **Internal API Integration:** Client connects directly to custom Express 5 REST API and Python analytical runtimes.
4. **Three-State Network Contract:** Explicit visual representations for **loading**, **success**, and **failure/offline resilience**.
5. **Strict Environment Parity:** Zero hardcoded secrets, complete `.env.example` reference, and runtime configuration validation.
6. **Navigable Codebase:** Predictable file structure where any judge, teammate, or recruiter can locate the UI, API, shared types, and tests in under two minutes.
7. **Verified Reproducibility:** Single-command local startup and automated verification test suites with 100% pass rates.

---

## 2. Technology Stack

| Layer | Technology | Key Capabilities |
| :--- | :--- | :--- |
| **Frontend Client** | React 18 + Vite 5 + Vanilla CSS3 | Modular components (`TaskForm`, `TaskList`, `TaskFilter`, `MetricsBar`), controlled inputs, stable keys, lifted state, dark mode dashboard. |
| **Backend REST API** | Express 5.3 + Node.js 24 LTS | Router-driven modular routes (`/health`, `/api/v1/tasks`, `/api/v1/agent/run`), CORS, JSON body parser, 4-argument centralized error handler. |
| **AI/ML Engine** | Python 3.12 + Scikit-Learn | Stratified 80/20 ML classifier (96.25% test accuracy, 0.9771 F1), Grounded Document QA RAG engine with verifiable citations. |
| **Persistence Layer** | PostgreSQL 16 + Local JSON Datastore | Multi-container Docker Compose service (`db`), structured JSON storage (`data/chunks.json`, `data/sample_input.json`), cached joblib indices. |
| **DevOps & Tooling** | Docker, Vite Dev Server Proxy, Native Test Runner | Containerized multi-stage Dockerfile, Vite `/api` reverse proxy, Node `--test`, Python `unittest`. |

---

## 3. State Hierarchy & Data Flow

```
+-----------------------------------------------------------------------------------+
|                                FRONTEND CLIENT                                    |
|                                                                                   |
|  [Ephemeral Component State]                                                      |
|   - TaskForm local useState: form input values, draft validations                 |
|   - TaskFilter local useState: search keywords, priority selection                |
|                                                                                   |
|  [Lifted Application State (src/App.jsx)]                                         |
|   - tasks: Current collection of active workloads                                 |
|   - isLoading: Visual feedback during active API handshakes                       |
|   - errorMessage / notification: Alert toasts for error or success                |
|   - dataSource: Indicates whether serving from 'Live API' or 'Offline Store'     |
+----------------------------------------+------------------------------------------+
                                         |
               fetch('/api/v1/tasks')    |  Reverse Proxy (Vite :5173 -> :3000)
               AbortController Teardown  v
+-----------------------------------------------------------------------------------+
|                             BACKEND API SERVER                                    |
|                                                                                   |
|  [Express 5 REST API (server/)]                                                   |
|   - Middleware: requestLogger, jsonParser, corsMiddleware, notFoundHandler        |
|   - Routes: /health, /api/v1/tasks (CRUD), /api/v1/agent/run (Autonomous Runner)  |
|   - Error Pipeline: Centralized 4-argument handler returning structured JSON      |
+----------------------------------------+------------------------------------------+
                                         |
                       Database Queries  v
+-----------------------------------------------------------------------------------+
|                            PERSISTENCE & RUNTIMES                                 |
|                                                                                   |
|  [PostgreSQL 16 (docker-compose.yml)]      [Analytical File Stores]              |
|   - Structured table schemas               - data/sample_input.json & .csv        |
|   - Relational workload transactions       - data/chunks.json (RAG Document Store)|
|                                            - models/*.joblib (Trained ML Models)  |
+-----------------------------------------------------------------------------------+
```

---

## 4. API Specification & Proof of Operation

The backend API is bound to port `3000` (or `PORT` environment variable) and exposes standard RESTful endpoints:

### 1. Health & Telemetry
- **Endpoint:** `GET /health`
- **Response:**
  ```json
  {
    "status": "healthy",
    "uptime": 42.15,
    "timestamp": "2026-11-12T14:30:00.000Z",
    "nodeVersion": "v24.11.0",
    "environment": "development"
  }
  ```

### 2. Task Collection Retrieval
- **Endpoint:** `GET /api/v1/tasks?priority=HIGH`
- **Response:** `200 OK`
  ```json
  {
    "status": "success",
    "data": [
      {
        "id": "TASK-001",
        "topic": "Autonomous AI Agents in 2026",
        "category": "ai_tech_trends",
        "priority": "HIGH",
        "status": "COMPLETED"
      }
    ],
    "count": 1
  }
  ```

### 3. Workload Creation
- **Endpoint:** `POST /api/v1/tasks`
- **Payload:**
  ```json
  {
    "topic": "Real-Time Vector Search Integration",
    "category": "developer_ecosystem",
    "priority": "HIGH"
  }
  ```
- **Response:** `201 Created` with created record and assigned identifier.

### 4. Autonomous Agent Execution
- **Endpoint:** `POST /api/v1/agent/run`
- **Payload:** `{"priorityFilter": "HIGH", "useMock": true}`
- **Response:** `200 OK` with execution report, ML classification scores, and task metrics.

---

## 5. Network Lifecycle: Loading, Success, and Failure Resilience

In accordance with Lesson 4:
1. **Loading State:**  
   When `fetchLiveTasks()` triggers on mount or reload, `isLoading` is set to `true`, displaying an accessible status banner (`role="status"`).
2. **Success State:**  
   When the Express server responds with `200 OK`, tasks are hydrated into state, `dataSource` displays `"Live Express 5 API"`, and a confirmation banner renders.
3. **Failure State & Offline Resilience:**  
   If the backend API is temporarily offline or unreachable, the component catches the exception, updates `errorMessage` (`role="alert"`), and seamlessly falls back to pre-seeded local task storage with `"Local Store (Offline Resilience)"`. The application never crashes or displays blank screens.

---

## 6. Environment Configuration (.env.example)

Environment variables are isolated from the codebase and documented in `.env.example`:

```ini
PORT=3000
HOST=0.0.0.0
NODE_ENV=development
VITE_API_URL=http://localhost:3000
API_KEY=agentverse_local_dev_key
DATABASE_URL=postgres://app_user:app_password@localhost:5432/app_db
RAG_DATA_DIR=data/sample_docs
RAG_CHUNKS_PATH=data/chunks.json
```

---

## 7. Automated Verification & Testing

Verify the full-stack architecture using the automated CLI verification tool or native test runners:

```bash
# 1. Full-Stack Architecture Verification Tool
python verify_full_stack_repo.py
npm run verify:fullstack

# 2. Complete Node.js Integration Suite (28+ Tests)
npm test

# 3. Python Unit Test Suite (40 Tests)
python -m unittest discover tests
```
