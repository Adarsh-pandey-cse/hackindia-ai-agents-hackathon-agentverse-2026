'use client';

import { useState } from 'react';

export default function LoginPage() {
  const [email, setEmail] = useState('developer@hackindia.org');
  const [password, setPassword] = useState('HackIndia2026!SafeAuth');
  const [status, setStatus] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setStatus(null);

    try {
      const res = await fetch('/api/auth', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password, action: 'signin' }),
      });
      const data = await res.json();
      if (!res.ok) {
        setStatus({ type: 'error', message: data.error || 'Authentication failed' });
      } else {
        setStatus({
          type: 'success',
          message: `Welcome ${data.user.name}! Safe session cookie established.`,
        });
      }
    } catch (err) {
      setStatus({ type: 'error', message: err.message });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: '420px', margin: '40px auto', padding: '24px', border: '1px solid #e2e8f0', borderRadius: '8px', background: '#fff' }}>
      <h2 style={{ fontSize: '20px', fontWeight: 'bold', marginBottom: '16px' }}>Safe Sign-In (Next.js App Router)</h2>
      <p style={{ fontSize: '13px', color: '#64748b', marginBottom: '20px' }}>
        Uses bcrypt password verification and HttpOnly SameSite=Strict session cookies.
      </p>

      <form onSubmit={handleSubmit}>
        <div style={{ marginBottom: '14px' }}>
          <label style={{ display: 'block', fontSize: '12px', fontWeight: '600', marginBottom: '4px' }}>Email</label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
            style={{ width: '100%', padding: '8px 12px', border: '1px solid #cbd5e1', borderRadius: '4px' }}
          />
        </div>

        <div style={{ marginBottom: '18px' }}>
          <label style={{ display: 'block', fontSize: '12px', fontWeight: '600', marginBottom: '4px' }}>Password</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            style={{ width: '100%', padding: '8px 12px', border: '1px solid #cbd5e1', borderRadius: '4px' }}
          />
        </div>

        <button
          type="submit"
          disabled={loading}
          style={{ width: '100%', padding: '10px', background: '#0284c7', color: '#fff', border: 'none', borderRadius: '4px', fontWeight: 'bold', cursor: 'pointer' }}
        >
          {loading ? 'Authenticating...' : 'Sign In Safely'}
        </button>
      </form>

      {status && (
        <div
          style={{
            marginTop: '16px',
            padding: '10px',
            borderRadius: '4px',
            fontSize: '13px',
            background: status.type === 'error' ? '#fee2e2' : '#dcfce7',
            color: status.type === 'error' ? '#991b1b' : '#166534',
          }}
        >
          {status.message}
        </div>
      )}
    </div>
  );
}
