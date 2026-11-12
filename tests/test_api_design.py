"""
Unit tests for API Design Architecture
Skill: 'design-an-api-teammates-can-use' (HackIndia 2026)
Developer: Adarsh Pandey (@adarsh-pandey-cse)
"""

import unittest
import os
from verify_api_design import verify_api_design

class TestApiDesign(unittest.TestCase):
    def setUp(self):
        self.root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def test_verify_script(self):
        self.assertTrue(verify_api_design(self.root_dir))

if __name__ == "__main__":
    unittest.main()
