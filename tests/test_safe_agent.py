"""
Automated Unit Tests for AgentVerse Safe Tool-Calling Agent.
Tests tool schemas, risk classification, argument validation, human approval gates,
call-result loop execution, and hard safety limits.
"""

import unittest
from typing import Dict, Any

from src.tools.schemas import (
    TOOL_SCHEMAS,
    TOOL_MAP,
    is_approval_required,
    get_tool_schema,
    APPROVAL_REQUIRED_TOOLS
)
from src.tools.implementations import (
    search_campus_events,
    get_event_details,
    calculate_reimbursement,
    draft_registration_message
)
from src.agent_loop import SafeToolCallingAgent, AgentLimits


class TestSafeToolCallingAgent(unittest.TestCase):
    """Test suite verifying safety guardrails and tool execution."""

    def test_tool_schemas_structure(self):
        """Verify all tool schemas adhere to HackIndia specification."""
        self.assertGreaterEqual(len(TOOL_SCHEMAS), 4)
        for tool in TOOL_SCHEMAS:
            self.assertIn("name", tool)
            self.assertIn("description", tool)
            self.assertIn("risk", tool)
            self.assertIn(tool["risk"], ("low", "medium", "high"))
            self.assertIn("input_schema", tool)
            self.assertEqual(tool["input_schema"]["type"], "object")
            self.assertIn("properties", tool["input_schema"])
            self.assertIn("required", tool["input_schema"])
            self.assertIn("output_schema", tool)

    def test_risk_tagging_and_approval_requirements(self):
        """Verify mutating tools require approval while safe read tools do not."""
        # Low risk tools must not require approval
        self.assertFalse(is_approval_required("search_campus_events"))
        self.assertFalse(is_approval_required("get_event_details"))
        self.assertFalse(is_approval_required("calculate_reimbursement"))
        self.assertFalse(is_approval_required("draft_registration_message"))

        # High risk tools must require approval
        self.assertTrue(is_approval_required("send_registration_email"))
        self.assertTrue(is_approval_required("update_student_record"))
        self.assertIn("send_registration_email", APPROVAL_REQUIRED_TOOLS)

    def test_argument_validation(self):
        """Verify parameter validation detects missing required fields."""
        agent = SafeToolCallingAgent()
        # Valid arguments
        valid, err = agent.validate_tool_arguments("search_campus_events", {
            "city": "Bengaluru",
            "date": "2026-09-21",
            "topic": "AI",
            "max_results": 5
        })
        self.assertTrue(valid)
        self.assertEqual(err, "")

        # Missing required 'topic'
        invalid, err = agent.validate_tool_arguments("search_campus_events", {
            "city": "Bengaluru",
            "date": "2026-09-21",
            "max_results": 5
        })
        self.assertFalse(invalid)
        self.assertIn("Missing required parameter 'topic'", err)

    def test_tool_implementations(self):
        """Verify tool execution returns expected data structures."""
        # Search
        res = search_campus_events(city="Bengaluru", date="2026-09-21", topic="AI")
        self.assertIn("events", res)
        self.assertGreater(len(res["events"]), 0)

        # Reimbursement calculation with policy cap
        calc = calculate_reimbursement(amounts=[500.0, 1500.0, 2000.0], category="travel")
        self.assertEqual(calc["gross_total"], 4000.0)
        self.assertEqual(calc["approved_total"], 3000.0)  # Capped at ₹3000 for travel
        self.assertTrue(calc["cap_applied"])

    def test_agent_loop_completed_with_auto_approve(self):
        """Verify agent loop runs to completion when approval is granted."""
        agent = SafeToolCallingAgent(auto_approve=True)
        result = agent.run("Find AI events in Bengaluru and draft registration")
        self.assertEqual(result["status"], "COMPLETED")
        self.assertEqual(result["reason"], "finished")
        self.assertIn("answer", result)
        self.assertGreater(result["state"].turns, 0)
        self.assertGreater(result["state"].tool_calls, 0)

    def test_approval_gate_blocks_on_rejection(self):
        """Verify approval gate halts risky tool execution when rejected by supervisor."""
        def reject_all(tool_name: str, args: Dict[str, Any]) -> bool:
            return False

        agent = SafeToolCallingAgent(approval_handler=reject_all)
        result = agent.run("Find AI events in Bengaluru and send registration email")
        self.assertEqual(result["status"], "COMPLETED")

        # Verify that send_registration_email was never executed
        executed_tools = [entry["tool"] for entry in result["state"].audit_log if entry["type"] == "tool_execution"]
        self.assertNotIn("send_registration_email", executed_tools)

        # Verify approval gate rejection was audited
        audit_rejections = [
            entry for entry in result["state"].audit_log
            if entry["type"] == "approval_gate" and not entry["approved"]
        ]
        self.assertGreater(len(audit_rejections), 0)
        self.assertEqual(audit_rejections[0]["tool"], "send_registration_email")

    def test_hard_limit_max_turns(self):
        """Verify agent stops when max turn limit is reached."""
        limits = AgentLimits(max_turns=2, max_tool_calls=10, max_seconds=30.0, max_failures=2)
        agent = SafeToolCallingAgent(limits=limits, auto_approve=True)
        result = agent.run("Find AI events in Bengaluru and draft registration")
        self.assertEqual(result["status"], "STOPPED")
        self.assertEqual(result["reason"], "max_turns")
        self.assertEqual(result["state"].turns, 2)

    def test_hard_limit_max_tool_calls(self):
        """Verify agent stops when tool budget is exhausted."""
        limits = AgentLimits(max_turns=10, max_tool_calls=1, max_seconds=30.0, max_failures=2)
        agent = SafeToolCallingAgent(limits=limits, auto_approve=True)
        result = agent.run("Find AI events in Bengaluru and draft registration")
        self.assertEqual(result["status"], "STOPPED")
        self.assertEqual(result["reason"], "max_tool_calls")
        self.assertEqual(result["state"].tool_calls, 1)

    def test_hard_limit_consecutive_failures(self):
        """Verify agent stops if a tool triggers repeated failures."""
        def failing_tool(**kwargs):
            raise ConnectionError("Simulated remote API outage")

        agent = SafeToolCallingAgent(auto_approve=True)
        agent.tools = dict(agent.tools)
        agent.tools["search_campus_events"] = failing_tool

        limits = AgentLimits(max_turns=10, max_tool_calls=10, max_seconds=30.0, max_failures=1)
        agent.limits = limits

        result = agent.run("Find AI events in Bengaluru")
        self.assertEqual(result["status"], "STOPPED")
        self.assertEqual(result["reason"], "too_many_failures")
        self.assertGreaterEqual(result["state"].failures, 1)


if __name__ == "__main__":
    unittest.main()
