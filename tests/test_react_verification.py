"""
Unit Tests for React 18 & Vite App Verification & Submission Tool.
Skill: 'Build readable React apps' (HackIndia 2026)
Run via: python -m unittest discover tests
"""

import unittest
import verify_react_app


class TestReactAppVerification(unittest.TestCase):
    """Test suite for React app verification script."""

    def test_check_react_dependencies(self):
        """Verify react, react-dom, and vite exist in package.json."""
        passed, msg = verify_react_app.check_react_dependencies()
        self.assertTrue(passed, msg)
        self.assertIn("react", msg)

    def test_check_jsx_components(self):
        """Verify presence of *.jsx components and Vite config."""
        passed, msg = verify_react_app.check_jsx_components()
        self.assertTrue(passed, msg)
        self.assertIn("9/9", msg)

    def test_check_react_concepts(self):
        """Verify useState, controlled forms, stable keys, and useEffect."""
        passed, msg = verify_react_app.check_react_concepts()
        self.assertTrue(passed, msg)

    def test_check_automated_tests(self):
        """Verify node --test tests/test_react_app.js passes."""
        passed, msg = verify_react_app.check_automated_tests()
        self.assertTrue(passed, msg)
        self.assertIn("PASSED", msg)

    def test_check_link_reachability(self):
        """Verify repository URL reachability."""
        passed, msg = verify_react_app.check_link_reachability()
        self.assertTrue(passed, msg)

    def test_get_submission_payload(self):
        """Verify submission payload fields."""
        payload = verify_react_app.get_submission_payload()
        self.assertEqual(payload["slug"], "build-readable-react-apps")
        self.assertTrue(payload["verified"])
        self.assertEqual(payload["framework"], "React 18")
        self.assertEqual(payload["buildTool"], "Vite 5")
        self.assertIn("evidenceUrl", payload)
        self.assertIn("evidenceLabel", payload)


if __name__ == "__main__":
    unittest.main()
