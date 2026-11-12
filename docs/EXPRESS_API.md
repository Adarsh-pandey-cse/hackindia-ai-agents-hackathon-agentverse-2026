# Recruiter-Ready Express 5 REST API

**HackIndia Skill:** [Build a Recruiter-Ready Express API](https://hackindia.org/skills/build-a-recruiter-ready-express-api)  
**Runtime:** Node.js 24 LTS (`v24.14.1`)  
**Framework:** Express 5 (`^5.0.0`)  
**Repository:** [https://github.com/HackIndiaXYZ/hackindia-ai-agents-hackathon-agentverse-2026-adarsh-pandeys-team](https://github.com/HackIndiaXYZ/hackindia-ai-agents-hackathon-agentverse-2026-adarsh-pandeys-team)  
**Developer:** Adarsh Pandey ([@adarsh-pandey-cse](https://github.com/adarsh-pandey-cse))

---

## 🏛️ Project Architecture & Clean Structure

The API adheres to a modular, layer-separated structure designed for enterprise maintainability and recruiter code reviews:

```
server/
  ├── config/
  │     └── env.js            # Typed environment configuration with fallbacks
  ├── middleware/
  │     ├── logger.js         # Request latency & telemetry logger
  │     ├── validate.js       # Express query & body validation middleware
  │     └── auth.js           # API Key authentication header handler
  ├── routes/
  │     ├── health.js         # Diagnostic & discovery routes (GET /health, GET /)
  │     ├── tasks.js          # RESTful CRUD & query filters (GET, POST, PUT, DELETE)
  │     └── agent.js          # AI Agent execution endpoint (POST /api/v1/agent/run)
  ├── errors/
  │     └── errorHandler.js   # Centralized 4-argument error handler & ApiError class
  ├── app.js                  # Express app factory (middleware, router mount, 404)
  └── index.js                # Server entry point & graceful shutdown listeners
```

---

## 📋 API Route Specifications & Status Codes

All responses follow a consistent, predictable JSON envelope.

### 1. Health & Discovery Endpoints

| Method | Endpoint | Status Code | Description |
|:---|:---|:---:|:---|
| `GET` | `/health` | `200 OK` | Uptime telemetry, node version, service state |
| `GET` | `/` | `200 OK` | API index with route discovery map |

#### `GET /health` Response Example:
```json
{
  "status": "ok",
  "uptime": 128,
  "timestamp": "2026-11-11T00:30:00.000Z",
  "service": "agentverse-express-api",
  "version": "1.0.0",
  "environment": "development",
  "nodeVersion": "v24.14.1"
}
```

---

### 2. Task Resource Management Endpoints

| Method | Endpoint | Status Code | Description |
|:---|:---|:---:|:---|
| `GET` | `/api/v1/tasks` | `200 OK` | Query tasks with `priority`, `search`, `limit`, `page` |
| `GET` | `/api/v1/tasks/:id` | `200 OK` / `404 Not Found` | Retrieve single task record by unique ID |
| `POST` | `/api/v1/tasks` | `201 Created` / `400 Bad Request` | Create task with validated payload |
| `PUT` | `/api/v1/tasks/:id` | `200 OK` / `404 Not Found` | Update task properties |
| `DELETE` | `/api/v1/tasks/:id` | `204 No Content` / `404 Not Found` | Remove task from repository |

#### `GET /api/v1/tasks?priority=HIGH&limit=2` Example:
```json
{
  "success": true,
  "data": [
    {
      "id": "TASK-001",
      "topic": "Autonomous AI Agents in 2026",
      "category": "ai_tech_trends",
      "priority": "HIGH",
      "status": "COMPLETED"
    }
  ],
  "pagination": {
    "total": 2,
    "page": 1,
    "limit": 2,
    "totalPages": 1
  }
}
```

#### `POST /api/v1/tasks` Creation Example (`201 Created`):
```http
POST /api/v1/tasks HTTP/1.1
Content-Type: application/json

{
  "topic": "Implement Grounded QA Citations",
  "category": "rag_engineering",
  "priority": "HIGH"
}
```

---

## 🛡️ Centralized Error Handling

Centralized error handling is implemented via a canonical 4-argument Express middleware in `server/errors/errorHandler.js`:

```javascript
export function errorHandler(err, req, res, next) {
  const isApiError = err instanceof ApiError;
  const status = isApiError ? err.statusCode : (err.status || 500);
  const code = isApiError ? err.code : 'INTERNAL_SERVER_ERROR';

  res.status(status).json({
    success: false,
    error: {
      message: err.message || 'An unexpected error occurred',
      code,
      status,
      ...(err.details ? { details: err.details } : {})
    }
  });
}
```

### Error Responses Example (`400 Bad Request`):
```json
{
  "success": false,
  "error": {
    "message": "Validation failed for task payload",
    "code": "BAD_REQUEST",
    "status": 400,
    "details": [
      {
        "field": "category",
        "message": "Category is required and must be a non-empty string"
      }
    ]
  }
}
```

---

## 🔒 Environment Variable Isolation

All runtime variables are loaded through `server/config/env.js` and documented in `.env.example`:

| Variable | Default | Purpose |
|:---|:---|:---|
| `PORT` | `3000` | HTTP listener port |
| `NODE_ENV` | `development` | Environment mode (`development`, `production`, `test`) |
| `API_KEY` | `agentverse-secret-key-2026` | Admin authentication key |
| `CORS_ORIGIN` | `*` | Allowed origins for cross-origin requests |

---

## 🧪 Automated Testing & Running

### Run the Express 5 Server:
```bash
npm run api
```

### Run the Automated Test Suite (13 API Tests + 7 JS Core Tests):
```bash
npm test
```

### Run System & Express Skill Verification:
```bash
python verify_express_api.py
```


---

## 💻 Teammate Quickstart & cURL Examples

Teammates can test the API using standard `curl` commands:

### 1. Check Health Telemetry
```bash
curl -i "http://localhost:3000/health"
```

### 2. List Tasks with Pagination & Filtering
```bash
curl -i "http://localhost:3000/api/v1/tasks?page=1&limit=5&priority=HIGH"
```

### 3. Create a New Workload (201 Created)
```bash
curl -i -X POST "http://localhost:3000/api/v1/tasks" \
  -H "Content-Type: application/json" \
  -d '{"topic":"Decentralized Task Queue","priority":"HIGH","category":"ai_tech_trends"}'
```

### 4. Trigger a Structured Validation Error (400 Bad Request)
```bash
curl -i -X POST "http://localhost:3000/api/v1/tasks" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### 5. Run the Automated Smoke Test
```bash
sh scripts/smoke.sh
# Or on Windows/Python:
python scripts/smoke.py
```
