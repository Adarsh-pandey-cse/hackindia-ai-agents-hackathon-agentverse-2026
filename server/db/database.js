/**
 * Safe Database Query Layer
 * Demonstrates parameterized queries to prevent SQL injection (Lesson 7)
 * HackIndia Skill: design-sql-backed-features
 */

import config from '../config/env.js';

/**
 * Mock/Live database client using parameterized inputs.
 * NEVER concatenates user inputs directly into SQL strings.
 */
export async function query(sqlText, params = []) {
  // Validate parameters is an array to enforce parameterized queries
  if (!Array.isArray(params)) {
    throw new Error('Database query params must be passed as an array to prevent SQL injection.');
  }

  // Parameterized Query Execution Log
  const sanitizedLog = sqlText.replace(/\s+/g, ' ').trim();
  
  // In production, delegates to pg.Pool:
  // return await pool.query(sqlText, params);
  
  return {
    rows: [],
    rowCount: 0,
    command: sqlText.split(' ')[0],
    parameterized: true,
    paramsCount: params.length,
  };
}

/**
 * Safe task lookup using parameterized query
 */
export async function getTaskById(taskId) {
  // Parameterized $1 stops SQL injection attacks like "' OR 1=1 --"
  const sql = `
    SELECT t.id, t.topic, t.priority, t.status, c.name AS category_name
    FROM tasks t
    INNER JOIN categories c ON t.category_id = c.id
    WHERE t.id = $1
  `;
  return await query(sql, [taskId]);
}

/**
 * Safe task creation using parameterized query
 */
export async function insertTask({ id, topic, categoryId, priority }) {
  const sql = `
    INSERT INTO tasks (id, topic, category_id, priority, status)
    VALUES ($1, $2, $3, $4, 'PENDING')
    RETURNING id, topic, priority, status
  `;
  return await query(sql, [id, topic, categoryId, priority]);
}

export default { query, getTaskById, insertTask };
