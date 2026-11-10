/**
 * Authentication & API Key Middleware
 * Verifies optional API key for mutating administration routes.
 */
import config from '../config/env.js';
import { ApiError } from '../errors/errorHandler.js';

export function optionalApiKeyAuth(req, res, next) {
  const authHeader = req.headers['x-api-key'] || req.headers['authorization'];
  if (!authHeader) {
    // Non-enforced for open hackathon demo, passes through
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

export default optionalApiKeyAuth;
