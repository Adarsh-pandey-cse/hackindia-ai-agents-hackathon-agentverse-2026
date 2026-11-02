/**
 * main.js - Browser Application Entry Point (ES Module).
 * Written following HackIndia "Write JavaScript without guessing" Lessons 7 & 8.
 */
import { validateTask, filterTasks, sortTasksByPriority, updateTaskById } from "./data.js";
import { fetchTasks, queryExternalApi, DEFAULT_TASKS } from "./api.js";
import { renderTaskRows, renderEmptyState, hideEmptyState, renderErrorState } from "./render.js";

// Application State
let allTasks = [...DEFAULT_TASKS];
let activePriority = "ALL";
let activeSearchQuery = "";

/**
 * Initializes the application on DOM ready.
 */
async function initApp() {
  console.log("[AgentVerse] Initializing JavaScript Application Modules...");

  // Load initial tasks asynchronously
  try {
    const loaded = await fetchTasks("data/sample_input.json");
    if (Array.isArray(loaded) && loaded.length > 0) {
      allTasks = [...loaded];
    }
  } catch (err) {
    console.warn("[AgentVerse] Falling back to default task set:", err);
  }

  // Setup UI elements
  setupTabNavigation();
  setupFilterControls();
  setupDiagnosticForm();

  // Initial render
  refreshTaskView();
}

/**
 * Configures Tab switching logic.
 */
function setupTabNavigation() {
  const tabs = ["dashboard", "tasks", "diagnostics"];
  tabs.forEach(tabId => {
    const btn = document.getElementById(`tab-${tabId}`);
    if (btn) {
      btn.addEventListener("click", () => switchTab(tabId));
    }
  });
}

/**
 * Switches the active screen view.
 * @param {string} tabId - Target tab name.
 */
export function switchTab(tabId) {
  document.querySelectorAll(".tab-btn").forEach(btn => btn.classList.remove("active"));
  document.querySelectorAll(".screen-view").forEach(view => view.classList.remove("active"));

  const targetBtn = document.getElementById(`tab-${tabId}`);
  const targetView = document.getElementById(`view-${tabId}`);

  if (targetBtn) targetBtn.classList.add("active");
  if (targetView) targetView.classList.add("active");
}

/**
 * Registers real-time search & filter event listeners.
 */
function setupFilterControls() {
  const searchInput = document.getElementById("task-search");
  const prioritySelect = document.getElementById("priority-filter");
  const emptySimBtn = document.getElementById("btn-sim-empty");
  const resetBtn = document.getElementById("btn-reset-filters");

  if (searchInput) {
    searchInput.addEventListener("input", (e) => {
      activeSearchQuery = e.target.value;
      refreshTaskView();
    });
  }

  if (prioritySelect) {
    prioritySelect.addEventListener("change", (e) => {
      activePriority = e.target.value;
      refreshTaskView();
    });
  }

  if (emptySimBtn) {
    emptySimBtn.addEventListener("click", () => {
      if (searchInput) searchInput.value = "non-existent-quantum-algo";
      activeSearchQuery = "non-existent-quantum-algo";
      refreshTaskView();
    });
  }

  if (resetBtn) {
    resetBtn.addEventListener("click", () => {
      if (searchInput) searchInput.value = "";
      if (prioritySelect) prioritySelect.value = "ALL";
      activeSearchQuery = "";
      activePriority = "ALL";
      refreshTaskView();
    });
  }
}

/**
 * Updates the filtered task list and renders either the table or empty state.
 */
function refreshTaskView() {
  const tbody = document.getElementById("task-tbody");
  const emptyCard = document.getElementById("empty-state-card");
  const taskList = document.getElementById("task-list");

  // Filter tasks without mutating original state
  const filtered = filterTasks(allTasks, { query: activeSearchQuery, priority: activePriority });

  if (filtered.length === 0) {
    renderEmptyState(emptyCard, taskList, activeSearchQuery);
  } else {
    hideEmptyState(emptyCard, taskList);
    renderTaskRows(filtered, tbody);
  }
}

/**
 * Configures the manual verification & error handling form.
 */
function setupDiagnosticForm() {
  const errorBox = document.getElementById("error-notification");
  const topicInput = document.getElementById("task-topic-input");
  const btnValidate = document.getElementById("btn-validate-task");
  const btnSimError = document.getElementById("btn-sim-error");
  const btnLoadSample = document.getElementById("btn-load-sample");

  if (btnValidate) {
    btnValidate.addEventListener("click", () => {
      const candidate = {
        id: "TASK-TEST-01",
        category: document.getElementById("task-category")?.value || "ai_tech_trends",
        topic: topicInput?.value || "",
        priority: "HIGH"
      };

      const result = validateTask(candidate);
      if (!result.valid) {
        renderErrorState(errorBox, "Validation Error: Missing Required Field", result.errors);
      } else {
        if (errorBox) errorBox.style.display = "none";
        alert(`Validation passed for '${candidate.topic}'! All 4 required fields present.`);
      }
    });
  }

  if (btnSimError) {
    btnSimError.addEventListener("click", () => {
      if (topicInput) topicInput.value = "";
      const invalidCandidate = { id: "TASK-ERR", category: "ai_tech_trends", topic: "", priority: "HIGH" };
      const result = validateTask(invalidCandidate);
      renderErrorState(errorBox, "Validation Error: Missing Required Field 'topic'", result.errors);
    });
  }

  if (btnLoadSample) {
    btnLoadSample.addEventListener("click", () => {
      if (topicInput) topicInput.value = "Autonomous AI Agents in 2026";
      if (errorBox) errorBox.style.display = "none";
      alert("Valid sample loaded! Error state cleared.");
    });
  }
}

// Global inspect hook
window.inspectTask = function(taskId) {
  const task = allTasks.find(t => t.id === taskId);
  if (task) {
    alert(`[Task Inspector]\nID: ${task.id}\nTopic: ${task.topic}\nCategory: ${task.category}\nPriority: ${task.priority}`);
  }
};

// Bootstrap on DOMContentLoaded
if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", initApp);
} else {
  initApp();
}
