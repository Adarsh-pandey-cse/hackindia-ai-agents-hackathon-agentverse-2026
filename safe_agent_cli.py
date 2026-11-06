"""
AgentVerse Safe Tool-Calling Agent CLI (safe_agent_cli.py)
Entry point for running and inspecting the tool-calling agent with safety limits,
tool schemas, interactive human-in-the-loop approval gates, and audit trails.
"""

import sys
import time
import json
import argparse
from typing import Dict, Any

from src.agent_loop import SafeToolCallingAgent, AgentLimits
from src.tools.schemas import TOOL_SCHEMAS, APPROVAL_REQUIRED_TOOLS


def main():
    parser = argparse.ArgumentParser(
        description="AgentVerse Safe Tool-Calling Agent - HackIndia AI Agents Hackathon",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Search campus AI events and draft registration (interactive approval)
  python safe_agent_cli.py --goal "Find AI events in Bengaluru and draft registration"

  # Run with auto-approval for automated testing
  python safe_agent_cli.py --goal "Calculate reimbursement for travel expenses: 450, 1200, 350" --auto-approve

  # Simulate human rejection on risky tool calls
  python safe_agent_cli.py --goal "Find AI events and send registration email" --reject-risky

  # Inspect registered tool schemas
  python safe_agent_cli.py --list-tools
        """
    )
    parser.add_argument("--goal", type=str, default="Find AI events in Bengaluru and draft registration",
                        help="User task or question for the agent")
    parser.add_argument("--auto-approve", action="store_true",
                        help="Automatically approve high-risk gated actions")
    parser.add_argument("--reject-risky", action="store_true",
                        help="Simulate human supervisor rejecting high-risk actions")
    parser.add_argument("--max-turns", type=int, default=8,
                        help="Hard limit on maximum agent loop iterations (default: 8)")
    parser.add_argument("--max-tools", type=int, default=12,
                        help="Hard limit on tool call budget (default: 12)")
    parser.add_argument("--timeout", type=float, default=30.0,
                        help="Hard limit on total execution time in seconds (default: 30.0)")
    parser.add_argument("--list-tools", action="store_true",
                        help="Display registered tool schemas with risk classifications")
    parser.add_argument("--verbose", "-v", action="store_true",
                        help="Display full step-by-step audit trail")

    args = parser.parse_args()

    if args.list_tools:
        print("\n========================================================")
        print(" REGISTERED AGENT TOOL SCHEMAS & RISK CLASSIFICATIONS")
        print("========================================================")
        for t in TOOL_SCHEMAS:
            risk_label = "HIGH (Approval Gate Required)" if t["risk"] == "high" else "LOW (Auto-Executable)"
            print(f"\n[Tool]: {t['name']}")
            print(f"  Risk Level:   {risk_label}")
            print(f"  Description:  {t['description']}")
            print(f"  Inputs:       {list(t['input_schema'].get('properties', {}).keys())}")
            print(f"  Required:     {t['input_schema'].get('required', [])}")
        print("\n========================================================\n")
        sys.exit(0)

    # Custom approval handler if --reject-risky flag passed
    approval_handler = None
    if args.reject_risky:
        def simulated_rejection(tool_name: str, arguments: Dict[str, Any]) -> bool:
            print(f"\n[Simulated Human Gate]: REJECTED high-risk tool call '{tool_name}' with args {arguments}")
            return False
        approval_handler = simulated_rejection

    limits = AgentLimits(
        max_turns=args.max_turns,
        max_tool_calls=args.max_tools,
        max_seconds=args.timeout,
        max_failures=2
    )

    agent = SafeToolCallingAgent(
        limits=limits,
        approval_handler=approval_handler,
        auto_approve=args.auto_approve
    )

    print("========================================================================")
    print(" AgentVerse Safe Tool-Calling Agent")
    print(f" User Goal:     '{args.goal}'")
    print(f" Safety Limits: Max Turns: {limits.max_turns} | Max Tools: {limits.max_tool_calls} | Timeout: {limits.max_seconds}s")
    print(f" Gated Tools:   {list(APPROVAL_REQUIRED_TOOLS)}")
    print("========================================================================\n")

    result = agent.run(args.goal)
    state = result["state"]

    print("\n========================================================================")
    print(f" EXECUTION RESULT: {result['status']} (Reason: {result['reason']})")
    print("========================================================================")
    if "answer" in result:
        print(f"\nFinal Response:\n{result['answer']}")
    elif "message" in result:
        print(f"\nStop Message:\n{result['message']}")

    print(f"\nSummary Metrics:")
    print(f" - Turns Elapsed:     {state.turns} / {limits.max_turns}")
    print(f" - Tool Calls Made:   {state.tool_calls} / {limits.max_tool_calls}")
    print(f" - Failures Logged:   {state.failures}")
    print(f" - Total Time Taken:  {time.time() - state.started_at:.3f}s")

    if args.verbose:
        print("\n--- STEP-BY-STEP AUDIT TRAIL ---")
        for idx, entry in enumerate(state.audit_log, 1):
            print(f"[{idx}] Type: {entry.get('type')} | Tool: {entry.get('tool')} | Details: {entry}")
        print("--------------------------------")

    print("========================================================================\n")
    sys.exit(0 if result["status"] in ("COMPLETED", "STOPPED") else 1)


if __name__ == "__main__":
    main()
