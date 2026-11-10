/**
 * Request Validation Middleware
 * Validates request query parameters and body payloads against schemas.
 */
import { ApiError } from '../errors/errorHandler.js';

const VALID_PRIORITIES = ['HIGH', 'MEDIUM', 'LOW'];

export function validateTaskBody(req, res, next) {
  const { topic, category, priority } = req.body || {};
  const errors = [];

  if (!topic || typeof topic !== 'string' || !topic.trim()) {
    errors.push({ field: 'topic', message: 'Topic is required and must be a non-empty string' });
  }

  if (!category || typeof category !== 'string' || !category.trim()) {
    errors.push({ field: 'category', message: 'Category is required and must be a non-empty string' });
  }

  if (!priority || typeof priority !== 'string') {
    errors.push({ field: 'priority', message: `Priority is required and must be one of: ${VALID_PRIORITIES.join(', ')}` });
  } else if (!VALID_PRIORITIES.includes(priority.toUpperCase())) {
    errors.push({ field: 'priority', message: `Invalid priority '${priority}'. Allowed values: ${VALID_PRIORITIES.join(', ')}` });
  }

  if (errors.length > 0) {
    return next(ApiError.badRequest('Validation failed for task payload', errors));
  }

  // Normalize priority
  req.body.priority = priority.toUpperCase();
  next();
}

export function validateTaskQuery(req, res, next) {
  const { priority, limit, page } = req.query;
  const errors = [];

  if (priority && !VALID_PRIORITIES.includes(priority.toUpperCase())) {
    errors.push({ field: 'priority', message: `Query priority must be one of: ${VALID_PRIORITIES.join(', ')}` });
  }

  if (limit !== undefined) {
    const parsedLimit = parseInt(limit, 10);
    if (isNaN(parsedLimit) || parsedLimit <= 0 || parsedLimit > 100) {
      errors.push({ field: 'limit', message: 'Limit must be a positive integer between 1 and 100' });
    }
  }

  if (page !== undefined) {
    const parsedPage = parseInt(page, 10);
    if (isNaN(parsedPage) || parsedPage <= 0) {
      errors.push({ field: 'page', message: 'Page must be a positive integer >= 1' });
    }
  }

  if (errors.length > 0) {
    return next(ApiError.badRequest('Invalid query parameters', errors));
  }

  next();
}
