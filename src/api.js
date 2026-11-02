/**
 * api.js - Network requests & asynchronous data fetching.
 * Written following HackIndia "Write JavaScript without guessing" Lesson 6.
 */

import { normalizeTasks } from "./data.js";

// Fallback dataset used when offline or network fails
export const DEFAULT_TASKS = [
  {
    id: "TASK-001",
    category: "ai_tech_trends",
    topic: "Autonomous AI Agents in 2026",
    priority: "HIGH"
  },
  {
    id: "TASK-002",
    category: "market_indicators",
    topic: "Cryptocurrency and Web3 Ecosystem Metrics",
    priority: "MEDIUM"
  },
  {
    id: "TASK-003",
    category: "developer_ecosystem",
    topic: "Open Source AI Tools & Frameworks",
    priority: "HIGH"
  }
];

/**
 * Loads tasks asynchronously from a JSON endpoint or local file.
 * Always checks response.ok before parsing JSON.
 * @param {string} url - Target URL or path.
 * @returns {Promise<Array<object>>}
 */
export async function fetchTasks(url = "data/sample_input.json") {
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`HTTP error ${response.status}: Failed to fetch tasks from ${url}`);
    }
    const data = await response.json();
    const tasks = normalizeTasks(data);
    return tasks.length > 0 ? tasks : DEFAULT_TASKS;
  } catch (error) {
    // Return fallback tasks so app remains usable offline
    console.warn(`[AgentVerse.API] Fetch failed (${error.message}). Using local fallback tasks.`);
    return DEFAULT_TASKS;
  }
}

/**
 * Dispatches a simulated or live analytical query to an external REST endpoint.
 * Demonstrates async/await, response.ok verification, and try/catch error handling.
 * @param {string} category - Task category.
 * @param {string} topic - Search prompt or topic.
 * @returns {Promise<{ success: boolean, source: string, latencyMs: number, data: object }>}
 */
export async function queryExternalApi(category, topic) {
  const startTime = Date.now();

  let timeoutId;
  try {
    // Route to appropriate public API
    let endpoint = "https://httpbin.org/anything";
    if (category === "market_indicators") {
      endpoint = "https://api.coingecko.com/api/v3/ping";
    }

    const controller = new AbortController();
    timeoutId = setTimeout(() => controller.abort(), 2500); // 2.5s timeout

    const response = await fetch(endpoint, {
      signal: controller.signal,
      headers: { "Accept": "application/json" }
    });

    // Lesson 6: Always check response.ok before reading body
    if (!response.ok) {
      throw new Error(`API responded with status code ${response.status}`);
    }

    const json = await response.json();
    const latencyMs = Date.now() - startTime;

    return {
      success: true,
      source: endpoint,
      latencyMs,
      data: json
    };
  } catch (error) {
    const latencyMs = Date.now() - startTime;
    return {
      success: false,
      source: "Offline Mock Fallback Engine",
      latencyMs: Math.max(10, latencyMs),
      error: error.message,
      data: {
        category,
        topic,
        status: "simulated_success",
        note: "Fallback triggered cleanly without guessing."
      }
    };
  } finally {
    if (timeoutId) {
      clearTimeout(timeoutId);
    }
  }
}
