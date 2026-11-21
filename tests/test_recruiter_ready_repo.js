/**
 * Node.js Unit & Integration Tests for HackIndia Recruiter-Ready GitHub Repo
 */
import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import { execSync } from 'node:child_process';

test('1. Git & GitHub: Commit history contains conventional commits', () => {
  const log = execSync('git log --oneline -n 10', { encoding: 'utf-8' });
  const lines = log.split('\n').filter(Boolean);
  assert.ok(lines.length >= 5, 'Must have at least 5 commits');
  const hasConventional = lines.some((l) => /^(?:[a-f0-9]+)\s+(feat|fix|docs|chore|refactor|test):/i.test(l));
  assert.equal(hasConventional, true, 'Commits must follow Conventional Commits standard');
});

test('2. Git & GitHub: .gitignore exists and ignores secrets and dependencies', () => {
  assert.equal(fs.existsSync('.gitignore'), true, '.gitignore must exist');
  const gitignore = fs.readFileSync('.gitignore', 'utf-8');
  assert.match(gitignore, /node_modules/, '.gitignore must ignore node_modules');
  assert.match(gitignore, /\.env/, '.gitignore must ignore .env files');
});

test('3. Git & GitHub: LICENSE file is present and valid', () => {
  assert.equal(fs.existsSync('LICENSE'), true, 'LICENSE file must exist');
  const license = fs.readFileSync('LICENSE', 'utf-8');
  assert.match(license, /MIT|License/i, 'LICENSE must be an open-source license');
});

test('4. Git & GitHub: README contains setup, run, and architecture documentation', () => {
  assert.equal(fs.existsSync('README.md'), true, 'README.md must exist');
  const readme = fs.readFileSync('README.md', 'utf-8');
  assert.match(readme, /git clone/i, 'README must explain how to clone the repo');
  assert.match(readme, /npm|python/i, 'README must explain how to run the repo');
});
