import TaskForm from '../components/TaskForm.jsx';

/**
 * Server Component: Tasks Dashboard
 * Fetches data asynchronously on the server before streaming HTML to client.
 */
async function fetchTasks() {
  // Simulates server-side database/API query
  return [
    { id: 'TASK-001', topic: 'Autonomous AI Agents in 2026', priority: 'HIGH', status: 'COMPLETED' },
    { id: 'TASK-002', topic: 'Cryptocurrency and Web3 Ecosystem Metrics', priority: 'MEDIUM', status: 'IN_PROGRESS' },
    { id: 'TASK-003', topic: 'Open Source AI Tools & Frameworks', priority: 'HIGH', status: 'PENDING' },
    { id: 'TASK-004', topic: 'Vector Database Benchmarking and Performance', priority: 'LOW', status: 'PENDING' },
  ];
}

export default async function TasksPage() {
  const tasks = await fetchTasks();

  return (
    <section style={{ maxWidth: '900px', margin: '0 auto' }}>
      <header style={{ marginBottom: '1.5rem' }}>
        <h2 style={{ margin: 0, color: '#f8fafc' }}>Tasks Feed (Server Component)</h2>
        <p style={{ color: '#94a3b8', margin: '0.5rem 0 0' }}>
          Rendered on the server with <code>async/await</code> data fetch. Zero client JavaScript needed for rendering this list.
        </p>
      </header>

      {/* Client Component Boundary */}
      <TaskForm />

      <div style={{ display: 'grid', gap: '0.75rem' }}>
        {tasks.map((task) => (
          <div
            key={task.id}
            style={{
              padding: '1rem',
              background: '#1e293b',
              border: '1px solid #334155',
              borderRadius: '6px',
              display: 'flex',
              justifyContent: 'space-between',
              alignItems: 'center',
            }}
          >
            <div>
              <strong style={{ color: '#f97316' }}>{task.id}</strong>: <span style={{ color: '#f8fafc' }}>{task.topic}</span>
            </div>
            <span
              style={{
                padding: '0.2rem 0.6rem',
                borderRadius: '9999px',
                fontSize: '0.75rem',
                fontWeight: 700,
                background: task.priority === 'HIGH' ? 'rgba(239, 68, 68, 0.2)' : task.priority === 'MEDIUM' ? 'rgba(245, 158, 11, 0.2)' : 'rgba(59, 130, 246, 0.2)',
                color: task.priority === 'HIGH' ? '#f87171' : task.priority === 'MEDIUM' ? '#fbbf24' : '#60a5fa',
                border: '1px solid currentColor',
              }}
            >
              {task.priority}
            </span>
          </div>
        ))}
      </div>
    </section>
  );
}
