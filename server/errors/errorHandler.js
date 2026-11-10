/**
 * Centralized Error Handling Subsystem
 * Exports custom ApiError class and 4-argument Express error handling middleware.
 */

export class ApiError extends Error {
  constructor(statusCode, message, code = 'INTERNAL_ERROR', details = null) {
    super(message);
    this.name = 'ApiError';
    this.statusCode = statusCode;
    this.code = code;
    this.details = details;
    Error.captureStackTrace(this, this.constructor);
  }

  static badRequest(message, details = null) {
    return new ApiError(400, message, 'BAD_REQUEST', details);
  }

  static unauthorized(message = 'Unauthorized') {
    return new ApiError(401, message, 'UNAUTHORIZED');
  }

  static forbidden(message = 'Forbidden') {
    return new ApiError(403, message, 'FORBIDDEN');
  }

  static notFound(message = 'Resource not found') {
    return new ApiError(404, message, 'NOT_FOUND');
  }

  static unprocessable(message, details = null) {
    return new ApiError(422, message, 'UNPROCESSABLE_ENTITY', details);
  }

  static internal(message = 'Internal server error') {
    return new ApiError(500, message, 'INTERNAL_SERVER_ERROR');
  }
}

/**
 * Centralized 4-argument Express error handling middleware.
 * Must define (err, req, res, next) for Express to recognize it as an error handler.
 */
export function errorHandler(err, req, res, next) {
  const isApiError = err instanceof ApiError;
  const status = isApiError ? err.statusCode : (err.status || 500);
  const code = isApiError ? err.code : 'INTERNAL_SERVER_ERROR';
  const message = err.message || 'An unexpected error occurred';
  const details = isApiError ? err.details : null;

  // Log 500s for monitoring
  if (status >= 500 && process.env.NODE_ENV !== 'test') {
    console.error('[ServerError]', err);
  }

  res.status(status).json({
    success: false,
    error: {
      message,
      code,
      status,
      ...(details ? { details } : {}),
      ...(process.env.NODE_ENV === 'development' ? { stack: err.stack } : {})
    }
  });
}

export default errorHandler;
