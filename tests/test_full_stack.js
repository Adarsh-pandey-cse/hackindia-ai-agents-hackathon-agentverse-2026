/**
 * Weekend Full-Stack Repository Automated Test Suite
 * Validates complete end-to-end full-stack integration:
 * - Client (React 18 + Vite 5 + JSX Components + Loading/Error states)
 * - Server (Express 5 + Modular Routes + 4-arg Error Handler)
 * - Persistence (Docker PostgreSQL config + JSON Data Stores + ML Models)
 * - Environment (.env.example + git-ignored secrets)
 * - Package Scripts & Verification
 * 
 * HackIndia Skill: 'ship-a-weekend-full-stack-repo'
 * Developer: Adarsh Pandey (@adarsh-pandey-cse)
 */
import { test, describe } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import app from '../server/app.js';

describe('Weekend Full-Stack Repository Test Suite', () => {
  const rootDir = process.cwd();

  test('1. Frontend Client: React 18, Vite config, JSX components and loading/failure states exist', () => {
    assert.ok(fs.existsSync(path.join(rootDir, 'src', 'App.jsx')), 'src/App.jsx missing');
    assert.ok(fs.existsSync(path.join(rootDir, 'src', 'main.jsx')), 'src/main.jsx missing');
    assert.ok(fs.existsSync(path.join(rootDir, 'vite.config.js')), 'vite.config.js missing');
    assert.ok(fs.existsSync(path.join(rootDir, 'index.html')), 'index.html missing');

    const appContent = fs.readFileSync(path.join(rootDir, 'src', 'App.jsx'), 'utf-8');
    assert.ok(appContent.includes('useState'), 'App.jsx must use useState');
    assert.ok(appContent.includes('useEffect'), 'App.jsx must use useEffect');
    assert.ok(appContent.includes('isLoading'), 'App.jsx must manage isLoading state');
    assert.ok(appContent.includes('errorMessage'), 'App.jsx must manage errorMessage state');
    assert.ok(appContent.includes('fetch('), 'App.jsx must fetch from API');
    assert.ok(appContent.includes('AbortController'), 'App.jsx must use AbortController');

    const viteContent = fs.readFileSync(path.join(rootDir, 'vite.config.js'), 'utf-8');
    assert.ok(viteContent.includes('/api'), 'vite.config.js must configure /api reverse proxy');
  });

  test('2. Backend Server: Modular Express 5 structure, routers, and 4-arg error handler exist', () => {
    assert.ok(fs.existsSync(path.join(rootDir, 'server', 'index.js')), 'server/index.js missing');
    assert.ok(fs.existsSync(path.join(rootDir, 'server', 'app.js')), 'server/app.js missing');
    assert.ok(fs.existsSync(path.join(rootDir, 'server', 'routes', 'tasks.js')), 'server/routes/tasks.js missing');
    assert.ok(fs.existsSync(path.join(rootDir, 'server', 'routes', 'agent.js')), 'server/routes/agent.js missing');
    assert.ok(fs.existsSync(path.join(rootDir, 'server', 'errors', 'errorHandler.js')), 'server/errors/errorHandler.js missing');

    const errorsContent = fs.readFileSync(path.join(rootDir, 'server', 'errors', 'errorHandler.js'), 'utf-8');
    assert.ok(errorsContent.includes('(err, req, res, next)'), 'Must define 4-argument error handler signature');
  });

  test('3. Database & Storage: Docker Compose PostgreSQL and structured datasets exist', () => {
    assert.ok(fs.existsSync(path.join(rootDir, 'docker-compose.yml')), 'docker-compose.yml missing');
    const dockerContent = fs.readFileSync(path.join(rootDir, 'docker-compose.yml'), 'utf-8');
    assert.ok(dockerContent.toLowerCase().includes('postgres'), 'docker-compose.yml must define postgres service');

    assert.ok(fs.existsSync(path.join(rootDir, 'data', 'chunks.json')), 'data/chunks.json missing');
    assert.ok(fs.existsSync(path.join(rootDir, 'data', 'sample_input.json')), 'data/sample_input.json missing');
    assert.ok(fs.existsSync(path.join(rootDir, 'models', 'agent_workload_classifier.joblib')), 'ML model binary missing');
  });

  test('4. Environment & Secrets: .env.example exists and active secrets are safely ignored', () => {
    assert.ok(fs.existsSync(path.join(rootDir, '.env.example')), '.env.example template missing');
    const envExample = fs.readFileSync(path.join(rootDir, '.env.example'), 'utf-8');
    assert.ok(envExample.includes('PORT='), '.env.example must specify PORT');
    assert.ok(envExample.includes('DATABASE_URL='), '.env.example must specify DATABASE_URL');

    assert.ok(fs.existsSync(path.join(rootDir, '.gitignore')), '.gitignore missing');
    const gitignore = fs.readFileSync(path.join(rootDir, '.gitignore'), 'utf-8');
    assert.ok(gitignore.includes('.env'), '.gitignore must ignore .env files');
  });

  test('5. Navigable Scripts & Documentation: package.json scripts and full-stack docs exist', () => {
    const pkg = JSON.parse(fs.readFileSync(path.join(rootDir, 'package.json'), 'utf-8'));
    const scripts = pkg.scripts || {};
    assert.ok(scripts.start, 'Missing npm run start');
    assert.ok(scripts.dev, 'Missing npm run dev');
    assert.ok(scripts.api, 'Missing npm run api');
    assert.ok(scripts.fullstack, 'Missing npm run fullstack');
    assert.ok(scripts.test, 'Missing npm run test');
    assert.ok(scripts.build, 'Missing npm run build');
    assert.ok(scripts['verify:fullstack'], 'Missing npm run verify:fullstack');

    assert.ok(fs.existsSync(path.join(rootDir, 'docs', 'FULL_STACK_ARCHITECTURE.md')), 'docs/FULL_STACK_ARCHITECTURE.md missing');
    assert.ok(fs.existsSync(path.join(rootDir, 'verify_full_stack_repo.py')), 'verify_full_stack_repo.py missing');
  });

  test('6. API Contract: Express server handles /health and /api/v1/tasks in-memory requests', async () => {
    const server = app.listen(0);
    const port = server.address().port;
    const baseUrl = `http://127.0.0.1:${port}`;

    try {
      const healthRes = await fetch(`${baseUrl}/health`);
      assert.equal(healthRes.status, 200, '/health should return 200');
      const healthData = await healthRes.json();
      assert.equal(healthData.status, 'ok');

      const tasksRes = await fetch(`${baseUrl}/api/v1/tasks`);
      assert.equal(tasksRes.status, 200, '/api/v1/tasks should return 200');
      const tasksData = await tasksRes.json();
      assert.equal(tasksData.success, true);
      assert.ok(Array.isArray(tasksData.data));
    } finally {
      server.close();
    }
  });
});
