"""
Unit tests for HackIndia TypeScript features
"""
import unittest
import os
import subprocess
import sys

class TestTypeScriptFeature(unittest.TestCase):
    def test_ts_files_exist(self):
        self.assertTrue(os.path.exists("tsconfig.json"), "tsconfig.json must exist")
        self.assertTrue(os.path.exists("src-ts/types.ts"), "src-ts/types.ts must exist")
        self.assertTrue(os.path.exists("src-ts/agentService.ts"), "src-ts/agentService.ts must exist")
        self.assertTrue(os.path.exists("src-ts/index.ts"), "src-ts/index.ts must exist")
        self.assertTrue(os.path.exists("verify_typescript.py"), "verify_typescript.py must exist")

    def test_verify_typescript_script(self):
        result = subprocess.run([sys.executable, "verify_typescript.py"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, f"verify_typescript.py failed:\n{result.stdout}\n{result.stderr}")

if __name__ == "__main__":
    unittest.main()
