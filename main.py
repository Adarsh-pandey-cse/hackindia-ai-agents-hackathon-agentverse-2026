"""
Main Entry Point for Autonomous AI Agent.
Author: Adarsh Pandey (@adarsh-pandey-cse)
Project: HackIndia AI Agents Hackathon - AgentVerse 2026
"""

import os
import sys
import logging
from agent import AutonomousAnalysisAgent

def configure_logging(log_file: str = "output/execution_proof.log"):
    """Configures multi-handler logging to stdout and file."""
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    
    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(name)s]: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)

    file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    root_logger.handlers = [console_handler, file_handler]

def main():
    print("=" * 70)
    print("  AgentVerse Autonomous AI Agent - HackIndia 2026")
    print("  Developer: @adarsh-pandey-cse (Adarsh Pandey)")
    print("=" * 70)

    # 1. Setup logging
    log_file = "output/execution_proof.log"
    configure_logging(log_file)
    logger = logging.getLogger("AgentVerse.Main")
    logger.info("Initializing AgentVerse Autonomous Agent session...")

    try:
        # 2. Initialize Agent
        agent = AutonomousAnalysisAgent(config_path="data/sample_input.json")

        # 3. Step 1: Read input data
        logger.info("[STEP 1/3] Ingesting sample input dataset from data/sample_input.json")
        input_data = agent.load_input_data()
        print(f"[*] Ingested {len(input_data.get('query_tasks', []))} tasks for processing.")

        # 4. Step 2: Execute tasks & query APIs / mock APIs
        logger.info("[STEP 2/3] Calling live REST APIs & mock fallbacks for intelligence gathering")
        results = agent.execute_tasks()
        print(f"[*] Completed {len(results)} API-backed analytical tasks.")

        # 5. Step 3: Write useful output to files
        logger.info("[STEP 3/3] Exporting structured results & executive markdown report to output/")
        output_files = agent.save_outputs(output_dir="output")
        print(f"[+] Output JSON Report:     {output_files['json']}")
        print(f"[+] Output Markdown Report: {output_files['markdown']}")
        print(f"[+] Execution Proof Log:    {log_file}")

        print("\n" + "=" * 70)
        print("  AGENT EXECUTION COMPLETED SUCCESSFULLY!")
        print("=" * 70)

        # Print quick preview of results
        for r in results:
            print(f" - [{r['task_id']}] {r['target_topic']}: {r['api_interaction'].get('source')} (Status: {r['api_interaction'].get('status')})")

        return 0

    except Exception as e:
        logger.exception(f"Fatal error during agent execution: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
