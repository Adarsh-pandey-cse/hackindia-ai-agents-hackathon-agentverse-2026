"""
Unit tests for SQL-Backed Feature Architecture
Skill: 'design-sql-backed-features' (HackIndia 2026)
Developer: Adarsh Pandey (@adarsh-pandey-cse)
"""

import unittest
import os
from verify_sql_feature import verify_sql_feature
from scripts.init_db import initialize_database

class TestSqlFeature(unittest.TestCase):
    def setUp(self):
        self.root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def test_schema_files_exist(self):
        for f in ["db/schema.sql", "db/seed.sql", "db/queries.sql", "server/db/database.js"]:
            self.assertTrue(os.path.exists(os.path.join(self.root_dir, f)), f"Missing file: {f}")

    def test_database_initialization(self):
        self.assertTrue(initialize_database())

    def test_verify_script(self):
        self.assertTrue(verify_sql_feature(self.root_dir))

if __name__ == "__main__":
    unittest.main()
