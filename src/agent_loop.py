"""
AgentVerse Safe Tool-Calling Agent Loop (src/agent_loop.py)
Implements the core call-result loop, schema validation, human approval gates,
and hard safety limits (max turns, tool call budget, timeout, failure stops).
"""

import os
import re
import time
import json
from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional, Callable, Tuple

from .tools.schemas import TOOL_SCHEMAS, TOOL_MAP, is_approval_required
from .tools.implementations import TOOL_RUNNERS


@dataclass
class AgentLimits:
    """Hard safety boundaries governing agent loop execution."""
    max_turns: int = 8
    max_tool_calls: int = 12
    max_seconds: float = 30.0
    max_failures: int = 2


@dataclass
class AgentState:
    """Execution state tracking turns, budgets, and conversation history."""
    turns: int = 0
    tool_calls: int = 0
    failures: int = 0
    consecutive_failures: int = 0
    started_at: float = field(default_factory=time.time)
    messages: List[Dict[str, Any]] = field(default_factory=list)
    audit_log: List[Dict[str, Any]] = field(default_factory=list)


class SafeToolCallingAgent:
    """
    Robust Autonomous Agent implementing explicit tool-calling contracts,
    interactive human-in-the-loop approvals, and hard stop guardrails.
    """

    def __init__(self,
                 limits: Optional[AgentLimits] = None,
                 approval_handler: Optional[Callable[[str, Dict[str, Any]], bool]] = None,
                 auto_approve: bool = False,
                 mock_mode: bool = True):
        self.limits = limits or AgentLimits()
        self.approval_handler = approval_handler
        self.auto_approve = auto_approve
        self.mock_mode = mock_mode
        self.tools = TOOL_RUNNERS

    def default_cli_approval(self, tool_name: str, args: Dict[str, Any]) -> bool:
        """Interactive CLI prompt for human approval gate."""
        if self.auto_approve:
            return True
        print("\n" + "=" * 60)
        print(" [HUMAN APPROVAL GATE TRIGGERED]")
        print(f" Tool:      {tool_name} (HIGH RISK ACTION)")
        print(f" Arguments: {json.dumps(args, indent=2)}")
        print("=" * 60)
        try:
            choice = input("Type 'approve' to execute or 'reject' to deny: ").strip().lower()
            return choice == "approve"
        except (KeyboardInterrupt, EOFError):
            print("\nRejected by user interruption.")
            return False

    def validate_tool_arguments(self, tool_name: str, args: Dict[str, Any]) -> Tuple[bool, str]:
        """Validate input arguments against tool schema required fields."""
        if tool_name not in TOOL_MAP:
            return False, f"Unknown tool: '{tool_name}'"

        schema = TOOL_MAP[tool_name]["input_schema"]
        required = schema.get("required", [])
        for field_name in required:
            if field_name not in args:
                return False, f"Missing required parameter '{field_name}' for tool '{tool_name}'"

        return True, ""

    def simulate_model_planning(self, messages: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Deterministic mock model planner for reproducible hackathon execution and testing.
        Analyzes conversation context and decides next tool call or final response.
        """
        user_message = ""
        for m in messages:
            if m["role"] == "user":
                user_message = m["content"]

        tool_messages = [m for m in messages if m["role"] == "tool"]

        # Step 1: No tools called yet -> decide first tool based on user intent
        if not tool_messages:
            q_lower = user_message.lower()
            if "reimbursement" in q_lower or "expense" in q_lower or "bill" in q_lower:
                # Extract any numbers from query or use defaults
                numbers = [float(x) for x in re.findall(r'\b\d+(?:\.\d+)?\b', user_message)]
                amounts = numbers if numbers else [350.0, 1200.0, 800.0]
                return {
                    "tool_calls": [
                        {
                            "id": "call_reimb_1",
                            "name": "calculate_reimbursement",
                            "arguments": {"amounts": amounts, "category": "travel"}
                        }
                    ],
                    "content": "I will calculate your reimbursement total first."
                }
            else:
                # Default to searching campus events
                topic = "AI" if "ai" in q_lower else ("web3" if "web" in q_lower else "design")
                city = "Bengaluru" if "bengaluru" in q_lower or "bangalore" in q_lower else "Delhi"
                return {
                    "tool_calls": [
                        {
                            "id": "call_search_1",
                            "name": "search_campus_events",
                            "arguments": {
                                "city": city,
                                "date": "2026-09-21",
                                "topic": topic,
                                "max_results": 3
                            }
                        }
                    ],
                    "content": f"Searching for campus events in {city} on {topic}..."
                }

        # Step 2: Handle results of search or calculation
        last_tool = tool_messages[-1]
        last_tool_name = last_tool.get("name")
        last_content = json.loads(last_tool.get("content", "{}"))

        if last_tool_name == "search_campus_events":
            events = last_content.get("result", {}).get("events", [])
            if events:
                top_event_id = events[0]["id"]
                return {
                    "tool_calls": [
                        {
                            "id": "call_details_1",
                            "name": "get_event_details",
                            "arguments": {"event_id": top_event_id}
                        }
                    ],
                    "content": f"Found event {top_event_id}. Fetching specific rules and deadlines..."
                }
            return {"content": "No matching campus events found for the requested criteria.", "tool_calls": []}

        if last_tool_name == "get_event_details":
            ev_id = last_content.get("result", {}).get("event_id", "EVT-AI-101")
            return {
                "tool_calls": [
                    {
                        "id": "call_draft_1",
                        "name": "draft_registration_message",
                        "arguments": {
                            "student_name": "Adarsh Pandey",
                            "event_id": ev_id,
                            "roll_number": "CS2026-881"
                        }
                    }
                ],
                "content": "Drafting registration message for student review..."
            }

        if last_tool_name == "draft_registration_message":
            # Attempt gated email dispatch (requires human approval)
            draft_text = last_content.get("result", {}).get("draft", "")
            return {
                "tool_calls": [
                    {
                        "id": "call_email_1",
                        "name": "send_registration_email",
                        "arguments": {
                            "recipient": "cse_events@campus.edu.in",
                            "subject": "Event Registration Request: EVT-AI-101",
                            "body": draft_text
                        }
                    }
                ],
                "content": "Draft created. Requesting approval to dispatch registration email..."
            }

        if last_tool_name == "calculate_reimbursement":
            reimb = last_content.get("result", {})
            return {
                "tool_calls": [
                    {
                        "id": "call_update_1",
                        "name": "update_student_record",
                        "arguments": {
                            "student_id": "STU-2026-90",
                            "field": "reimbursement_claim",
                            "value": f"INR {reimb.get('approved_total', 0.0)}"
                        }
                    }
                ],
                "content": f"Calculated approved reimbursement: INR {reimb.get('approved_total')}. Requesting approval to commit record to database..."
            }

        # Step 3: Handle gated tool response (approval or rejection)
        if last_tool_name in ("send_registration_email", "update_student_record"):
            if last_content.get("ok"):
                return {
                    "content": f"Action completed successfully! Output: {last_content.get('result')}. All workflow steps finished.",
                    "tool_calls": []
                }
            else:
                return {
                    "content": f"The high-risk operation '{last_tool_name}' was rejected by the human supervisor. Stopping safely without making unauthorized state modifications.",
                    "tool_calls": []
                }

        return {"content": "Workflow completed.", "tool_calls": []}

    def execute_tool_call(self, tool_call: Dict[str, Any], state: AgentState) -> Dict[str, Any]:
        """
        Execute a single tool call with parameter validation and human approval gate.
        """
        tool_name = tool_call["name"]
        args = tool_call.get("arguments", {})

        # 1. Parameter Validation
        valid, err_msg = self.validate_tool_arguments(tool_name, args)
        if not valid:
            state.failures += 1
            state.consecutive_failures += 1
            return {
                "ok": False,
                "error": err_msg,
                "tool": tool_name
            }

        # 2. Human Approval Gate
        if is_approval_required(tool_name):
            approval_fn = self.approval_handler or self.default_cli_approval
            approved = approval_fn(tool_name, args)
            state.audit_log.append({
                "type": "approval_gate",
                "tool": tool_name,
                "approved": approved,
                "arguments": args,
                "timestamp": time.time()
            })

            if not approved:
                return {
                    "ok": False,
                    "error": "Human supervisor rejected this tool call",
                    "tool": tool_name,
                    "rejected": True
                }

        # 3. Execution
        try:
            runner = self.tools[tool_name]
            result = runner(**args)
            state.consecutive_failures = 0
            state.audit_log.append({
                "type": "tool_execution",
                "tool": tool_name,
                "ok": True,
                "result": result,
                "timestamp": time.time()
            })
            return {"ok": True, "result": result, "tool": tool_name}
        except Exception as e:
            state.failures += 1
            state.consecutive_failures += 1
            state.audit_log.append({
                "type": "tool_execution",
                "tool": tool_name,
                "ok": False,
                "error": str(e),
                "timestamp": time.time()
            })
            return {"ok": False, "error": str(e), "tool": tool_name}

    def run(self, user_goal: str) -> Dict[str, Any]:
        """
        Execute the call-result agent loop until completion or hard limit trigger.
        """
        state = AgentState(messages=[{"role": "user", "content": user_goal}])

        while True:
            # 1. Hard Safety Limit Checks
            if state.turns >= self.limits.max_turns:
                return {
                    "status": "STOPPED",
                    "reason": "max_turns",
                    "message": f"Agent reached maximum turn limit ({self.limits.max_turns}).",
                    "state": state
                }

            if state.tool_calls >= self.limits.max_tool_calls:
                return {
                    "status": "STOPPED",
                    "reason": "max_tool_calls",
                    "message": f"Agent reached maximum tool call budget ({self.limits.max_tool_calls}).",
                    "state": state
                }

            elapsed = time.time() - state.started_at
            if elapsed >= self.limits.max_seconds:
                return {
                    "status": "STOPPED",
                    "reason": "timeout",
                    "message": f"Agent exceeded maximum execution time ({self.limits.max_seconds}s).",
                    "state": state
                }

            if state.consecutive_failures >= self.limits.max_failures:
                return {
                    "status": "STOPPED",
                    "reason": "too_many_failures",
                    "message": f"Agent stopped due to {state.consecutive_failures} consecutive tool failures.",
                    "state": state
                }

            # 2. Advance turn
            state.turns += 1

            # 3. Model Planning Step
            model_response = self.simulate_model_planning(state.messages)
            state.messages.append({
                "role": "assistant",
                "content": model_response.get("content", ""),
                "tool_calls": model_response.get("tool_calls", [])
            })

            tool_calls = model_response.get("tool_calls", [])

            # 4. Completion check: No further tool calls requested
            if not tool_calls:
                return {
                    "status": "COMPLETED",
                    "reason": "finished",
                    "answer": model_response.get("content", ""),
                    "state": state
                }

            # 5. Process tool calls
            for call in tool_calls:
                if state.tool_calls >= self.limits.max_tool_calls:
                    return {
                        "status": "STOPPED",
                        "reason": "max_tool_calls",
                        "message": "Tool budget reached mid-turn.",
                        "state": state
                    }

                state.tool_calls += 1
                exec_result = self.execute_tool_call(call, state)

                state.messages.append({
                    "role": "tool",
                    "tool_call_id": call.get("id"),
                    "name": call.get("name"),
                    "content": json.dumps(exec_result)
                })
