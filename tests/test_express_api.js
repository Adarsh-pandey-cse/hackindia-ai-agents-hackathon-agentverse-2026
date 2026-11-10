/**
 * Express 5 REST API Automated Test Suite
 * Tests routes, middleware, validation, error handling, and status codes.
 * Node.js 24 LTS native test runner: node --test tests/test_express_api.js
 */
import { test, describe, before, after } from 'node:test';
import assert from 'node:assert/strict';
import { createApp } from '../server/app.js';

describe('Express 5 REST API Test Suite', () => {
  let server;
  let baseUrl;
  const app = createApp();

  before(async () => {
    // Start temporary test server on random available port
    await new Promise((resolve) => {
      server = app.listen(0, () => {
        const port = server.address().port;
        baseUrl = `http://127.0.0.1:${port}`;
        resolve();
      });
    });
  });

  after(async () => {
    await new Promise((resolve) => server.close(resolve));
  });

  // 1. Health and Discovery
  test('GET /health returns 200 OK with server telemetry', async () => {
    const res = await fetch(`${baseUrl}/health`);
    assert.equal(res.status, 200);
    const body = await res.json();
    assert.equal(body.status, 'ok');
    assert.equal(body.service, 'agentverse-express-api');
    assert.ok(body.uptime >= 0);
    assert.ok(body.timestamp);
    assert.ok(body.nodeVersion);
  });

  test('GET / returns 200 OK with route discovery map', async () => {
    const res = await fetch(`${baseUrl}/`);
    assert.equal(res.status, 200);
    const body = await res.json();
    assert.ok(body.endpoints);
    assert.ok(body.endpoints.tasks);
  });

  // 2. Query Parameters and Filtering
  test('GET /api/v1/tasks returns 200 with task list and pagination', async () => {
    const res = await fetch(`${baseUrl}/api/v1/tasks`);
    assert.equal(res.status, 200);
    const body = await res.json();
    assert.equal(body.success, true);
    assert.ok(Array.isArray(body.data));
    assert.ok(body.data.length >= 3);
    assert.ok(body.pagination.total >= 3);
    assert.equal(body.pagination.page, 1);
  });

  test('GET /api/v1/tasks?priority=HIGH filters tasks by priority', async () => {
    const res = await fetch(`${baseUrl}/api/v1/tasks?priority=HIGH`);
    assert.equal(res.status, 200);
    const body = await res.json();
    assert.equal(body.success, true);
    for (const t of body.data) {
      assert.equal(t.priority, 'HIGH');
    }
  });

  test('GET /api/v1/tasks?priority=INVALID returns 400 Bad Request with validation details', async () => {
    const res = await fetch(`${baseUrl}/api/v1/tasks?priority=INVALID`);
    assert.equal(res.status, 400);
    const body = await res.json();
    assert.equal(body.success, false);
    assert.equal(body.error.code, 'BAD_REQUEST');
    assert.ok(body.error.details);
    assert.ok(body.error.details.some(d => d.field === 'priority'));
  });

  // 3. Single Resource Retrieval
  test('GET /api/v1/tasks/:id returns 200 for existing task', async () => {
    const res = await fetch(`${baseUrl}/api/v1/tasks/TASK-001`);
    assert.equal(res.status, 200);
    const body = await res.json();
    assert.equal(body.success, true);
    assert.equal(body.data.id, 'TASK-001');
    assert.equal(body.data.priority, 'HIGH');
  });

  test('GET /api/v1/tasks/:id returns 404 Not Found for non-existent task', async () => {
    const res = await fetch(`${baseUrl}/api/v1/tasks/TASK-999-DOES-NOT-EXIST`);
    assert.equal(res.status, 404);
    const body = await res.json();
    assert.equal(body.success, false);
    assert.equal(body.error.code, 'NOT_FOUND');
  });

  // 4. Request Body Handling & Status Codes
  test('POST /api/v1/tasks creates a new task and returns 201 Created', async () => {
    const newTask = {
      id: 'TASK-TEST-99',
      topic: 'Recruiter-Ready Express 5 Architecture Verification',
      category: 'cloud_engineering',
      priority: 'HIGH'
    };
    const res = await fetch(`${baseUrl}/api/v1/tasks`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(newTask)
    });
    assert.equal(res.status, 201);
    const body = await res.json();
    assert.equal(body.success, true);
    assert.equal(body.data.id, 'TASK-TEST-99');
    assert.equal(body.data.status, 'PENDING');
  });

  test('POST /api/v1/tasks with missing fields returns 400 Bad Request', async () => {
    const invalidTask = { topic: '' }; // missing category and priority
    const res = await fetch(`${baseUrl}/api/v1/tasks`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(invalidTask)
    });
    assert.equal(res.status, 400);
    const body = await res.json();
    assert.equal(body.success, false);
    assert.equal(body.error.code, 'BAD_REQUEST');
    assert.ok(body.error.details.length >= 2);
  });

  test('PUT /api/v1/tasks/:id updates an existing task and returns 200 OK', async () => {
    const update = { topic: 'Updated Autonomous AI Agents in 2026', status: 'IN_PROGRESS' };
    const res = await fetch(`${baseUrl}/api/v1/tasks/TASK-001`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(update)
    });
    assert.equal(res.status, 200);
    const body = await res.json();
    assert.equal(body.success, true);
    assert.equal(body.data.topic, update.topic);
    assert.equal(body.data.status, 'IN_PROGRESS');
  });

  test('DELETE /api/v1/tasks/:id removes task and returns 204 No Content', async () => {
    const res = await fetch(`${baseUrl}/api/v1/tasks/TASK-004`, {
      method: 'DELETE'
    });
    assert.equal(res.status, 204);

    // Verify deletion
    const verifyRes = await fetch(`${baseUrl}/api/v1/tasks/TASK-004`);
    assert.equal(verifyRes.status, 404);
  });

  // 5. Agent Route Execution
  test('POST /api/v1/agent/run executes workload and returns 200 OK', async () => {
    const res = await fetch(`${baseUrl}/api/v1/agent/run`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        topic: 'Autonomous Multi-Agent Task Orchestration',
        category: 'ai_tech_trends',
        priority: 'HIGH'
      })
    });
    assert.equal(res.status, 200);
    const body = await res.json();
    assert.equal(body.success, true);
    assert.equal(body.data.status, 'COMPLETED');
    assert.ok(body.data.findings.length > 0);
  });

  // 6. Centralized Error Handling & 404
  test('Non-existent route returns 404 through centralized error handler', async () => {
    const res = await fetch(`${baseUrl}/api/v1/unmapped-endpoint`);
    assert.equal(res.status, 404);
    const body = await res.json();
    assert.equal(body.success, false);
    assert.equal(body.error.code, 'NOT_FOUND');
    assert.equal(body.error.status, 404);
  });
});