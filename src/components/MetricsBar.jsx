import React from 'react';

/**
 * MetricsBar Component
 * Demonstrates readable presentational component receiving structured props.
 */
export function MetricsBar({ totalTasks, completedTasks, accuracy, latency }) {
  return (
    <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6" style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '1rem', marginBottom: '1.5rem' }}>
      <div className="card" style={{ background: '#1e293b', padding: '1rem', borderRadius: '8px', border: '1px solid #334155' }}>
        <div style={{ color: '#94a3b8', fontSize: '0.85rem', fontWeight: 600, textTransform: 'uppercase' }}>Total Tasks</div>
        <div style={{ fontSize: '1.8rem', fontWeight: 700, color: '#f8fafc', marginTop: '0.25rem' }}>{totalTasks}</div>
      </div>
      <div className="card" style={{ background: '#1e293b', padding: '1rem', borderRadius: '8px', border: '1px solid #334155' }}>
        <div style={{ color: '#94a3b8', fontSize: '0.85rem', fontWeight: 600, textTransform: 'uppercase' }}>Completed</div>
        <div style={{ fontSize: '1.8rem', fontWeight: 700, color: '#10b981', marginTop: '0.25rem' }}>{completedTasks}</div>
      </div>
      <div className="card" style={{ background: '#1e293b', padding: '1rem', borderRadius: '8px', border: '1px solid #334155' }}>
        <div style={{ color: '#94a3b8', fontSize: '0.85rem', fontWeight: 600, textTransform: 'uppercase' }}>Model Accuracy</div>
        <div style={{ fontSize: '1.8rem', fontWeight: 700, color: '#f97316', marginTop: '0.25rem' }}>{accuracy}</div>
      </div>
      <div className="card" style={{ background: '#1e293b', padding: '1rem', borderRadius: '8px', border: '1px solid #334155' }}>
        <div style={{ color: '#94a3b8', fontSize: '0.85rem', fontWeight: 600, textTransform: 'uppercase' }}>API Latency</div>
        <div style={{ fontSize: '1.8rem', fontWeight: 700, color: '#38bdf8', marginTop: '0.25rem' }}>{latency}</div>
      </div>
    </div>
  );
}

export default MetricsBar;
