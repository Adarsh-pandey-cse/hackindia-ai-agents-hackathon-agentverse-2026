/**
 * render.js - Focused UI rendering functions.
 * Written following HackIndia "Write JavaScript without guessing" Lessons 4, 7, and UI/UX guidelines.
 */

/**
 * Escapes HTML characters to prevent XSS.
 * @param {string} str - Raw string.
 * @returns {string} Safe escaped string.
 */
function escapeHtml(str) {
  if (typeof str !== "string") return "";
  return str
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}

/**
 * Renders task rows into a table body element.
 * @param {Array<object>} tasks - Task objects to render.
 * @param {HTMLElement} tbody - Target table body container.
 */
export function renderTaskRows(tasks, tbody) {
  if (!tbody) return;

  if (!Array.isArray(tasks) || tasks.length === 0) {
    tbody.innerHTML = `<tr><td colspan="4" style="text-align: center; color: var(--text-muted); padding: 24px;">No tasks available to display.</td></tr>`;
    return;
  }

  tbody.innerHTML = tasks.map(task => {
    const priority = (task.priority || "LOW").toUpperCase();
    const pillClass = priority === "HIGH" ? "pill-high" : (priority === "MEDIUM" ? "pill-medium" : "pill-success");

    return `
      <tr data-task-id="${escapeHtml(task.id)}">
        <td><strong>${escapeHtml(task.id)}</strong></td>
        <td>${escapeHtml(task.topic)}</td>
        <td><span class="pill ${pillClass}">${escapeHtml(priority)}</span></td>
        <td>
          <button class="btn btn-secondary" style="padding: 4px 10px; font-size: 12px;" onclick="window.inspectTask('${escapeHtml(task.id)}')">
            Inspect
          </button>
        </td>
      </tr>
    `;
  }).join("");
}

/**
 * Displays or updates the empty state card.
 * @param {HTMLElement} emptyCard - Empty state container element.
 * @param {HTMLElement} taskContainer - Task list container element.
 * @param {string} query - The search query that yielded 0 results.
 */
export function renderEmptyState(emptyCard, taskContainer, query = "") {
  if (!emptyCard || !taskContainer) return;

  const queryLabel = emptyCard.querySelector("#empty-query-label");
  if (queryLabel) {
    queryLabel.textContent = query ? `"${query}"` : "selected filters";
  }

  emptyCard.style.display = "block";
  taskContainer.style.display = "none";
}

/**
 * Hides the empty state and restores the task container.
 * @param {HTMLElement} emptyCard - Empty state element.
 * @param {HTMLElement} taskContainer - Task list element.
 */
export function hideEmptyState(emptyCard, taskContainer) {
  if (emptyCard) emptyCard.style.display = "none";
  if (taskContainer) taskContainer.style.display = "block";
}

/**
 * Renders an error state banner with recovery actions.
 * @param {HTMLElement} errorBox - Error banner container element.
 * @param {string} title - Error heading.
 * @param {string|Array<string>} errors - Detailed error message(s).
 */
export function renderErrorState(errorBox, title, errors) {
  if (!errorBox) return;

  const titleEl = errorBox.querySelector(".error-title");
  const msgEl = errorBox.querySelector(".error-message");

  if (titleEl) titleEl.textContent = title;
  if (msgEl) {
    if (Array.isArray(errors)) {
      msgEl.innerHTML = errors.map(e => `• ${escapeHtml(e)}`).join("<br>");
    } else {
      msgEl.textContent = errors;
    }
  }

  errorBox.style.display = "flex";
}
