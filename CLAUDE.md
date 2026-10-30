@AGENTS.md

# Claude Code Project Context

Project: AgentVerse Autonomous AI Agent & ML Pipeline
Hackathon: HackIndia AI Agents Hackathon - AgentVerse 2026
Developer: Adarsh Pandey (@adarsh-pandey-cse)
Repository: https://github.com/Adarsh-pandey-cse/hackindia-ai-agents-hackathon-agentverse-2026-adarsh-pandeys-team

Stack:
- Python: 3.9+ (tested on Python 3.12.10)
- Machine Learning: scikit-learn, joblib, numpy
- Networking: requests (with offline mock fallback engine)
- Testing: Python standard library unittest framework

Commands:
- Install dependencies: pip install -r requirements.txt
- Run Python Agent Tool: python main.py
- Run with options: python main.py --input data/sample_input.csv --priority HIGH
- Run in offline mock mode: python main.py --mock
- Run ML training pipeline: python train_ml_model.py
- Run full test suite: python -m unittest discover tests

Conventions:
- Strongly typed data models using @dataclass.
- Clean exit codes: 0 for successful execution, non-zero for failures.
- Generated reports and logs must be stored in output/.
- Do not read or modify .env or .env.* files (enforced via .claude/settings.json).
- For multi-file changes, propose an explicit file-based plan first.
- Keep dependency footprint minimal and pinned in requirements.txt.

Review checklist:
- Run python -m unittest discover tests before any commit.
- Inspect git status and git diff before publishing changes.
- Ensure all commits are authored by Adarsh Pandey <adarshpandey.cse@gmail.com>.
- Maintain public repository visibility on GitHub.
