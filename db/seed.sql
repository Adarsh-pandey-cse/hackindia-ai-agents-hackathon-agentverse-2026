-- ==============================================================================
-- AgentVerse Database Seed Data
-- ==============================================================================

-- 1. Insert Categories
INSERT INTO categories (id, slug, name, description) VALUES
    (1, 'ai_tech_trends', 'AI Tech Trends', 'Deep learning, autonomous agent architectures, and LLM frameworks'),
    (2, 'market_indicators', 'Market Indicators', 'Web3 metrics, cryptocurrency volumes, and decentralized finance'),
    (3, 'developer_ecosystem', 'Developer Ecosystem', 'Developer tooling, package ecosystems, and CI/CD pipelines')
ON CONFLICT (id) DO NOTHING;

-- 2. Insert Users
INSERT INTO users (id, username, email, role) VALUES
    (1, 'adarsh', 'adarshpandey.cse@gmail.com', 'ADMIN'),
    (2, 'agent_worker_1', 'worker1@agentverse.internal', 'OPERATOR'),
    (3, 'audit_viewer', 'audit@agentverse.internal', 'VIEWER')
ON CONFLICT (id) DO NOTHING;

-- 3. Insert Tasks
INSERT INTO tasks (id, topic, category_id, priority, status, assigned_to) VALUES
    ('TASK-001', 'Autonomous AI Agents in 2026', 1, 'HIGH', 'COMPLETED', 1),
    ('TASK-002', 'Cryptocurrency and Web3 Ecosystem Metrics', 2, 'MEDIUM', 'IN_PROGRESS', 2),
    ('TASK-003', 'Open Source AI Tools & Frameworks', 3, 'HIGH', 'PENDING', 2),
    ('TASK-004', 'Vector Database Benchmarking and Performance', 1, 'LOW', 'PENDING', 1),
    ('TASK-005', 'Containerized Deployment with Docker and Kubernetes', 3, 'MEDIUM', 'COMPLETED', 1)
ON CONFLICT (id) DO NOTHING;

-- 4. Insert Execution Logs
INSERT INTO execution_logs (task_id, duration_ms, prediction_confidence, predicted_success) VALUES
    ('TASK-001', 879, 0.9625, TRUE),
    ('TASK-001', 842, 0.9710, TRUE),
    ('TASK-002', 1240, 0.8840, TRUE),
    ('TASK-005', 915, 0.9520, TRUE)
ON CONFLICT DO NOTHING;
