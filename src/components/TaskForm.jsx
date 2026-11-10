import React, { useState } from 'react';

/**
 * TaskForm Component
 * Demonstrates a controlled form with local useState validation before submitting
 * to the lifted state in parent.
 */
export function TaskForm({ onAddTask }) {
  const [topic, setTopic] = useState('');
  const [category, setCategory] = useState('ai_tech_trends');
  const [priority, setPriority] = useState('HIGH');
  const [error, setError] = useState(null);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!topic.trim()) {
      setError('Topic cannot be empty.');
      return;
    }

    onAddTask({
      topic: topic.trim(),
      category: category.trim(),
      priority,
    });

    // Reset controlled inputs
    setTopic('');
    setError(null);
  };

  return (
    <form
      onSubmit={handleSubmit}
      style={{
        background: '#1e293b',
        border: '1px solid #334155',
        borderRadius: '8px',
        padding: '1.25rem',
        marginBottom: '1.5rem',
      }}
    >
      <h3 style={{ fontSize: '1.1rem', fontWeight: 700, color: '#f8fafc', marginBottom: '0.75rem' }}>
        ➕ Dispatch New Agent Workload
      </h3>

      {error && (
        <div style={{ background: '#7f1d1d', color: '#fca5a5', padding: '0.5rem 0.75rem', borderRadius: '4px', fontSize: '0.85rem', marginBottom: '0.75rem' }}>
          ⚠ {error}
        </div>
      )}

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '0.75rem', marginBottom: '0.75rem' }}>
        <div>
          <label style={{ display: 'block', fontSize: '0.8rem', color: '#94a3b8', marginBottom: '0.25rem' }}>
            Workload Topic:
          </label>
          <input
            type="text"
            value={topic}
            onChange={(e) => setTopic(e.target.value)}
            placeholder="e.g. Distributed Consensus Engine"
            style={{ width: '100%', padding: '0.5rem 0.75rem', borderRadius: '6px', border: '1px solid #334155', background: '#0f172a', color: '#f8fafc', fontSize: '0.85rem' }}
          />
        </div>

        <div>
          <label style={{ display: 'block', fontSize: '0.8rem', color: '#94a3b8', marginBottom: '0.25rem' }}>
            Category:
          </label>
          <select
            value={category}
            onChange={(e) => setCategory(e.target.value)}
            style={{ width: '100%', padding: '0.5rem 0.75rem', borderRadius: '6px', border: '1px solid #334155', background: '#0f172a', color: '#f8fafc', fontSize: '0.85rem' }}
          >
            <option value="ai_tech_trends">AI Tech Trends</option>
            <option value="developer_ecosystem">Developer Ecosystem</option>
            <option value="market_indicators">Market Indicators</option>
            <option value="cloud_infrastructure">Cloud Infrastructure</option>
          </select>
        </div>

        <div>
          <label style={{ display: 'block', fontSize: '0.8rem', color: '#94a3b8', marginBottom: '0.25rem' }}>
            Priority Level:
          </label>
          <select
            value={priority}
            onChange={(e) => setPriority(e.target.value)}
            style={{ width: '100%', padding: '0.5rem 0.75rem', borderRadius: '6px', border: '1px solid #334155', background: '#0f172a', color: '#f8fafc', fontSize: '0.85rem' }}
          >
            <option value="HIGH">High</option>
            <option value="MEDIUM">Medium</option>
            <option value="LOW">Low</option>
          </select>
        </div>
      </div>

      <button
        type="submit"
        style={{
          background: '#f97316',
          color: 'white',
          border: 'none',
          padding: '0.5rem 1.25rem',
          borderRadius: '6px',
          fontWeight: 600,
          cursor: 'pointer',
          fontSize: '0.85rem',
        }}
      >
        Submit Task
      </button>
    </form>
  );
}

export default TaskForm;
