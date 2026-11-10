/**
 * Express Application Setup
 * Configures middleware, security, route mounting, 404 handling, and centralized error handling.
 * Compatible with Node.js 24 LTS and Express 5.
 */
import express from 'express';
import cors from 'cors';
import config from './config/env.js';
import requestLogger from './middleware/logger.js';
import { optionalApiKeyAuth } from './middleware/auth.js';
import { errorHandler, ApiError } from './errors/errorHandler.js';

// Route imports
import healthRoutes from './routes/health.js';
import tasksRoutes from './routes/tasks.js';
import agentRoutes from './routes/agent.js';

export function createApp() {
  const app = express();

  // Core Middleware
  app.use(cors({ origin: config.corsOrigin }));
  app.use(express.json({ limit: '1mb' }));
  app.use(express.urlencoded({ extended: true }));
  app.use(requestLogger);

  // Health and root diagnostics
  app.use('/', healthRoutes);

  // API v1 Resource Routes
  app.use('/api/v1/tasks', optionalApiKeyAuth, tasksRoutes);
  app.use('/api/v1/agent', optionalApiKeyAuth, agentRoutes);

  // 404 Catch-All Handler
  app.use((req, res, next) => {
    next(ApiError.notFound(`Endpoint ${req.method} ${req.originalUrl} not found`));
  });

  // Centralized Error Handling Middleware (must be 4 arguments)
  app.use(errorHandler);

  return app;
}

export const app = createApp();
export default app;
