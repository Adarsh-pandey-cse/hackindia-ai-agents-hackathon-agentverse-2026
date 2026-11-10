"""
Unit Tests for Express 5 API Verification & Submission Tool.
Skill: 'Build a Recruiter-Ready Express API' (HackIndia 2026)
Run via: python -m unittest discover tests
"""

import unittest
import verify_express_api


class TestExpressApiVerification(unittest.TestCase):
    """Test suite for Express 5 API verification script."""

    def test_check_node_and_express(self):
        """Verify Node.js runtime and Express 5 framework."""
        passed, msg = verify_express_api.check_node_and_express()
        self.assertTrue(passed, msg)
        self.assertIn("Node.js 24 LTS", msg)

    def test_check_project_structure(self):
        """Verify all server directory components exist."""
        passed, msg = verify_express_api.check_project_structure()
        self.assertTrue(passed, msg)
        self.assertIn("11/11", msg)

    def test_check_error_handling_and_status_codes(self):
        """Verify 4-argument error handler and status codes."""
        passed, msg = verify_express_api.check_error_handling_and_status_codes()
        self.assertTrue(passed, msg)

    def test_check_automated_tests(self):
        """Verify that Node express tests pass."""
        passed, msg = verify_express_api.check_automated_tests()
        self.assertTrue(passed, msg)
        self.assertIn("PASSED", msg)

    def test_check_link_reachability(self):
        """Verify repository URL reachability."""
        passed, msg = verify_express_api.check_link_reachability()
        self.assertTrue(passed, msg)

    def test_get_submission_payload(self):
        """Verify submission payload fields."""
        payload = verify_express_api.get_submission_payload()
        self.assertEqual(payload["slug"], "build-a-recruiter-ready-express-api")
        self.assertTrue(payload["verified"])
        self.assertIn("evidenceUrl", payload)
        self.assertIn("evidenceLabel", payload)
        self.assertEqual(payload["runtime"], "Node.js 24 LTS")
        self.assertEqual(payload["framework"], "Express 5")


if __name__ == "__main__":
    unittest.main()
