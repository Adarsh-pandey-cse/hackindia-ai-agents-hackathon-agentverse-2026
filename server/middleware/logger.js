/**
 * Request Logging Middleware
 * Measures latency and logs structured request telemetry.
 */
export function requestLogger(req, res, next) {
  const start = Date.now();
  res.on('finish', () => {
    const duration = Date.now() - start;
    if (process.env.NODE_ENV !== 'test') {
      const timestamp = new Date().toISOString();
      console.log(`[${timestamp}] ${req.method} ${req.originalUrl} ${res.statusCode} -${duration}ms`);
    }
  });
  next();
}

export default requestLogger;
