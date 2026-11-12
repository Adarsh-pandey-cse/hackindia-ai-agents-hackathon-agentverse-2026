"""
Unit tests for Weekend Full-Stack Repository Architecture
Skill: 'ship-a-weekend-full-stack-repo' (HackIndia 2026)
Developer: Adarsh Pandey (@adarsh-pandey-cse)
"""

import unittest
import os
import json
from verify_full_stack_repo import verify_full_stack_repository

class TestFullStackRepository(unittest.TestCase):
    def setUp(self):
        self.root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def test_frontend_structure(self):
        required_frontend = [
            "src/App.jsx",
            "src/main.jsx",
            "src/components/MetricsBar.jsx",
            "src/components/TaskCard.jsx",
            "src/components/TaskList.jsx",
            "src/components/TaskFilter.jsx",
            "src/components/TaskForm.jsx",
            "vite.config.js",
            "index.html"
        ]
        for f in required_frontend:
            path = os.path.join(self.root_dir, f)
            self.assertTrue(os.path.exists(path), f"Missing frontend component: {f}")

        # Check App.jsx
        app_file = os.path.join(self.root_dir, "src/App.jsx")
        with open(app_file, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("useState", content)
        self.assertIn("useEffect", content)
        self.assertIn("AbortController", content)
        self.assertIn("isLoading", content)
        self.assertIn("errorMessage", content)

    def test_backend_structure(self):
        required_backend = [
            "server/index.js",
            "server/app.js",
            "server/routes/tasks.js",
            "server/routes/agent.js",
            "server/routes/health.js",
            "server/errors/errorHandler.js",
            "server/middleware/logger.js",
            "server/config/env.js"
        ]
        for f in required_backend:
            path = os.path.join(self.root_dir, f)
            self.assertTrue(os.path.exists(path), f"Missing backend component: {f}")

        err_file = os.path.join(self.root_dir, "server/errors/errorHandler.js")
        with open(err_file, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("(err, req, res, next)", content)

    def test_database_and_persistence(self):
        dc_file = os.path.join(self.root_dir, "docker-compose.yml")
        self.assertTrue(os.path.exists(dc_file), "Missing docker-compose.yml")
        with open(dc_file, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("postgres", content.lower())

        chunks_file = os.path.join(self.root_dir, "data/chunks.json")
        self.assertTrue(os.path.exists(chunks_file), "Missing data/chunks.json")

        model_file = os.path.join(self.root_dir, "models/agent_workload_classifier.joblib")
        self.assertTrue(os.path.exists(model_file), "Missing models/agent_workload_classifier.joblib")

    def test_environment_and_secrets(self):
        env_ex = os.path.join(self.root_dir, ".env.example")
        self.assertTrue(os.path.exists(env_ex), "Missing .env.example")
        with open(env_ex, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("PORT=", content)
        self.assertIn("DATABASE_URL=", content)

        git_ign = os.path.join(self.root_dir, ".gitignore")
        self.assertTrue(os.path.exists(git_ign), "Missing .gitignore")
        with open(git_ign, "r", encoding="utf-8") as f:
            ign_content = f.read()
        self.assertIn(".env", ign_content)

    def test_package_scripts_and_docs(self):
        pkg_file = os.path.join(self.root_dir, "package.json")
        with open(pkg_file, "r", encoding="utf-8") as f:
            pkg = json.load(f)
        scripts = pkg.get("scripts", {})
        for s in ["start", "dev", "api", "fullstack", "test", "build", "verify:fullstack"]:
            self.assertIn(s, scripts, f"Missing package script: {s}")

        doc_file = os.path.join(self.root_dir, "docs/FULL_STACK_ARCHITECTURE.md")
        self.assertTrue(os.path.exists(doc_file), "Missing docs/FULL_STACK_ARCHITECTURE.md")

    def test_verify_script_execution(self):
        success = verify_full_stack_repository(self.root_dir)
        self.assertTrue(success, "verify_full_stack_repository() failed")

if __name__ == "__main__":
    unittest.main()
