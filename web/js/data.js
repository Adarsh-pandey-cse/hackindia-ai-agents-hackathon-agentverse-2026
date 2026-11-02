/**
 * data.js - Data models & immutable array operations.
 * Written following HackIndia "Write JavaScript without guessing" lessons 2, 3, and 5.
 */

/**
 * Normalizes input dataset into standard TaskItem array.
 * Handles both flat arrays and HackIndia nested { query_tasks: [...] } structures.
 * @param {any} raw - Parsed JSON content.
 * @returns {Array<object>} Array of standardized task items.
 */
export function normalizeTasks(raw) {
  if (Array.isArray(raw)) {
    return raw.map(t => ({
      id: t.id || t.task_id || "TASK-UNKNOWN",
      category: t.category || "general",
      topic: t.topic || t.target_topic || "",
      priority: (t.priority || "LOW").toUpperCase()
    }));
  }

  if (raw && typeof raw === "object" && Array.isArray(raw.query_tasks)) {
    return raw.query_tasks.map(t => ({
      id: t.task_id || t.id || "TASK-UNKNOWN",
      category: t.category || "general",
      topic: t.target_topic || t.topic || "",
      priority: (t.priority || "LOW").toUpperCase()
    }));
  }

  return [];
}

/**
 * Validates a task object to ensure required properties are present.
 * Avoids falsy pitfalls by checking explicitly for null and undefined.
 * @param {object} task - Task item candidate.
 * @returns {{ valid: boolean, errors: string[] }}
 */
export function validateTask(task) {
  const errors = [];

  if (task === null || task === undefined || typeof task !== "object") {
    return { valid: false, errors: ["Task must be a non-null object."] };
  }

  // Check required string properties
  const requiredProps = ["id", "category", "topic", "priority"];
  for (const prop of requiredProps) {
    const val = task[prop];
    if (val === null || val === undefined || (typeof val === "string" && val.trim() === "")) {
      errors.push(`Field '${prop}' is missing or empty.`);
    }
  }

  // Validate allowed priorities
  const allowedPriorities = ["HIGH", "MEDIUM", "LOW"];
  if (task.priority && !allowedPriorities.includes(task.priority.toUpperCase())) {
    errors.push(`Priority '${task.priority}' is invalid. Allowed: ${allowedPriorities.join(", ")}.`);
  }

  return {
    valid: errors.length === 0,
    errors
  };
}

/**
 * Filter tasks by search keyword and priority.
 * Uses Array.prototype.filter without mutating the original array.
 * @param {Array<object>} tasks - List of task objects.
 * @param {object} options - Filtering options.
 * @param {string} [options.query] - Text search query.
 * @param {string} [options.priority] - Priority filter (ALL, HIGH, MEDIUM, LOW).
 * @returns {Array<object>} Filtered task list.
 */
export function filterTasks(tasks, { query = "", priority = "ALL" } = {}) {
  if (!Array.isArray(tasks)) return [];

  const normalizedQuery = (query || "").trim().toLowerCase();
  const normalizedPriority = (priority || "ALL").toUpperCase();

  return tasks.filter(task => {
    // Check priority match
    const matchesPriority = normalizedPriority === "ALL" || (task.priority || "").toUpperCase() === normalizedPriority;

    // Check query match across topic, category, and id
    const topic = (task.topic || "").toLowerCase();
    const category = (task.category || "").toLowerCase();
    const id = (task.id || "").toLowerCase();
    const matchesQuery = normalizedQuery === "" ||
      topic.includes(normalizedQuery) ||
      category.includes(normalizedQuery) ||
      id.includes(normalizedQuery);

    return matchesPriority && matchesQuery;
  });
}

/**
 * Extracts display labels using Array.prototype.map.
 * @param {Array<object>} tasks - List of task objects.
 * @returns {Array<string>} Formatted labels.
 */
export function mapTaskLabels(tasks) {
  if (!Array.isArray(tasks)) return [];
  return tasks.map(task => `[${task.id}] ${task.topic} (${task.priority})`);
}

/**
 * Sorts tasks by priority weight (HIGH > MEDIUM > LOW).
 * Makes a shallow copy first to keep original order safe.
 * @param {Array<object>} tasks - List of task objects.
 * @returns {Array<object>} New sorted array.
 */
export function sortTasksByPriority(tasks) {
  if (!Array.isArray(tasks)) return [];

  const priorityWeight = { HIGH: 3, MEDIUM: 2, LOW: 1 };

  // Copy first, then sort (Lesson 5)
  return [...tasks].sort((a, b) => {
    const weightA = priorityWeight[(a.priority || "").toUpperCase()] || 0;
    const weightB = priorityWeight[(b.priority || "").toUpperCase()] || 0;
    return weightB - weightA;
  });
}

/**
 * Updates a task by its unique ID instead of array index (Lesson 3).
 * @param {Array<object>} tasks - Existing task array.
 * @param {string} taskId - Target ID.
 * @param {object} updates - Attributes to update.
 * @returns {Array<object>} New array with updated item.
 */
export function updateTaskById(tasks, taskId, updates) {
  if (!Array.isArray(tasks)) return [];
  return tasks.map(task => {
    if (task.id === taskId) {
      return { ...task, ...updates };
    }
    return task;
  });
}
