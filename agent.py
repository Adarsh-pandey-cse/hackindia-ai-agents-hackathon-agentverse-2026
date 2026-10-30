"""
Autonomous Agent Module for HackIndia: 'Write a runnable Python tool'.
Implements:
- Structured data representation (Dataclasses)
- Comprehensions (list, dict, set) for data shaping
- Robust file ingestion (JSON & CSV)
- API interaction dispatch
- Multi-format report generation (JSON, Markdown)
"""

import os
import csv
import json
import logging
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from typing import Dict, Any, List, Optional, Set
from api_client import APIClient

logger = logging.getLogger("AgentVerse.Agent")

@dataclass
class TaskItem:
    """Represents an analytical task ingested from input files."""
    task_id: str
    category: str
    target_topic: str
    priority: str = "MEDIUM"
    analysis_depth: str = "standard"

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "TaskItem":
        return cls(
            task_id=str(data.get("task_id", "")).strip(),
            category=str(data.get("category", "general")).strip(),
            target_topic=str(data.get("target_topic", "")).strip(),
            priority=str(data.get("priority", "MEDIUM")).strip().upper(),
            analysis_depth=str(data.get("analysis_depth", "standard")).strip()
        )

@dataclass
class AnalysisRecord:
    """Represents a completed analytical report item."""
    task_id: str
    category: str
    target_topic: str
    priority: str
    processed_at: str
    api_interaction: Dict[str, Any]
    agent_synthesis: Dict[str, Any]

