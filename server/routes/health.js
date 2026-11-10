/**
 * Health & Diagnostic Routes
 * Monitored by Docker, uptime checkers, and Kubernetes probes.
 */
import { Router } from 'express';
import config from '../config/env.js';

const router = Router();

router.get('/health', (req, res) => {
  res.status(200).json({
    status: 'ok',
    uptime: Math.floor(process.uptime()),
    timestamp: new Date().toISOString(),
    service: 'agentverse-express-api',
    version: config.version,
    environment: config.nodeEnv,
    nodeVersion: process.version,
  });
});

router.get('/', (req, res) => {
  res.status(200).json({
    message: 'Welcome to AgentVerse Recruiter-Ready Express 5 API',
    version: config.version,
    documentation: '/docs',
    endpoints: {
      health: 'GET /health',
      tasks: 'GET /api/v1/tasks',
      createTask: 'POST /api/v1/tasks',
      getTaskById: 'GET /api/v1/tasks/:id',
      runAgent: 'POST /api/v1/agent/run',
    }
  });
});

export default router;
