import React from 'react';

/**
 * TaskFilter Component
 * Controlled form inputs demonstrating lifted state.
 * All state lives in parent App.jsx and updates via callbacks.
 */
export function TaskFilter({ searchQuery, onSearchChange, priorityFilter, onPriorityChange }) {
  return (
    <div
      style={{
        display: 'flex',
        flexWrap: 'wrap',
        gap: '0.75rem',
        marginBottom: '1rem',
        alignItems: 'center',
        justifyContent: 'space-between',
      }}
    >
      <div style={{ flex: '1 1 260px' }}>
        <input
          type="text"
          value={searchQuery}
          onChange={(e) => onSearchChange(e.target.value)}
          placeholder="Search agent tasks by topic, category, or ID..."
          style={{
            width: '100%',
            padding: '0.65rem 1rem',
            borderRadius: '6px',
            border: '1px solid #334155',
            background: '#1e293b',
            color: '#f8fafc',
            fontSize: '0.9rem',
          }}
        />
      </div>

      <div style={{ display: 'flex', gap: '0.5rem', alignItems: 'center' }}>
        <label htmlFor="priority-filter" style={{ fontSize: '0.85rem', color: '#94a3b8' }}>
          Priority:
        </label>
        <select
          id="priority-filter"
          value={priorityFilter}
          onChange={(e) => onPriorityChange(e.target.value)}
          style={{
            padding: '0.65rem 1rem',
            borderRadius: '6px',
            border: '1px solid #334155',
            background: '#1e293b',
            color: '#f8fafc',
            fontSize: '0.9rem',
            cursor: 'pointer',
          }}
        >
          <option value="ALL">All Priorities</option>
          <option value="HIGH">High</option>
          <option value="MEDIUM">Medium</option>
          <option value="LOW">Low</option>
        </select>
      </div>
    </div>
  );
}

export default TaskFilter;