class AutonomousAnalysisAgent:
    """
    Core AI-adjacent intelligence agent.
    Demonstrates Python data structures, comprehensions, file reading,
    API consumption, and formatted data output.
    """

    def __init__(self, config_path: str = "data/sample_input.json", force_mock: bool = False):
        self.config_path = config_path
        self.api_client = APIClient(force_mock=force_mock)
        self.agent_metadata: Dict[str, Any] = {
            "agent_name": "AgentVerse Trend & Intelligence Agent",
            "version": "1.2.0",
            "author": "Adarsh Pandey (@adarsh-pandey-cse)"
        }
        self.tasks: List[TaskItem] = []
        self.task_results: List[AnalysisRecord] = []

    def load_input_data(self, file_path: Optional[str] = None) -> List[TaskItem]:
        """
        Reads input data from either JSON or CSV files using Python file context managers.
        Implements Lesson 5: Read files and JSON.
        """
        path = file_path or self.config_path
        if not os.path.exists(path):
            raise FileNotFoundError(f"Input configuration file not found at: {path}")

        logger.info(f"Loading input dataset from: {path}")

        if path.endswith(".csv"):
            with open(path, mode="r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                # List comprehension to parse CSV rows into TaskItem instances (Lesson 2 & 5)
                self.tasks = [TaskItem.from_dict(row) for row in reader if row.get("task_id")]
        else:
            with open(path, mode="r", encoding="utf-8") as f:
                raw_data = json.load(f)
                if isinstance(raw_data, dict):
                    self.agent_metadata["agent_name"] = raw_data.get("agent_name", self.agent_metadata["agent_name"])
                    raw_tasks = raw_data.get("query_tasks", [])
                elif isinstance(raw_data, list):
                    raw_tasks = raw_data
                else:
                    raw_tasks = []

                # List comprehension with data transformation (Lesson 2: Shape data with comprehensions)
                self.tasks = [TaskItem.from_dict(t) for t in raw_tasks if t.get("task_id")]

        logger.info(f"Successfully loaded and validated {len(self.tasks)} tasks.")
        return self.tasks

    def get_categories(self) -> Set[str]:
        """Set comprehension demonstrating unique category extraction (Lesson 2)."""
        return {task.category for task in self.tasks}

    def filter_by_priority(self, min_priority: str = "HIGH") -> List[TaskItem]:
        """List comprehension filtering tasks by priority level (Lesson 2)."""
        return [task for task in self.tasks if task.priority == min_priority.upper()]

    def execute_tasks(self) -> List[AnalysisRecord]:
        """
        Iterates over tasks, calls external REST or mock APIs, and synthesizes findings.
        Implements Lesson 6: Call APIs from Python.
        """
        if not self.tasks:
            logger.warning("No tasks available to execute. Call load_input_data() first.")
            return []

        self.task_results.clear()

        for idx, task in enumerate(self.tasks, 1):
            logger.info(f"[{idx}/{len(self.tasks)}] Executing task '{task.task_id}': {task.target_topic} ({task.priority})")

            # Call API or mock API
            api_resp = self.api_client.fetch_topic_insights(task.category, task.target_topic)

            # Synthesize agent recommendations
            synthesis = self._synthesize_insights(task, api_resp)

            record = AnalysisRecord(
                task_id=task.task_id,
                category=task.category,
                target_topic=task.target_topic,
                priority=task.priority,
                processed_at=datetime.now(timezone.utc).isoformat(),
                api_interaction=api_resp,
                agent_synthesis=synthesis
            )
            self.task_results.append(record)

        logger.info(f"Completed execution of {len(self.task_results)} analytical tasks.")
        return self.task_results

    def get_task_status_map(self) -> Dict[str, str]:
        """Dict comprehension mapping each task_id to its API response status (Lesson 2)."""
        return {r.task_id: r.api_interaction.get("status", "unknown") for r in self.task_results}

    def _synthesize_insights(self, task: TaskItem, api_response: Dict[str, Any]) -> Dict[str, Any]:
        """Creates agent reasoning synthesis and actionable recommendations."""
        source = api_response.get("source", "Unknown")
        status = api_response.get("status", "unknown")
        latency = api_response.get("latency_ms", 0)

        recommendations = [
            f"Prioritize monitoring '{task.target_topic}' in production workflows.",
            f"Automate scheduled telemetry sweep via API client (current latency: {latency} ms).",
            "Incorporate synthesized outputs into cross-agent decision pipelines."
        ]

        return {
            "summary": f"Completed automated intelligence sweep for '{task.target_topic}' using {source}.",
            "data_source_used": source,
            "status": status,
            "confidence": 0.95 if status == "success" else 0.88,
            "strategic_recommendations": recommendations
        }

    def save_outputs(self, output_dir: str = "output") -> Dict[str, str]:
        """
        Exports results to structured JSON and human-readable Markdown.
        Implements Lesson 5 & 7: Writes useful output.
        """
        os.makedirs(output_dir, exist_ok=True)

        json_path = os.path.join(output_dir, "agent_results.json")
        md_path = os.path.join(output_dir, "agent_summary.md")

        # Dict comprehension for summary telemetry
        telemetry = {r.task_id: {"latency_ms": r.api_interaction.get("latency_ms"), "source": r.api_interaction.get("source")} for r in self.task_results}

        final_payload = {
            "agent_metadata": {
                **self.agent_metadata,
                "execution_timestamp": datetime.now(timezone.utc).isoformat(),
                "total_tasks_processed": len(self.task_results),
                "distinct_categories": list(self.get_categories())
            },
            "task_telemetry": telemetry,
            "results": [asdict(r) for r in self.task_results]
        }

        # 1. Write structured JSON output
        with open(json_path, mode="w", encoding="utf-8") as f:
            json.dump(final_payload, f, indent=2)
        logger.info(f"Saved JSON results to: {json_path}")

        # 2. Write Markdown executive summary
        md_content = self._generate_markdown_report(final_payload)
        with open(md_path, mode="w", encoding="utf-8") as f:
            f.write(md_content)
        logger.info(f"Saved Markdown report to: {md_path}")

        return {"json": json_path, "markdown": md_path}

    def _generate_markdown_report(self, payload: Dict[str, Any]) -> str:
        """Constructs formatted Markdown table and findings."""
        meta = payload["agent_metadata"]
        lines = [
            f"# {meta['agent_name']} - Execution Report",
            f"**Developer:** {meta.get('author', 'Adarsh Pandey')}  ",
            f"**Execution Timestamp:** `{meta['execution_timestamp']}`  ",
            f"**Tasks Processed:** {meta['total_tasks_processed']}  ",
            f"**Categories Analyzed:** {', '.join(meta['distinct_categories'])}  ",
            "\n---\n",
            "## Task Execution Overview\n",
            "| Task ID | Topic | Priority | API Source | Latency | Status |",
            "| :--- | :--- | :--- | :--- | :--- | :--- |"
        ]

        for item in payload.get("results", []):
            task_id = item["task_id"]
            topic = item["target_topic"]
            priority = item["priority"]
            api_info = item["api_interaction"]
            source = api_info.get("source", "N/A")
            latency = f"{api_info.get('latency_ms', 0)} ms"
            status = api_info.get("status", "N/A")
            lines.append(f"| `{task_id}` | {topic} | **{priority}** | {source} | {latency} | `{status}` |")

        lines.append("\n## Key Insights & Recommendations\n")
        for item in payload.get("results", []):
            lines.append(f"### {item['task_id']}: {item['target_topic']}")
            lines.append(f"- **Summary:** {item['agent_synthesis']['summary']}")
            lines.append("- **Recommendations:**")
            for rec in item['agent_synthesis']['strategic_recommendations']:
                lines.append(f"  - {rec}")
            lines.append("")

        return "\n".join(lines)
