/**
 * Next.js App Router Architecture Automated Test Suite
 * Validates file-based routing, shared layout, Server Components,
 * Client Components, and route handlers.
 * 
 * HackIndia Skill: 'ship-a-nextjs-app-router-project'
 * Developer: Adarsh Pandey (@adarsh-pandey-cse)
 */
import { test, describe } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';

describe('Next.js App Router Architecture Test Suite', () => {
  const rootDir = process.cwd();

  test('1. Dependencies: package.json specifies next, react, and react-dom', () => {
    const pkg = JSON.parse(fs.readFileSync(path.join(rootDir, 'package.json'), 'utf-8'));
    assert.ok(pkg.dependencies.next, 'Missing next dependency');
    assert.ok(pkg.dependencies.react, 'Missing react dependency');
    assert.ok(pkg.dependencies['react-dom'], 'Missing react-dom dependency');
  });

  test('2. File-based Routing: app/ layout and pages exist', () => {
    assert.ok(fs.existsSync(path.join(rootDir, 'app', 'layout.jsx')), 'app/layout.jsx missing');
    assert.ok(fs.existsSync(path.join(rootDir, 'app', 'page.jsx')), 'app/page.jsx missing');
    assert.ok(fs.existsSync(path.join(rootDir, 'app', 'tasks', 'page.jsx')), 'app/tasks/page.jsx missing');
    assert.ok(fs.existsSync(path.join(rootDir, 'next.config.mjs')), 'next.config.mjs missing');

    const layout = fs.readFileSync(path.join(rootDir, 'app', 'layout.jsx'), 'utf-8');
    assert.ok(layout.includes('<html'), 'Root layout must define <html>');
    assert.ok(layout.includes('<body'), 'Root layout must define <body>');
    assert.ok(layout.includes('{children}'), 'Root layout must render children prop');
  });

  test('3. Server Component: app/tasks/page.jsx fetches data with async/await', () => {
    const content = fs.readFileSync(path.join(rootDir, 'app', 'tasks', 'page.jsx'), 'utf-8');
    assert.ok(content.includes('async'), 'Server component must use async');
    assert.ok(content.includes('await'), 'Server component must use await');
    assert.ok(!content.includes("'use client'"), 'Server component must not declare use client');
  });

  test('4. Client Component: app/components/TaskForm.jsx marks boundary with use client', () => {
    const content = fs.readFileSync(path.join(rootDir, 'app', 'components', 'TaskForm.jsx'), 'utf-8');
    assert.ok(content.startsWith("'use client'") || content.includes("'use client'"), 'Must mark use client at top');
    assert.ok(content.includes('useState'), 'Client component must use useState for interactivity');
    assert.ok(content.includes('onSubmit'), 'Client component must handle form submission');
  });

  test('5. Route Handler: app/api/tasks/route.js implements GET and POST', () => {
    const content = fs.readFileSync(path.join(rootDir, 'app', 'api', 'tasks', 'route.js'), 'utf-8');
    assert.ok(content.includes('export async function GET'), 'Route handler must export GET');
    assert.ok(content.includes('export async function POST'), 'Route handler must export POST');
    assert.ok(content.includes('Response.json'), 'Route handler must return standard Response');
  });

  test('6. README proof: README contains proof block and exact file paths', () => {
    const readme = fs.readFileSync(path.join(rootDir, 'README.md'), 'utf-8');
    assert.ok(readme.includes('Next.js App Router'), 'README must mention Built with: Next.js App Router');
    assert.ok(readme.includes('app/layout.jsx'), 'README must list app/layout.jsx');
    assert.ok(readme.includes('app/tasks/page.jsx'), 'README must list app/tasks/page.jsx');
    assert.ok(readme.includes('app/api/tasks/route.js'), 'README must list app/api/tasks/route.js');
  });
});
