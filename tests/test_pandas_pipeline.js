/**
 * Node.js Unit & Integration Tests for HackIndia Pandas Data Cleaning Pipeline
 */
import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';

test('1. Pandas: Cleaned dataset exists and contains expected columns', () => {
  const csvPath = 'output/cleaned_tasks.csv';
  assert.equal(fs.existsSync(csvPath), true, 'Cleaned CSV must exist');
  const content = fs.readFileSync(csvPath, 'utf-8');
  assert.match(content, /category_name/, 'Cleaned CSV must contain joined category_name');
  assert.match(content, /duration_minutes/, 'Cleaned CSV must contain duration_minutes');
});

test('2. Pandas: Grouped category summary JSON is valid', () => {
  const jsonPath = 'output/category_summary.json';
  assert.equal(fs.existsSync(jsonPath), true, 'Summary JSON must exist');
  const raw = fs.readFileSync(jsonPath, 'utf-8');
  const data = JSON.parse(raw);
  assert.ok(Array.isArray(data), 'Summary data must be an array');
  assert.ok(data.length > 0, 'Summary data must not be empty');
  assert.ok('category_name' in data[0], 'Summary record must contain category_name');
});

test('3. Pandas: Visualization chart exists and has valid size', () => {
  const chartPath = 'output/charts/tasks_by_category.png';
  assert.equal(fs.existsSync(chartPath), true, 'Chart image must exist');
  const stat = fs.statSync(chartPath);
  assert.ok(stat.size > 1000, 'Chart image must be non-empty');
});

test('4. Pandas: Jupyter Notebook exists', () => {
  assert.equal(fs.existsSync('notebooks/clean_data_pipeline.ipynb'), true, 'Jupyter Notebook must exist');
});
