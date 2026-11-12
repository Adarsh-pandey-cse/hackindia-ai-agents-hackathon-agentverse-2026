#!/bin/sh
# Smoke test script for AgentVerse REST API
# HackIndia Skill: design-an-api-teammates-can-use

BASE_URL=${BASE_URL:-http://localhost:3000/api/v1}
HEALTH_URL=${HEALTH_URL:-http://localhost:3000/health}

echo "=========================================="
echo "AgentVerse API Smoke Test"
echo "=========================================="

echo "\n1. Checking Server Health..."
curl -s -i "$HEALTH_URL"

echo "\n\n2. Listing Tasks with Pagination & Filtering..."
curl -s -i "$BASE_URL/tasks?page=1&limit=5&priority=HIGH"

echo "\n\n3. Creating a Workload..."
curl -s -i -X POST "$BASE_URL/tasks" \
  -H "Content-Type: application/json" \
  -d '{"topic":"Autonomous Smoke Verification","priority":"HIGH","category":"ai_tech_trends"}'

echo "\n\n4. Triggering 400 Validation Error..."
curl -s -i -X POST "$BASE_URL/tasks" \
  -H "Content-Type: application/json" \
  -d '{}'

echo "\n\nSmoke test finished."
