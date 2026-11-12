/**
 * SQL-Backed Feature Automated Test Suite
 * Validates schema, seed data, query patterns, and parameterized query safety.
 * 
 * HackIndia Skill: 'design-sql-backed-features'
 * Developer: Adarsh Pandey (@adarsh-pandey-cse)
 */
import { test, describe } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { query, getTaskById, insertTask } from '../server/db/database.js';

describe('SQL-Backed Feature Architecture Test Suite', () => {
  const rootDir = process.cwd();

  test('1. Schema: db/schema.sql defines tables, primary keys, foreign keys, and indexes', () => {
    assert.ok(fs.existsSync(path.join(rootDir, 'db', 'schema.sql')), 'db/schema.sql missing');
    const schema = fs.readFileSync(path.join(rootDir, 'db', 'schema.sql'), 'utf-8');
    assert.ok(schema.includes('CREATE TABLE'), 'Missing CREATE TABLE');
    assert.ok(schema.includes('PRIMARY KEY'), 'Missing PRIMARY KEY');
    assert.ok(schema.includes('FOREIGN KEY'), 'Missing FOREIGN KEY');
    assert.ok(schema.includes('REFERENCES'), 'Missing REFERENCES');
    assert.ok(schema.includes('CREATE INDEX'), 'Missing CREATE INDEX');
  });

  test('2. Seed: db/seed.sql populates realistic starter data', () => {
    assert.ok(fs.existsSync(path.join(rootDir, 'db', 'seed.sql')), 'db/seed.sql missing');
    const seed = fs.readFileSync(path.join(rootDir, 'db', 'seed.sql'), 'utf-8');
    assert.ok(seed.includes('INSERT INTO'), 'Missing INSERT INTO');
    assert.ok(seed.includes('categories'), 'Missing categories seed');
    assert.ok(seed.includes('tasks'), 'Missing tasks seed');
  });

  test('3. Query Patterns: db/queries.sql demonstrates SELECT, JOIN, GROUP BY', () => {
    assert.ok(fs.existsSync(path.join(rootDir, 'db', 'queries.sql')), 'db/queries.sql missing');
    const queries = fs.readFileSync(path.join(rootDir, 'db', 'queries.sql'), 'utf-8');
    assert.ok(queries.includes('SELECT'), 'Missing SELECT');
    assert.ok(queries.includes('JOIN'), 'Missing JOIN');
    assert.ok(queries.includes('GROUP BY'), 'Missing GROUP BY');
  });

  test('4. SQL Injection Defense: server/db/database.js enforces parameterized inputs', async () => {
    assert.ok(fs.existsSync(path.join(rootDir, 'server', 'db', 'database.js')), 'server/db/database.js missing');
    const res = await getTaskById('TASK-001');
    assert.equal(res.parameterized, true);
    assert.equal(res.paramsCount, 1);
  });
});
