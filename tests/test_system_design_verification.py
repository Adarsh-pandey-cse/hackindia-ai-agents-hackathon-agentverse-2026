"""
Unit Tests for System Design Verification & Submission Tool.
Skill: 'Design systems you can defend' (HackIndia 2026)
Run via: python -m unittest discover tests
"""

import unittest
import verify_system_design


class TestSystemDesignVerification(unittest.TestCase):
    """Test suite for system design verification script."""

    def test_check_working_app(self):
        """Verify all core application entry points exist."""
        passed, msg = verify_system_design.check_working_app()
        self.assertTrue(passed, msg)
        self.assertIn("validated", msg)

    def test_check_system_design_docs(self):
        """Verify docs/SYSTEM_DESIGN.md and README.md satisfy rubric requirements."""
        passed, msg = verify_system_design.check_system_design_docs()
        self.assertTrue(passed, msg)
        self.assertIn("5 architectural layers", msg)

    def test_check_git_status(self):
        """Verify git status detection."""
        passed, msg = verify_system_design.check_git_status()
        self.assertTrue(passed, msg)

    def test_check_link_reachability(self):
        """Verify public repository reachability."""
        passed, msg = verify_system_design.check_link_reachability()
        self.assertTrue(passed, msg)

    def test_get_submission_payload(self):
        """Verify submission payload contains all required attributes."""
        payload = verify_system_design.get_submission_payload()
        self.assertEqual(payload["slug"], "design-systems-you-can-defend")
        self.assertTrue(payload["verified"])
        self.assertIn("evidenceUrl", payload)
        self.assertIn("evidenceLabel", payload)
        self.assertIn("instruction", payload)
        self.assertIn("mirrors", payload)


if __name__ == "__main__":
    unittest.main()
