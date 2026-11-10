/**
 * Tasks Resource Routes (CRUD & Query Filtering)
 * Demonstrates request body and query handling, status codes, and error branching.
 */
import { Router } from 'express';
import { validateTaskBody, validateTaskQuery } from '../middleware/validate.js';
import { ApiError } from '../errors/errorHandler.js';

const router = Router();

// In-memory data store with initial sample tasks
let tasks = [
  { id: 'TASK-001', topic: 'Autonomous AI Agents in 2026', category: 'ai_tech_trends', priority: 'HIGH', status: 'COMPLETED', createdAt: '2026-11-08T10:00:00Z' },
  { id: 'TASK-002', topic: 'Cryptocurrency and Web3 Ecosystem Metrics', category: 'market_indicators', priority: 'MEDIUM', status: 'IN_PROGRESS', createdAt: '2026-11-08T10:15:00Z' },
  { id: 'TASK-003', topic: 'Open Source AI Tools & Frameworks', category: 'developer_ecosystem', priority: 'HIGH', status: 'PENDING', createdAt: '2026-11-08T10:30:00Z' },
  { id: 'TASK-004', topic: 'Vector Database Benchmarking and Performance', category: 'ai_tech_trends', priority: 'LOW', status: 'PENDING', createdAt: '2026-11-08T11:00:00Z' },
  { id: 'TASK-005', topic: 'Containerized Deployment with Docker and Kubernetes', category: 'developer_ecosystem', priority: 'MEDIUM', status: 'COMPLETED', createdAt: '2026-11-08T11:30:00Z' },
];

/**
 * GET /api/v1/tasks
 * Supports query params: ?priority=HIGH&search=agents&limit=10&page=1
 */
router.get('/', validateTaskQuery, (req, res) => {
  const { priority, search, limit = '20', page = '1' } = req.query;
  let filtered = [...tasks];

  if (priority) {
    filtered = filtered.filter(t => t.priority === priority.toUpperCase());
  }

  if (search) {
    const term = search.toLowerCase();
    filtered = filtered.filter(t =>
      t.topic.toLowerCase().includes(term) ||
      t.category.toLowerCase().includes(term) ||
      t.id.toLowerCase().includes(term)
    );
  }

  const numLimit = Math.min(100, Math.max(1, parseInt(limit, 10)));
  const numPage = Math.max(1, parseInt(page, 10));
  const total = filtered.length;
  const startIndex = (numPage - 1) * numLimit;
  const paginatedTasks = filtered.slice(startIndex, startIndex + numLimit);

  res.status(200).json({
    success: true,
    data: paginatedTasks,
    pagination: {
      total,
      page: numPage,
      limit: numLimit,
      totalPages: Math.ceil(total / numLimit) || 1,
    }
  });
});

/**
 * GET /api/v1/tasks/:id
 * Retrieve a specific task by unique identifier
 */
router.get('/:id', (req, res, next) => {
  const { id } = req.params;
  const task = tasks.find(t => t.id.toLowerCase() === id.toLowerCase());

  if (!task) {
    return next(ApiError.notFound(`Task with ID '${id}' not found`));
  }

  res.status(200).json({
    success: true,
    data: task
  });
});

/**
 * POST /api/v1/tasks
 * Create a new task with validated body
 */
router.post('/', validateTaskBody, (req, res, next) => {
  const { id, topic, category, priority } = req.body;
  const taskId = id || `TASK-${String(tasks.length + 1).padStart(3, '0')}`;

  // Check duplicate ID
  if (tasks.some(t => t.id.toLowerCase() === taskId.toLowerCase())) {
    return next(ApiError.badRequest(`Task with ID '${taskId}' already exists`));
  }

  const newTask = {
    id: taskId,
    topic: topic.trim(),
    category: category.trim(),
    priority,
    status: 'PENDING',
    createdAt: new Date().toISOString(),
  };

  tasks.unshift(newTask);

  res.status(201).json({
    success: true,
    message: 'Task successfully created',
    data: newTask
  });
});

/**
 * PUT /api/v1/tasks/:id
 * Update an existing task
 */
router.put('/:id', (req, res, next) => {
  const { id } = req.params;
  const index = tasks.findIndex(t => t.id.toLowerCase() === id.toLowerCase());

  if (index === -1) {
    return next(ApiError.notFound(`Task with ID '${id}' not found`));
  }

  const { topic, category, priority, status } = req.body;
  tasks[index] = {
    ...tasks[index],
    ...(topic ? { topic: topic.trim() } : {}),
    ...(category ? { category: category.trim() } : {}),
    ...(priority ? { priority: priority.toUpperCase() } : {}),
    ...(status ? { status: status.toUpperCase() } : {}),
    updatedAt: new Date().toISOString(),
  };

  res.status(200).json({
    success: true,
    message: 'Task updated successfully',
    data: tasks[index]
  });
});

/**
 * DELETE /api/v1/tasks/:id
 * Delete a task - returns 204 No Content
 */
router.delete('/:id', (req, res, next) => {
  const { id } = req.params;
  const index = tasks.findIndex(t => t.id.toLowerCase() === id.toLowerCase());

  if (index === -1) {
    return next(ApiError.notFound(`Task with ID '${id}' not found`));
  }

  tasks.splice(index, 1);
  res.status(204).send();
});

export default router;
