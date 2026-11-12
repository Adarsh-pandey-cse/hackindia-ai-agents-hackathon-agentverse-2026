-- ==============================================================================
-- AgentVerse SQL Queries - Demonstrating SQL Core Competencies
-- ==============================================================================

-- Query 1: Basic SELECT with filtering and ordering (Lesson 3)
SELECT id, topic, priority, status, created_at
FROM tasks
WHERE status = 'PENDING'
ORDER BY created_at DESC
LIMIT 10;

-- Query 2: Multi-Table JOIN (Lesson 4)
SELECT 
    t.id AS task_id,
    t.topic,
    t.priority,
    c.name AS category_name,
    u.username AS assigned_operator
FROM tasks t
INNER JOIN categories c ON t.category_id = c.id
LEFT JOIN users u ON t.assigned_to = u.id
ORDER BY t.priority ASC;

-- Query 3: Aggregation and GROUP BY (Lesson 5)
SELECT 
    c.name AS category_name,
    COUNT(t.id) AS total_tasks,
    COUNT(CASE WHEN t.status = 'COMPLETED' THEN 1 END) AS completed_tasks,
    ROUND(AVG(l.duration_ms), 2) AS avg_duration_ms,
    ROUND(AVG(l.prediction_confidence), 4) AS avg_model_confidence
FROM categories c
LEFT JOIN tasks t ON c.id = t.category_id
LEFT JOIN execution_logs l ON t.id = l.task_id
GROUP BY c.id, c.name
HAVING COUNT(t.id) > 0
ORDER BY total_tasks DESC;

-- Query 4: Parameterized Query Template to Stop SQL Injection (Lesson 7)
-- In application code: db.query("SELECT * FROM tasks WHERE id = $1 AND priority = $2", [taskId, priority]);
PREPARE get_safe_task(VARCHAR, VARCHAR) AS
SELECT t.id, t.topic, t.status, c.name AS category
FROM tasks t
JOIN categories c ON t.category_id = c.id
WHERE t.id = $1 AND t.priority = $2;

EXECUTE get_safe_task('TASK-001', 'HIGH');
DEALLOCATE get_safe_task;
