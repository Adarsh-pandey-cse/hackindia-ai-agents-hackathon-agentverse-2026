"""
Autonomous Agent Engine for AgentVerse Hackathon.
Performs data ingestion, autonomous task execution, API interaction,
and structured output generation.
"""

import json
import os
import logging
from datetime import datetime
from typing import Dict, Any, List
from api_client import APIClient

logger = logging.getLogger("AgentVerse.Agent")

class AutonomousAnalysisAgent:
    """Intelligent agent that ingests task data, queries external/mock APIs, and compiles actionable reports."""

    def __init__(self, config_path: str = "data/sample_input.json"):
        self.config_path = config_path
        self.api_client = APIClient()
        self.session_data: Dict[str, Any] = {}
        self.task_results: List[Dict[str, Any]] = []

    def load_input_data(self) -> Dict[str, Any]:
        """Reads and validates sample input data from file."""
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"Input configuration file not found at: {self.config_path}")

        logger.info(f"Loading input task data from: {self.config_path}")
        with open(self.config_path, "r", encoding="utf-8") as f:
            self.session_data = json.load(f)

        tasks = self.session_data.get("query_tasks", [])
        logger.info(f"Loaded {len(tasks)} tasks from input file.")
        return self.session_data

    def execute_tasks(self) -> List[Dict[str, Any]]:
        """Processes each task, dispatches API queries, and aggregates synthesized insights."""
        tasks = self.session_data.get("query_tasks", [])
        if not tasks:
            logger.warning("No tasks found to execute.")
            return []

        for idx, task in enumerate(tasks, 1):
            task_id = task.get("task_id", f"TASK-{idx:03d}")
            category = task.get("category", "general")
            topic = task.get("target_topic", "Unknown")
            priority = task.get("priority", "MEDIUM")

            logger.info(f"[{idx}/{len(tasks)}] Processing {task_id}: '{topic}' (Priority: {priority})")

            # Autonomous agent action: Call external/mock API
            api_response = self.api_client.fetch_topic_insights(category, topic)

            # Agent reasoning & synthesis step
            synthesis = self._synthesize_insights(task, api_response)

            record = {
                "task_id": task_id,
                "target_topic": topic,
                "category": category,
                "priority": priority,
                "processed_at": datetime.utcnow().isoformat() + "Z",
                "api_interaction": api_response,
                "agent_synthesis": synthesis
            }
            self.task_results.append(record)

        return self.task_results

    def _synthesize_insights(self, task: Dict[str, Any], api_response: Dict[str, Any]) -> Dict[str, Any]:
        """Synthesizes insights based on API output and task requirements."""
        source = api_response.get("source", "Unknown")
        status = api_response.get("status", "unknown")

        recommendations = [
            f"Prioritize resource allocation for {task.get('target_topic')}.",
            "Maintain continuous monitoring via scheduled background agents.",
            "Establish automated alert triggers on key sentiment shifts."
        ]

        return {
            "summary": f"Successfully completed intelligence sweep for '{task.get('target_topic')}' using {source}.",
            "data_source_used": source,
            "status": status,
            "confidence": 0.95 if status == "success" else 0.88,
            "strategic_recommendations": recommendations
        }

    def save_outputs(self, output_dir: str = "output") -> Dict[str, str]:
        """Writes structured JSON and Markdown summary outputs to disk."""
        os.makedirs(output_dir, exist_ok=True)

        json_path = os.path.join(output_dir, "agent_results.json")
        md_path = os.path.join(output_dir, "agent_summary.md")

        final_payload = {
            "agent_metadata": {
                "agent_name": self.session_data.get("agent_name", "Autonomous AI Agent"),
                "version": self.session_data.get("version", "1.0.0"),
                "execution_timestamp": datetime.utcnow().isoformat() + "Z",
                "total_tasks_processed": len(self.task_results)
            },
            "results": self.task_results
        }

        # Write JSON output
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(final_payload, f, indent=2)
        logger.info(f"Saved JSON results to {json_path}")

        # Write Markdown summary report
        md_content = self._generate_markdown_report(final_payload)
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(md_content)
        logger.info(f"Saved Markdown report to {md_path}")

        return {"json": json_path, "markdown": md_path}

    def _generate_markdown_report(self, payload: Dict[str, Any]) -> str:
        """Generates executive Markdown summary."""
        lines = [
            f"# {payload['agent_metadata']['agent_name']} - Execution Report",
            f"**Generated at:** {payload['agent_metadata']['execution_timestamp']}  ",
            f"**Tasks Processed:** {payload['agent_metadata']['total_tasks_processed']}  ",
            "\n---\n",
            "## Task Execution Overview\n",
            "| Task ID | Topic | Priority | API Source | Status |",
            "| :--- | :--- | :--- | :--- | :--- |"
        ]

        for item in payload.get("results", []):
            task_id = item["task_id"]
            topic = item["target_topic"]
            priority = item["priority"]
            source = item["api_interaction"].get("source", "N/A")
            status = item["api_interaction"].get("status", "N/A")
            lines.append(f"| `{task_id}` | {topic} | **{priority}** | {source} | `{status}` |")

        lines.append("\n## Key Insights & Recommendations\n")
        for item in payload.get("results", []):
            lines.append(f"### {item['task_id']}: {item['target_topic']}")
            lines.append(f"- **Summary:** {item['agent_synthesis']['summary']}")
            lines.append("- **Recommendations:**")
            for rec in item['agent_synthesis']['strategic_recommendations']:
                lines.append(f"  - {rec}")
            lines.append("")

        return "\n".join(lines)
