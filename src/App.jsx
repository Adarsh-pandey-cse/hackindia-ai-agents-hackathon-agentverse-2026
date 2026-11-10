import React, { useState, useEffect } from 'react';
import MetricsBar from './components/MetricsBar.jsx';
import TaskFilter from './components/TaskFilter.jsx';
import TaskList from './components/TaskList.jsx';
import TaskForm from './components/TaskForm.jsx';
import './styles/app.css';

const INITIAL_TASKS = [
  { id: 'TASK-001', topic: 'Autonomous AI Agents in 2026', category: 'ai_tech_trends', priority: 'HIGH', status: 'COMPLETED' },
  { id: 'TASK-002', topic: 'Cryptocurrency and Web3 Ecosystem Metrics', category: 'market_indicators', priority: 'MEDIUM', status: 'IN_PROGRESS' },
  { id: 'TASK-003', topic: 'Open Source AI Tools & Frameworks', category: 'developer_ecosystem', priority: 'HIGH', status: 'PENDING' },
  { id: 'TASK-004', topic: 'Vector Database Benchmarking and Performance', category: 'ai_tech_trends', priority: 'LOW', status: 'PENDING' },
  { id: 'TASK-005', topic: 'Containerized Deployment with Docker and Kubernetes', category: 'developer_ecosystem', priority: 'MEDIUM', status: 'COMPLETED' },
];

/**
 * App Root Container
 * Demonstrates:
 * 1. useState: Management of tasks, search query, priority filter, and network status.
 * 2. Lifted state: State shared between TaskFilter, TaskForm, and TaskList.
 * 3. Justified useEffect: Fetches initial live telemetry from Express backend /api/v1/tasks
 *    with an AbortController for clean component teardown and race condition prevention.
 */
export function App() {
  const [tasks, setTasks] = useState(INITIAL_TASKS);
  const [searchQuery, setSearchQuery] = useState('');
  const [priorityFilter, setPriorityFilter] = useState('ALL');
  const [dataSource, setDataSource] = useState('Local Store');

  /**
   * Justified useEffect:
   * Synchronizes component with external Express REST API on mount.
   * Includes cleanup function aborting ongoing fetch to prevent state updates on unmounted component.
   */
  useEffect(() => {
    const controller = new AbortController();

    async function fetchLiveTasks() {
      try {
        const response = await fetch('/api/v1/tasks', { signal: controller.signal });
        if (response.ok) {
          const payload = await response.json();
          if (payload.data && Array.isArray(payload.data) && payload.data.length > 0) {
            setTasks(payload.data);
            setDataSource('Live Express 5 API');
          }
        }
      } catch (err) {
        if (err.name !== 'AbortError') {
          // Graceful fallback to verified initial state
          setDataSource('Local Store (Offline Resilience)');
        }
      }
    }

    fetchLiveTasks();

    return () => {
      // Cleanup: cancel pending request when component unmounts
      controller.abort();
    };
  }, []); // Run once on mount

  // Handlers for state updates
  const handleAddTask = (newTaskData) => {
    const newTask = {
      id: `TASK-${String(tasks.length + 1).padStart(3, '0')}`,
      ...newTaskData,
      status: 'PENDING',
    };
    setTasks((prev) => [newTask, ...prev]);
  };

  const handleStatusToggle = (id) => {
    setTasks((prev) =>
      prev.map((t) =>
        t.id === id ? { ...t, status: t.status === 'COMPLETED' ? 'PENDING' : 'COMPLETED' } : t
      )
    );
  };

  const handleDelete = (id) => {
    setTasks((prev) => prev.filter((t) => t.id !== id));
  };

  const handleResetFilter = () => {
    setSearchQuery('');
    setPriorityFilter('ALL');
  };

  // Filtered task computation (pure, immutable)
  const filteredTasks = tasks.filter((t) => {
    const matchesPriority = priorityFilter === 'ALL' || t.priority === priorityFilter;
    const matchesSearch =
      !searchQuery ||
      t.topic.toLowerCase().includes(searchQuery.toLowerCase()) ||
      t.category.toLowerCase().includes(searchQuery.toLowerCase()) ||
      t.id.toLowerCase().includes(searchQuery.toLowerCase());
    return matchesPriority && matchesSearch;
  });

  const completedCount = tasks.filter((t) => t.status === 'COMPLETED').length;

  return (
    <div className="container" style={{ maxWidth: '1100px', margin: '0 auto', padding: '2rem 1rem' }}>
      <header style={{ marginBottom: '2rem', display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: '1rem' }}>
        <div>
          <span style={{ color: '#f97316', fontSize: '0.8rem', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '0.1em' }}>
            HackIndia React Skill
          </span>
          <h1 style={{ fontSize: '2.2rem', fontWeight: 800, color: '#f8fafc', marginTop: '0.2rem' }}>
            AgentVerse Control Dashboard
          </h1>
          <p style={{ color: '#94a3b8', fontSize: '0.95rem' }}>
            Readable, accessible React 18 application built with Vite and Node.js 24 LTS.
          </p>
        </div>
        <div style={{ background: '#1e293b', border: '1px solid #334155', borderRadius: '6px', padding: '0.4rem 0.8rem', fontSize: '0.8rem', color: '#94a3b8' }}>
          Data Source: <strong style={{ color: '#10b981' }}>{dataSource}</strong>
        </div>
      </header>

      {/* Metrics Header Component */}
      <MetricsBar
        totalTasks={tasks.length}
        completedTasks={completedCount}
        accuracy="96.25%"
        latency="879ms"
      />

      {/* Controlled Workload Dispatch Form */}
      <TaskForm onAddTask={handleAddTask} />

      {/* Controlled Search & Filter Bar (Lifted State) */}
      <TaskFilter
        searchQuery={searchQuery}
        onSearchChange={setSearchQuery}
        priorityFilter={priorityFilter}
        onPriorityChange={setPriorityFilter}
      />

      {/* Stable List Rendering Component */}
      <TaskList
        tasks={filteredTasks}
        onStatusToggle={handleStatusToggle}
        onDelete={handleDelete}
        onResetFilter={handleResetFilter}
      />
    </div>
  );
}

export default App;
