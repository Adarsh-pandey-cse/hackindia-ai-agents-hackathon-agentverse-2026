#!/usr/bin/env python3
"""
AgentVerse Autonomous AI Agent - Command Line Interface (CLI).
Skill: 'Write a runnable Python tool' (HackIndia 2026)
Author: Adarsh Pandey (@adarsh-pandey-cse)

Usage:
  python main.py
  python main.py --help
  python main.py --input data/sample_input.json --output-dir output
  python main.py --input data/sample_input.csv --priority HIGH
  python main.py --mock
"""

import os
import sys
import argparse
import logging
from typing import List
from agent import AutonomousAnalysisAgent

def configure_logging(log_file: str = "output/execution_proof.log", verbose: bool = False):
    """Configures structured logging to both stdout and persistent log file."""
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(name)s]: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.DEBUG if verbose else logging.INFO)

    file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    root_logger.handlers = [console_handler, file_handler]

def parse_arguments() -> argparse.Namespace:
    """Configures CLI argument parser implementing Lesson 7: Make it runnable by others."""
    parser = argparse.ArgumentParser(
        prog="agentverse-cli",
        description="AgentVerse Autonomous AI Agent - HackIndia Python Skill Tool",
        epilog="Example: python main.py --input data/sample_input.json --output-dir output"
    )

    parser.add_argument(
        "-i", "--input",
        dest="input_file",
        default="data/sample_input.json",
        help="Path to input task dataset (.json or .csv). Default: data/sample_input.json"
    )

    parser.add_argument(
        "-o", "--output-dir",
        dest="output_dir",
        default="output",
        help="Directory to save generated JSON, Markdown, and log outputs. Default: output"
    )

    parser.add_argument(
        "-p", "--priority",
        dest="priority",
        default="ALL",
        choices=["ALL", "HIGH", "MEDIUM", "LOW"],
        help="Filter tasks by minimum priority level. Default: ALL"
    )

    parser.add_argument(
        "--mock",
        dest="force_mock",
        action="store_true",
        help="Force mock API simulation mode (offline / isolated sandbox test)"
    )

    parser.add_argument(
        "-v", "--verbose",
        dest="verbose",
        action="store_true",
        help="Enable detailed debug logs"
    )

    return parser.parse_args()

def main() -> int:
    args = parse_arguments()

    print("=" * 72)
    print("  AgentVerse Autonomous AI Agent - HackIndia 2026")
    print("  Skill: Write a runnable Python tool")
    print("  Developer: @adarsh-pandey-cse (Adarsh Pandey)")
    print("=" * 72)

    log_file = os.path.join(args.output_dir, "execution_proof.log")
    configure_logging(log_file=log_file, verbose=args.verbose)
    logger = logging.getLogger("AgentVerse.Main")

    logger.info("Starting AgentVerse Autonomous Agent session...")
    logger.info(f"Configuration: input={args.input_file}, output_dir={args.output_dir}, mock={args.force_mock}")

    try:
        # Step 1: Initialize Agent
        agent = AutonomousAnalysisAgent(config_path=args.input_file, force_mock=args.force_mock)

        # Step 2: Ingest Data (Lesson 5: Read files and JSON)
        logger.info(f"[STEP 1/3] Reading data from: {args.input_file}")
        tasks = agent.load_input_data(args.input_file)

        if args.priority != "ALL":
            logger.info(f"Applying priority filter: {args.priority}")
            agent.tasks = agent.filter_by_priority(args.priority)

        print(f"[*] Successfully ingested {len(agent.tasks)} tasks.")

        # Step 3: Execute Tasks & Call APIs (Lesson 6: Call APIs from Python)
        logger.info("[STEP 2/3] Calling external REST APIs & mock fallbacks...")
        results = agent.execute_tasks()
        print(f"[*] Completed {len(results)} API-backed analytical tasks.")

        # Step 4: Write Useful Output (Lesson 5 & 7)
        logger.info(f"[STEP 3/3] Exporting structured reports to: {args.output_dir}")
        saved_paths = agent.save_outputs(output_dir=args.output_dir)

        print(f"[+] Output JSON Report:     {saved_paths['json']}")
        print(f"[+] Output Markdown Report: {saved_paths['markdown']}")
        print(f"[+] Execution Proof Log:    {log_file}")

        print("\n" + "=" * 72)
        print("  AGENT EXECUTION COMPLETED SUCCESSFULLY (EXIT CODE 0)")
        print("=" * 72)

        # Print summary preview table
        status_map = agent.get_task_status_map()
        for r in results:
            source = r.api_interaction.get("source", "N/A")
            latency = r.api_interaction.get("latency_ms", 0)
            status = status_map.get(r.task_id, "unknown")
            print(f" - [{r.task_id}] {r.target_topic:<42} | {source:<32} | {latency}ms [{status}]")

        return 0

    except Exception as exc:
        logger.exception(f"Fatal error during agent execution: {exc}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
