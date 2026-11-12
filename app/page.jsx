export default function HomePage() {
  return (
    <section style={{ maxWidth: '800px', margin: '0 auto' }}>
      <div style={{ background: '#1e293b', border: '1px solid #334155', borderRadius: '8px', padding: '2rem' }}>
        <h2 style={{ marginTop: 0, color: '#f97316' }}>Next.js App Router Architecture</h2>
        <p style={{ color: '#cbd5e1', lineHeight: 1.6 }}>
          This application proves modern Next.js App Router capabilities for HackIndia 2026:
        </p>
        <ul style={{ color: '#cbd5e1', lineHeight: 1.8 }}>
          <li><strong>File-based Routing:</strong> <code>app/page.jsx</code> (Home) and <code>app/tasks/page.jsx</code> (Tasks)</li>
          <li><strong>Shared Layout:</strong> <code>app/layout.jsx</code> wrapping children with common UI and navigation</li>
          <li><strong>Server Component:</strong> <code>app/tasks/page.jsx</code> executes async/await data fetching on server</li>
          <li><strong>Client Component:</strong> <code>app/components/TaskForm.jsx</code> with <code>'use client'</code> directive</li>
          <li><strong>Route Handler:</strong> <code>app/api/tasks/route.js</code> providing GET and POST endpoints</li>
        </ul>
        <div style={{ marginTop: '1.5rem' }}>
          <a href="/tasks" style={{ display: 'inline-block', padding: '0.6rem 1.2rem', background: '#f97316', color: '#fff', borderRadius: '6px', textDecoration: 'none', fontWeight: 600 }}>
            Open Server Component Tasks Page →
          </a>
        </div>
      </div>
    </section>
  );
}
