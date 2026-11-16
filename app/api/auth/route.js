/**
 * Next.js App Router Safe Sign-In API Route Handler
 * Implements safe authentication, JWT token issuance, and HttpOnly cookies.
 */
import { NextResponse } from 'next/server';
import bcrypt from 'bcryptjs';
import jwt from 'jsonwebtoken';

const JWT_SECRET = process.env.JWT_SECRET || 'hackindia-safe-auth-secret-key-2026-agentverse';

// Pre-hashed credentials (HackIndia2026!SafeAuth)
const MOCK_USER = {
  id: 'usr-approuter-01',
  email: 'developer@hackindia.org',
  name: 'Adarsh Pandey',
  passwordHash: bcrypt.hashSync('HackIndia2026!SafeAuth', 10),
};

export async function POST(request) {
  try {
    const body = await request.json();
    const { email, password, action = 'signin' } = body || {};

    if (!email || !password) {
      return NextResponse.json(
        { error: 'Email and password are required' },
        { status: 400 }
      );
    }

    if (action === 'signin') {
      const isMatch = await bcrypt.compare(password, MOCK_USER.passwordHash);
      if (email.toLowerCase() !== MOCK_USER.email.toLowerCase() || !isMatch) {
        return NextResponse.json(
          { error: 'Invalid email or password' },
          { status: 401 }
        );
      }

      const token = jwt.sign(
        { id: MOCK_USER.id, email: MOCK_USER.email, name: MOCK_USER.name },
        JWT_SECRET,
        { expiresIn: '24h' }
      );

      const response = NextResponse.json({
        success: true,
        message: 'Signed in safely with HttpOnly cookie',
        user: { id: MOCK_USER.id, email: MOCK_USER.email, name: MOCK_USER.name },
      });

      // Set secure HTTP-only cookie in Next.js App Router
      response.cookies.set('token', token, {
        httpOnly: true,
        secure: process.env.NODE_ENV === 'production',
        sameSite: 'strict',
        path: '/',
        maxAge: 86400,
      });

      return response;
    }

    return NextResponse.json({ error: 'Unsupported action' }, { status: 400 });
  } catch (err) {
    return NextResponse.json({ error: err.message }, { status: 500 });
  }
}

export async function GET(request) {
  const token = request.cookies.get('token')?.value;

  if (!token) {
    return NextResponse.json(
      { authenticated: false, error: 'Unauthorized: missing authentication cookie' },
      { status: 401 }
    );
  }

  try {
    const decoded = jwt.verify(token, JWT_SECRET);
    return NextResponse.json({
      authenticated: true,
      user: decoded,
    });
  } catch {
    return NextResponse.json(
      { authenticated: false, error: 'Invalid or expired token' },
      { status: 401 }
    );
  }
}

export async function DELETE() {
  const response = NextResponse.json({
    success: true,
    message: 'Signed out safely',
  });

  response.cookies.set('token', '', {
    httpOnly: true,
    sameSite: 'strict',
    path: '/',
    maxAge: 0,
  });

  return response;
}
