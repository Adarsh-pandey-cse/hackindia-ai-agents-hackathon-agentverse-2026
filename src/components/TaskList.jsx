import React from 'react';
import TaskCard from './TaskCard.jsx';

/**
 * TaskList Component
 * Demonstrates stable list keys (using task.id rather than fragile array indices)
 * and empty state handling.
 */
export function TaskList({ tasks, onStatusToggle, onDelete, onResetFilter }) {
  if (tasks.length === 0) {
    return (
      <div
        className="card"
        style={{
          background: '#1e293b',
          border: '1px dashed #475569',
          borderRadius: '8px',
          padding: '3rem 1.5rem',
          textAlign: 'center',
          marginTop: '1rem',
        }}
      >
        <div style={{ fontSize: '2rem', marginBottom: '0.5rem' }}>🔍</div>
        <h3 style={{ fontSize: '1.2rem', fontWeight: 700, color: '#f8fafc', marginBottom: '0.5rem' }}>
          No Matching Workloads Found
        </h3>
        <p style={{ color: '#94a3b8', fontSize: '0.9rem', maxWidth: '400px', margin: '0 auto 1.25rem auto' }}>
          No agent tasks match your active search or priority filters. Try clearing your search or reset the filters.
        </p>
        <button
          type="button"
          onClick={onResetFilter}
          style={{
            background: '#f97316',
            color: 'white',
            border: 'none',
            padding: '0.5rem 1rem',
            borderRadius: '6px',
            fontWeight: 600,
            cursor: 'pointer',
          }}
        >
          Reset All Filters
        </button>
      </div>
    );
  }

  return (
    <div className="task-list" style={{ marginTop: '1rem' }}>
      {/* Stable list keys: Always use task.id rather than index to preserve DOM stability */}
      {tasks.map((task) => (
        <TaskCard
          key={task.id}
          task={task}
          onStatusToggle={onStatusToggle}
          onDelete={onDelete}
        />
      ))}
    </div>
  );
}

export default TaskList;
