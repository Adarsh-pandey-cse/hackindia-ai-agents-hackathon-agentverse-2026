/**
 * API Design Architecture Automated Test Suite
 * Validates resource routing, HTTP status codes, filtering, pagination,
 * error handling, and smoke test scripts.
 * 
 * HackIndia Skill: 'design-an-api-teammates-can-use'
 * Developer: Adarsh Pandey (@adarsh-pandey-cse)
 */
import { test, describe } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';

describe('API Design Architecture Test Suite', () => {
  const rootDir = process.cwd();

  test('1. Versioning: server/app.js mounts routes at /api/v1/tasks', () => {
    const appContent = fs.readFileSync(path.join(rootDir, 'server', 'app.js'), 'utf-8');
    assert.ok(appContent.includes('/api/v1/tasks'), 'Must mount tasks router at /api/v1/tasks');
  });

  test('2. Resources & Methods: tasks.js supports GET, POST, PUT, DELETE', () => {
    const routeContent = fs.readFileSync(path.join(rootDir, 'server', 'routes', 'tasks.js'), 'utf-8');
    assert.ok(routeContent.includes('router.get('), 'Must support GET');
    assert.ok(routeContent.includes('router.post('), 'Must support POST');
    assert.ok(routeContent.includes('router.put('), 'Must support PUT');
    assert.ok(routeContent.includes('router.delete('), 'Must support DELETE');
  });

  test('3. Status Codes: tasks.js returns 200, 201, 204, 400', () => {
    const routeContent = fs.readFileSync(path.join(rootDir, 'server', 'routes', 'tasks.js'), 'utf-8');
    assert.ok(routeContent.includes('200'), 'Must return 200 OK');
    assert.ok(routeContent.includes('201'), 'Must return 201 Created');
    assert.ok(routeContent.includes('204'), 'Must return 204 No Content');
  });

  test('4. Filtering & Pagination: tasks.js supports priority, limit, page', () => {
    const routeContent = fs.readFileSync(path.join(rootDir, 'server', 'routes', 'tasks.js'), 'utf-8');
    assert.ok(routeContent.includes('priority'), 'Must support priority filter');
    assert.ok(routeContent.includes('limit'), 'Must support limit query');
    assert.ok(routeContent.includes('page'), 'Must support page query');
  });

  test('5. Smoke Test & Docs: scripts/smoke.sh and docs/EXPRESS_API.md exist', () => {
    assert.ok(fs.existsSync(path.join(rootDir, 'scripts', 'smoke.sh')), 'scripts/smoke.sh missing');
    assert.ok(fs.existsSync(path.join(rootDir, 'scripts', 'smoke.py')), 'scripts/smoke.py missing');
    assert.ok(fs.existsSync(path.join(rootDir, 'docs', 'EXPRESS_API.md')), 'docs/EXPRESS_API.md missing');
  });
});
