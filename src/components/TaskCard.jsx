import React from 'react';

/**
 * TaskCard Component
 * Pure presentation component displaying a task record.
 * Uses props for all data and callbacks.
 */
export function TaskCard({ task, onStatusToggle, onDelete }) {
  const getBadgeClass = (priority) => {
    switch (priority) {
      case 'HIGH': return 'badge-high';
      case 'MEDIUM': return 'badge-medium';
      default: return 'badge-low';
    }
  };

  const isCompleted = task.status === 'COMPLETED';

  return (
    <div
      className="card"
      style={{
        background: '#1e293b',
        border: '1px solid #334155',
        borderRadius: '8px',
        padding: '1.25rem',
        marginBottom: '0.75rem',
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        opacity: isCompleted ? 0.75 : 1,
        transition: 'all 0.2s ease',
      }}
    >
      <div style={{ flex: 1, minWidth: 0, marginRight: '1rem' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '0.25rem' }}>
          <span style={{ fontFamily: 'monospace', color: '#94a3b8', fontSize: '0.85rem', fontWeight: 600 }}>
            {task.id}
          </span>
          <span
            className={`badge ${getBadgeClass(task.priority)}`}
            style={{
              padding: '0.15rem 0.5rem',
              borderRadius: '9999px',
              fontSize: '0.7rem',
              fontWeight: 700,
            }}
          >
            {task.priority}
          </span>
          <span style={{ fontSize: '0.75rem', color: '#64748b' }}>
            [{task.category}]
          </span>
        </div>
        <div
          style={{
            fontSize: '1.05rem',
            fontWeight: 600,
            color: isCompleted ? '#94a3b8' : '#f8fafc',
            textDecoration: isCompleted ? 'line-through' : 'none',
          }}
        >
          {task.topic}
        </div>
      </div>

      <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
        <button
          type="button"
          onClick={() => onStatusToggle(task.id)}
          style={{
            background: isCompleted ? '#059669' : '#334155',
            color: 'white',
            border: 'none',
            padding: '0.4rem 0.8rem',
            borderRadius: '6px',
            fontSize: '0.8rem',
            fontWeight: 600,
            cursor: 'pointer',
          }}
        >
          {isCompleted ? 'Completed' : 'Mark Done'}
        </button>
        <button
          type="button"
          onClick={() => onDelete(task.id)}
          aria-label={`Delete ${task.id}`}
          style={{
            background: 'transparent',
            color: '#ef4444',
            border: '1px solid rgba(239, 68, 68, 0.3)',
            padding: '0.4rem 0.8rem',
            borderRadius: '6px',
            fontSize: '0.8rem',
            fontWeight: 600,
            cursor: 'pointer',
          }}
        >
          Delete
        </button>
      </div>
    </div>
  );
}

export default TaskCard;
