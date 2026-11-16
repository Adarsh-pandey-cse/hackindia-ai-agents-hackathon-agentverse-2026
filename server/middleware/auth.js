/**
 * Authentication Middleware & Security Guards
 * HackIndia "Add Safe Sign-In" Skill Implementation.
 * Implements JWT token verification from secure HTTP-only cookies or Bearer headers.
 */
import jwt from 'jsonwebtoken';
import config from '../config/env.js';
import { ApiError } from '../errors/errorHandler.js';

/**
 * Utility to parse cookies safely without extra external middleware
 */
export function parseCookies(cookieHeader) {
  const list = {};
  if (!cookieHeader) return list;

  cookieHeader.split(';').forEach((cookie) => {
    const parts = cookie.split('=');
    const name = parts.shift().trim();
    if (name) {
      list[name] = decodeURIComponent(parts.join('='));
    }
  });

  return list;
}

/**
 * Strict authentication guard for protected routes.
 * Checks HTTP-only cookie first, falls back to Authorization: Bearer header.
 */
export function requireAuth(req, res, next) {
  // 1. Try to extract from Cookie header (safe against XSS when HttpOnly is set)
  let token = null;
  const cookies = req.cookies || parseCookies(req.headers.cookie);
  if (cookies && cookies.token) {
    token = cookies.token;
  }

  // 2. Fallback to Authorization: Bearer <token> header for REST/mobile clients
  if (!token && req.headers.authorization) {
    const parts = req.headers.authorization.split(' ');
    if (parts.length === 2 && /^Bearer$/i.test(parts[0])) {
      token = parts[1];
    }
  }

  if (!token) {
    return next(ApiError.unauthorized('Authentication required: please sign in to access this resource'));
  }

  try {
    const decoded = jwt.verify(token, config.jwtSecret);
    req.user = decoded;
    req.authenticated = true;
    return next();
  } catch (err) {
    if (err.name === 'TokenExpiredError') {
      return next(ApiError.unauthorized('Authentication token has expired. Please sign in again.'));
    }
    return next(ApiError.unauthorized('Invalid authentication token'));
  }
}

/**
 * Optional API key auth for administration or backward compatibility.
 */
export function optionalApiKeyAuth(req, res, next) {
  const authHeader = req.headers['x-api-key'] || req.headers['authorization'];
  if (!authHeader) {
    req.authenticated = false;
    return next();
  }

  const token = authHeader.replace(/^Bearer\s+/i, '').trim();
  if (token === config.apiKey) {
    req.authenticated = true;
    return next();
  }

  return next(ApiError.unauthorized('Invalid API key provided'));
}

export default {
  requireAuth,
  optionalApiKeyAuth,
  parseCookies,
};
