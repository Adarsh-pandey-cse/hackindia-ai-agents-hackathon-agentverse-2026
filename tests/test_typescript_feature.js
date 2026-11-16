/**
 * Node.js Unit & Integration Tests for HackIndia TypeScript Feature
 * Validates compiled TypeScript modules, type guards, and service pipelines.
 */
import test from 'node:test';
import assert from 'node:assert/strict';
import {
  isTaskItem,
  isValidPriority,
  filterByPriority,
  handleAgentAction,
} from '../dist-ts/agentService.js';
import { runTypedAgentDemo } from '../dist-ts/index.js';

test('1. TypeScript: Custom Type Guard validates TaskItem objects', () => {
  const validTask = {
    id: 'TS-001',
    topic: 'Static Type Checking',
    category: 'engineering',
    priority: 'HIGH',
    status: 'PENDING',
    createdAt: new Date().toISOString(),
  };

  assert.equal(isTaskItem(validTask), true, 'Valid task object must satisfy isTaskItem');
  assert.equal(isTaskItem(null), false, 'null must return false');
  assert.equal(isTaskItem({}), false, 'empty object must return false');
  assert.equal(isTaskItem({ id: 'TS-002', priority: 'INVALID' }), false, 'invalid priority must return false');
});

test('2. TypeScript: Priority union type guard checks allowed values', () => {
  assert.equal(isValidPriority('HIGH'), true);
  assert.equal(isValidPriority('MEDIUM'), true);
  assert.equal(isValidPriority('LOW'), true);
  assert.equal(isValidPriority('CRITICAL'), false);
  assert.equal(isValidPriority(123), false);
});

test('3. TypeScript: Generic filter preserves collection types', () => {
  const tasks = [
    { id: '1', topic: 'A', category: 'cat', priority: 'HIGH', status: 'PENDING', createdAt: '2026-01-01' },
    { id: '2', topic: 'B', category: 'cat', priority: 'LOW', status: 'PENDING', createdAt: '2026-01-01' },
    { id: '3', topic: 'C', category: 'cat', priority: 'HIGH', status: 'PENDING', createdAt: '2026-01-01' },
  ];

  const high = filterByPriority(tasks, 'HIGH');
  assert.equal(high.length, 2);
  assert.equal(high[0].id, '1');
  assert.equal(high[1].id, '3');
});

test('4. TypeScript: Discriminated union narrows action types safely', () => {
  const analyzeMsg = handleAgentAction({
    type: 'ANALYZE',
    payload: { query: 'test query', limit: 10 },
  });
  assert.match(analyzeMsg, /Analyzing query/);

  const executeMsg = handleAgentAction({
    type: 'EXECUTE',
    payload: { taskId: 'TASK-123', dryRun: true },
  });
  assert.match(executeMsg, /Executing task TASK-123/);
});

test('5. TypeScript: End-to-end pipeline execution runs smoothly', async () => {
  const result = await runTypedAgentDemo();
  assert.equal(result.validCount, 2, '2 of 3 tasks in sample must be valid');
  assert.equal(result.highPriorityCount, 1, '1 task must be HIGH priority');
  assert.ok(result.actionMessage.length > 0);
});
