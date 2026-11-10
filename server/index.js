/**
 * HTTP Server Entry Point
 * Binds to port and handles lifecycle events and graceful shutdown.
 */
import app from './app.js';
import config from './config/env.js';

const server = app.listen(config.port, () => {
  console.log('========================================================================');
  console.log('  AgentVerse Express 5 REST API Server');
  console.log(`  Environment: ${config.nodeEnv}`);
  console.log(`  Node.js:     ${process.version}`);
  console.log(`  Port:        ${config.port}`);
  console.log(`  Health URL:  http://localhost:${config.port}/health`);
  console.log(`  Tasks API:   http://localhost:${config.port}/api/v1/tasks`);
  console.log('========================================================================');
});

function gracefulShutdown(signal) {
  console.log(`\nReceived ${signal}. Shutting down gracefully...`);
  server.close(() => {
    console.log('Express server closed. Exiting process.');
    process.exit(0);
  });
}

process.on('SIGTERM', () => gracefulShutdown('SIGTERM'));
process.on('SIGINT', () => gracefulShutdown('SIGINT'));

export default server;
