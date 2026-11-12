export const metadata = {
  title: 'AgentVerse Next.js App Router',
  description: 'HackIndia 2026 Next.js App Router Project',
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body style={{ fontFamily: 'system-ui, -apple-system, sans-serif', margin: 0, padding: '2rem', background: '#0f172a', color: '#f8fafc' }}>
        <header style={{ borderBottom: '1px solid #334155', paddingBottom: '1rem', marginBottom: '2rem', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <div>
            <span style={{ color: '#f97316', fontSize: '0.8rem', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '0.1em' }}>HackIndia Next.js Skill</span>
            <h1 style={{ color: '#f8fafc', margin: '0.2rem 0 0', fontSize: '1.8rem' }}>AgentVerse App Router</h1>
          </div>
          <nav style={{ display: 'flex', gap: '1rem' }}>
            <a href="/" style={{ color: '#60a5fa', textDecoration: 'none', fontWeight: 600 }}>Home</a>
            <a href="/tasks" style={{ color: '#60a5fa', textDecoration: 'none', fontWeight: 600 }}>Tasks (Server Component)</a>
          </nav>
        </header>
        <main>{children}</main>
      </body>
    </html>
  );
}
