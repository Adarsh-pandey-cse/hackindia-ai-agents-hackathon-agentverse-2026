"""
Unit tests for HackIndia Safe Sign-In & Authentication features
"""
import unittest
import os
import subprocess
import sys

class TestSafeAuthFeature(unittest.TestCase):
    def test_auth_files_exist(self):
        self.assertTrue(os.path.exists("server/routes/auth.js"), "server/routes/auth.js must exist")
        self.assertTrue(os.path.exists("server/middleware/auth.js"), "server/middleware/auth.js must exist")
        self.assertTrue(os.path.exists("app/api/auth/route.js"), "app/api/auth/route.js must exist")
        self.assertTrue(os.path.exists("verify_safe_signin.py"), "verify_safe_signin.py must exist")

    def test_verify_safe_signin_script(self):
        result = subprocess.run([sys.executable, "verify_safe_signin.py"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, f"verify_safe_signin.py failed:\n{result.stdout}\n{result.stderr}")

if __name__ == "__main__":
    unittest.main()
