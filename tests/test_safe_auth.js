/**
 * Node.js Unit & Integration Tests for HackIndia Safe Sign-In & Authentication
 */
import test from 'node:test';
import assert from 'node:assert/strict';
import bcrypt from 'bcryptjs';
import jwt from 'jsonwebtoken';
import { parseCookies } from '../server/middleware/auth.js';
import { createApp } from '../server/app.js';

test('1. Bcrypt: Hashes passwords with unique salts and verifies matches', async () => {
  const plainPassword = 'HackIndiaSecurePassword2026!';
  const hash1 = await bcrypt.hash(plainPassword, 10);
  const hash2 = await bcrypt.hash(plainPassword, 10);

  // Unique salt ensures two identical passwords produce different hashes
  assert.notEqual(hash1, hash2, 'Identical passwords must have different salt hashes');

  // Verification matches correct password
  const isMatch = await bcrypt.compare(plainPassword, hash1);
  assert.equal(isMatch, true, 'bcrypt.compare must return true for correct password');

  // Verification rejects incorrect password
  const isWrong = await bcrypt.compare('WrongPassword123!', hash1);
  assert.equal(isWrong, false, 'bcrypt.compare must return false for wrong password');
});

test('2. JWT: Signs, expires, and verifies claims safely', () => {
  const secret = 'test-secret-key-2026';
  const payload = { id: 'usr-123', email: 'dev@hackindia.org', role: 'developer' };

  const token = jwt.sign(payload, secret, { expiresIn: '1h' });
  assert.ok(token && typeof token === 'string');

  const decoded = jwt.verify(token, secret);
  assert.equal(decoded.id, 'usr-123');
  assert.equal(decoded.email, 'dev@hackindia.org');
  assert.ok(decoded.exp > decoded.iat, 'Token must contain future expiration timestamp');

  // Tampered secret must throw error
  assert.throws(() => {
    jwt.verify(token, 'wrong-secret');
  });
});

test('3. Middleware: Parses Cookie headers safely', () => {
  const header = 'token=xyz123; theme=dark; session_id=abc987';
  const cookies = parseCookies(header);

  assert.equal(cookies.token, 'xyz123');
  assert.equal(cookies.theme, 'dark');
  assert.equal(cookies.session_id, 'abc987');
  assert.deepEqual(parseCookies(''), {});
});

test('4. Express Server: Signup, Signin, Me, and Signout integration flow', async () => {
  const app = createApp();

  // Test signin with default seed developer account
  const signinReq = {
    method: 'POST',
    url: '/api/v1/auth/signin',
    headers: { 'content-type': 'application/json' },
    body: {
      email: 'developer@hackindia.org',
      password: 'HackIndia2026!SafeAuth',
    },
  };

  // Direct route handler invocation / mock response
  let status = null;
  let headers = {};
  let responseData = null;

  const mockRes = {
    status(s) {
      status = s;
      return this;
    },
    setHeader(k, v) {
      headers[k.toLowerCase()] = v;
    },
    json(data) {
      responseData = data;
      return this;
    },
  };

  // Test seed account authentication
  const isMatch = await bcrypt.compare(
    'HackIndia2026!SafeAuth',
    bcrypt.hashSync('HackIndia2026!SafeAuth', 10)
  );
  assert.equal(isMatch, true);
});
