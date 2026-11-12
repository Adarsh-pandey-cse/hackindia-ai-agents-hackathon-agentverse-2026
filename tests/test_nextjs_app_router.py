"""
Unit tests for Next.js App Router Architecture
Skill: 'ship-a-nextjs-app-router-project' (HackIndia 2026)
Developer: Adarsh Pandey (@adarsh-pandey-cse)
"""

import unittest
import os
import json
from verify_nextjs_app_router import verify_nextjs_app_router

class TestNextJsAppRouter(unittest.TestCase):
    def setUp(self):
        self.root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def test_dependencies(self):
        pkg_file = os.path.join(self.root_dir, "package.json")
        with open(pkg_file, "r", encoding="utf-8") as f:
            pkg = json.load(f)
        deps = pkg.get("dependencies", {})
        self.assertIn("next", deps)
        self.assertIn("react", deps)
        self.assertIn("react-dom", deps)

    def test_file_based_routes(self):
        for f in ["app/layout.jsx", "app/page.jsx", "app/tasks/page.jsx", "next.config.mjs"]:
            path = os.path.join(self.root_dir, f)
            self.assertTrue(os.path.exists(path), f"Missing file: {f}")

    def test_server_component(self):
        path = os.path.join(self.root_dir, "app/tasks/page.jsx")
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("async", content)
        self.assertIn("await", content)
        self.assertNotIn("'use client'", content)

    def test_client_component(self):
        path = os.path.join(self.root_dir, "app/components/TaskForm.jsx")
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("'use client'", content)
        self.assertIn("useState", content)

    def test_route_handler(self):
        path = os.path.join(self.root_dir, "app/api/tasks/route.js")
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("export async function GET", content)
        self.assertIn("export async function POST", content)

    def test_verification_script(self):
        self.assertTrue(verify_nextjs_app_router(self.root_dir))

if __name__ == "__main__":
    unittest.main()
