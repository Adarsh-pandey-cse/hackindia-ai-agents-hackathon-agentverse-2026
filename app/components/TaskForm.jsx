'use client';

import { useState } from 'react';

/**
 * Client Component for Interactive Workload Dispatch
 * Explicit 'use client' directive marks this boundary for React hydration.
 */
export default function TaskForm({ onTaskAdded }) {
  const [topic, setTopic] = useState('');
  const [priority, setPriority] = useState('HIGH');
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!topic.trim()) return;

    setLoading(true);
    setMessage(null);
    try {
      const res = await fetch('/api/tasks', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ topic, priority }),
      });
      if (res.ok) {
        setTopic('');
        setMessage('Task created successfully via Route Handler!');
        if (onTaskAdded) onTaskAdded();
      } else {
        setMessage('Failed to create task.');
      }
    } catch (err) {
      setMessage(`Network notice: ${err.message}`);
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} style={{ background: '#0f172a', border: '1px solid #334155', padding: '1.25rem', borderRadius: '8px', marginBottom: '2rem' }}>
      <h3 style={{ margin: '0 0 1rem', fontSize: '1.1rem', color: '#f8fafc' }}>Add Task (Interactive Client Component)</h3>
      <div style={{ display: 'flex', gap: '0.75rem', flexWrap: 'wrap' }}>
        <input
          type="text"
          value={topic}
          onChange={(e) => setTopic(e.target.value)}
          placeholder="Enter task topic..."
          style={{ flex: 1, minWidth: '220px', padding: '0.6rem', borderRadius: '6px', border: '1px solid #475569', background: '#1e293b', color: '#fff' }}
        />
        <select
          value={priority}
          onChange={(e) => setPriority(e.target.value)}
          style={{ padding: '0.6rem', borderRadius: '6px', border: '1px solid #475569', background: '#1e293b', color: '#fff' }}
        >
          <option value="HIGH">HIGH</option>
          <option value="MEDIUM">MEDIUM</option>
          <option value="LOW">LOW</option>
        </select>
        <button
          type="submit"
          disabled={loading}
          style={{ padding: '0.6rem 1.2rem', background: '#f97316', color: '#fff', border: 'none', borderRadius: '6px', cursor: 'pointer', fontWeight: 600 }}
        >
          {loading ? 'Adding...' : 'Add Task'}
        </button>
      </div>
      {message && <p style={{ color: '#10b981', margin: '0.75rem 0 0', fontSize: '0.9rem' }}>✓ {message}</p>}
    </form>
  );
}
