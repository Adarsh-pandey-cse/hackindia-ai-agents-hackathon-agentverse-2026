/**
 * React 18 & Vite Architecture Automated Test Suite
 * Validates readable components, props, useState, controlled forms,
 * stable keys, lifted state, and justified useEffect.
 * Skill: 'Build readable React apps' (HackIndia 2026)
 */
import { test, describe } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';

describe('React 18 & Vite Architecture Test Suite', () => {
  const rootDir = process.cwd();

  test('package.json includes react, react-dom, and vite dependencies', () => {
    const pkg = JSON.parse(fs.readFileSync(path.join(rootDir, 'package.json'), 'utf-8'));
    assert.ok(pkg.dependencies.react, 'react dependency missing');
    assert.ok(pkg.dependencies['react-dom'], 'react-dom dependency missing');
    assert.ok(pkg.dependencies.vite || pkg.devDependencies?.vite, 'vite dependency missing');
  });

  test('Vite configuration and root index.html exist', () => {
    assert.ok(fs.existsSync(path.join(rootDir, 'vite.config.js')), 'vite.config.js missing');
    assert.ok(fs.existsSync(path.join(rootDir, 'index.html')), 'index.html missing');

    const htmlContent = fs.readFileSync(path.join(rootDir, 'index.html'), 'utf-8');
    assert.ok(htmlContent.includes('src/main.jsx'), 'index.html must reference src/main.jsx');
    assert.ok(htmlContent.includes('id="root"'), 'index.html must contain root mount element');
  });

  test('All required *.jsx component files exist', () => {
    const requiredJsxFiles = [
      'src/main.jsx',
      'src/App.jsx',
      'src/components/MetricsBar.jsx',
      'src/components/TaskCard.jsx',
      'src/components/TaskList.jsx',
      'src/components/TaskFilter.jsx',
      'src/components/TaskForm.jsx'
    ];

    for (const relPath of requiredJsxFiles) {
      assert.ok(fs.existsSync(path.join(rootDir, relPath)), `Missing component: ${relPath}`);
    }
  });

  test('App.jsx implements useState, lifted state, and justified useEffect with cleanup', () => {
    const appContent = fs.readFileSync(path.join(rootDir, 'src', 'App.jsx'), 'utf-8');
    assert.ok(appContent.includes('useState'), 'App.jsx must use useState');
    assert.ok(appContent.includes('useEffect'), 'App.jsx must use useEffect');
    assert.ok(appContent.includes('AbortController'), 'useEffect must use AbortController for clean teardown');
    assert.ok(appContent.includes('controller.abort()'), 'useEffect must include cleanup function aborting request');
    assert.ok(appContent.includes('handleAddTask'), 'App.jsx must define lifted state handler for adding tasks');
    assert.ok(appContent.includes('handleStatusToggle'), 'App.jsx must define lifted state handler for updating tasks');
    assert.ok(appContent.includes('handleDelete'), 'App.jsx must define lifted state handler for deleting tasks');
  });

  test('TaskList.jsx enforces stable keys (task.id) rather than fragile array indices', () => {
    const listContent = fs.readFileSync(path.join(rootDir, 'src', 'components', 'TaskList.jsx'), 'utf-8');
    assert.ok(listContent.includes('key={task.id}'), 'TaskList must use key={task.id} for stable reconciliation');
    assert.ok(!listContent.includes('key={index}'), 'TaskList must not use fragile array index as key');
  });

  test('TaskForm.jsx implements a controlled form with local useState and onSubmit', () => {
    const formContent = fs.readFileSync(path.join(rootDir, 'src', 'components', 'TaskForm.jsx'), 'utf-8');
    assert.ok(formContent.includes('useState'), 'TaskForm must manage controlled form state with useState');
    assert.ok(formContent.includes('value={topic}'), 'TaskForm must bind topic input value');
    assert.ok(formContent.includes('onChange='), 'TaskForm must bind onChange handlers');
    assert.ok(formContent.includes('onSubmit={handleSubmit}'), 'TaskForm must bind onSubmit handler');
  });

  test('TaskFilter.jsx implements controlled inputs driven by lifted props', () => {
    const filterContent = fs.readFileSync(path.join(rootDir, 'src', 'components', 'TaskFilter.jsx'), 'utf-8');
    assert.ok(filterContent.includes('value={searchQuery}'), 'TaskFilter must bind value={searchQuery}');
    assert.ok(filterContent.includes('value={priorityFilter}'), 'TaskFilter must bind value={priorityFilter}');
    assert.ok(filterContent.includes('onSearchChange'), 'TaskFilter must call onSearchChange prop');
    assert.ok(filterContent.includes('onPriorityChange'), 'TaskFilter must call onPriorityChange prop');
  });

  test('Production build (dist/) generates optimized bundle without errors', () => {
    assert.ok(fs.existsSync(path.join(rootDir, 'dist', 'index.html')), 'dist/index.html missing from build');
    const builtHtml = fs.readFileSync(path.join(rootDir, 'dist', 'index.html'), 'utf-8');
    assert.ok(builtHtml.includes('assets/'), 'dist/index.html must reference compiled assets');
  });
});
