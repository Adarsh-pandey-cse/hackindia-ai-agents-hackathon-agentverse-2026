"""
Unit tests for HackIndia Recruiter-Ready GitHub Repo feature
"""
import unittest
import os
import subprocess
import sys

class TestRecruiterReadyRepo(unittest.TestCase):
    def test_repo_files_exist(self):
        self.assertTrue(os.path.exists(".gitignore"), ".gitignore must exist")
        self.assertTrue(os.path.exists("LICENSE"), "LICENSE must exist")
        self.assertTrue(os.path.exists("README.md"), "README.md must exist")
        self.assertTrue(os.path.exists("verify_recruiter_ready_repo.py"), "verify_recruiter_ready_repo.py must exist")

    def test_verify_recruiter_ready_repo_script(self):
        result = subprocess.run([sys.executable, "verify_recruiter_ready_repo.py"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, f"verify_recruiter_ready_repo.py failed:\n{result.stdout}\n{result.stderr}")

if __name__ == "__main__":
    unittest.main()
