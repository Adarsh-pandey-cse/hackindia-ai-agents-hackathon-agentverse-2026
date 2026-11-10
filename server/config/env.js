/**
 * Centralized Environment Configuration
 * Validates and exposes typed environment variables with sensible defaults.
 */
import dotenv from 'dotenv';
import path from 'node:path';

// Load .env if present
dotenv.config();

export const config = {
  port: parseInt(process.env.PORT || '3000', 10),
  nodeEnv: process.env.NODE_ENV || 'development',
  isProduction: process.env.NODE_ENV === 'production',
  isTest: process.env.NODE_ENV === 'test',
  apiKey: process.env.API_KEY || 'agentverse-secret-key-2026',
  corsOrigin: process.env.CORS_ORIGIN || '*',
  version: '1.0.0',
};

export default config;
