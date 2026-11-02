/**
 * test_agent.js - Automated unit tests for JavaScript modules.
 * Run with: node --test tests/test_agent.js
 */
import test from "node:test";
import assert from "node:assert/strict";
import { validateTask, filterTasks, sortTasksByPriority, updateTaskById, normalizeTasks } from "../src/data.js";
import { fetchTasks, queryExternalApi, DEFAULT_TASKS } from "../src/api.js";

test("validateTask: accepts valid task object", () => {
  const task = { id: "TASK-01", category: "ai", topic: "Agent Systems", priority: "HIGH" };
  const res = validateTask(task);
  assert.equal(res.valid, true);
  assert.equal(res.errors.length, 0);
});

test("validateTask: catches missing properties and null values", () => {
  const invalid = { id: "TASK-02", category: null, topic: "", priority: "INVALID" };
  const res = validateTask(invalid);
  assert.equal(res.valid, false);
  assert.ok(res.errors.length >= 2);
});

test("filterTasks: filters by search query and priority without mutating original", () => {
  const tasks = [
    { id: "T1", category: "finance", topic: "Crypto Trends", priority: "HIGH" },
    { id: "T2", category: "tech", topic: "Autonomous AI", priority: "MEDIUM" },
    { id: "T3", category: "tech", topic: "Open Source AI", priority: "HIGH" }
  ];
  const originalCopy = JSON.parse(JSON.stringify(tasks));

  const filtered = filterTasks(tasks, { query: "crypto", priority: "HIGH" });
  assert.equal(filtered.length, 1);
  assert.equal(filtered[0].id, "T1");

  // Verify immutability
  assert.deepEqual(tasks, originalCopy);
});

test("sortTasksByPriority: sorts high to low immutably", () => {
  const tasks = [
    { id: "T1", priority: "LOW" },
    { id: "T2", priority: "HIGH" },
    { id: "T3", priority: "MEDIUM" }
  ];

  const sorted = sortTasksByPriority(tasks);
  assert.equal(sorted[0].priority, "HIGH");
  assert.equal(sorted[1].priority, "MEDIUM");
  assert.equal(sorted[2].priority, "LOW");

  // Verify original array order was preserved (Lesson 5)
  assert.equal(tasks[0].priority, "LOW");
});

test("updateTaskById: updates by ID rather than index", () => {
  const tasks = [
    { id: "T1", topic: "Initial", priority: "LOW" },
    { id: "T2", topic: "Secondary", priority: "HIGH" }
  ];

  const updated = updateTaskById(tasks, "T1", { topic: "Updated Topic" });
  assert.equal(updated[0].topic, "Updated Topic");
  assert.equal(tasks[0].topic, "Initial"); // Immutability preserved
});

test("normalizeTasks: parses both arrays and nested query_tasks payloads", () => {
  const nested = {
    query_tasks: [
      { task_id: "N-1", category: "ai", target_topic: "Neural Nets", priority: "HIGH" }
    ]
  };
  const normalized = normalizeTasks(nested);
  assert.equal(normalized.length, 1);
  assert.equal(normalized[0].id, "N-1");
  assert.equal(normalized[0].topic, "Neural Nets");
});

test("queryExternalApi: handles network call or falls back to mock resilience", async () => {
  const result = await queryExternalApi("ai_tech_trends", "Autonomous AI Agents in 2026");
  assert.ok(typeof result.latencyMs === "number");
  assert.ok(result.latencyMs >= 0);
  assert.ok(result.data !== null && result.data !== undefined);
});
