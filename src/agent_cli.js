#!/usr/bin/env node
/**
 * agent_cli.js - Runnable Node.js CLI Intelligence Agent.
 * Written following HackIndia "Write JavaScript without guessing" Lessons 6 & 8.
 */
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { validateTask, filterTasks, sortTasksByPriority, mapTaskLabels, normalizeTasks } from "./data.js";
import { queryExternalApi, DEFAULT_TASKS } from "./api.js";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT_DIR = path.resolve(__dirname, "..");

async function runCli() {
  console.log("=".repeat(72));
  console.log("  AgentVerse Autonomous AI Agent (Node.js Engine)");
  console.log("  Skill: Write JavaScript without guessing (HackIndia 2026)");
  console.log("  Developer: Adarsh Pandey (@adarsh-pandey-cse)");
  console.log("=".repeat(72));

  const inputPath = path.join(ROOT_DIR, "data", "sample_input.json");
  let rawTasks = [];

  try {
    const fileContent = await fs.readFile(inputPath, "utf-8");
    const parsed = JSON.parse(fileContent);
    rawTasks = normalizeTasks(parsed);
    console.log(`[INFO] Loaded ${rawTasks.length} tasks from ${path.relative(ROOT_DIR, inputPath)}`);
  } catch (err) {
    console.warn(`[WARN] Could not read ${inputPath} (${err.message}). Using default tasks.`);
    rawTasks = [...DEFAULT_TASKS];
  }

  // 1. Data Validation (Lesson 2 & 3)
  console.log("\n[STEP 1/3] Validating task inputs...");
  const validTasks = [];
  for (const t of rawTasks) {
    const check = validateTask(t);
    if (check.valid) {
      validTasks.push(t);
    } else {
      console.warn(`  [!] Skipping invalid task '${t.id || "UNKNOWN"}': ${check.errors.join(", ")}`);
    }
  }
  console.log(`[+] Successfully validated ${validTasks.length} structured task items.`);

  // 2. Data Transformation & Sorting (Lesson 5)
  console.log("\n[STEP 2/3] Sorting tasks by priority (HIGH > MEDIUM > LOW)...");
  const sortedTasks = sortTasksByPriority(validTasks);
  const labels = mapTaskLabels(sortedTasks);
  labels.forEach(l => console.log(`  - ${l}`));

  // 3. Asynchronous API Execution (Lesson 6)
  console.log("\n[STEP 3/3] Calling external REST endpoints (async/await & mock fallbacks)...");
  const results = [];
  for (const task of sortedTasks) {
    const res = await queryExternalApi(task.category, task.topic);
    results.push({
      id: task.id,
      topic: task.topic,
      source: res.source,
      latencyMs: res.latencyMs,
      success: res.success
    });
    console.log(`  [+] ${task.id} | ${task.topic.padEnd(42)} | ${res.latencyMs}ms [${res.success ? "success" : "mock_fallback"}]`);
  }

  console.log("\n" + "=".repeat(72));
  console.log("  JAVASCRIPT AGENT EXECUTION COMPLETED SUCCESSFULLY (EXIT CODE 0)");
  console.log("=".repeat(72));
  return 0;
}

runCli().then(code => {
  process.exitCode = code || 0;
}).catch(err => {
  console.error("[FATAL ERROR]:", err);
  process.exitCode = 1;
});
