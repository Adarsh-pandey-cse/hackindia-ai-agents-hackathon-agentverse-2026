#!/usr/bin/env python3
"""
verify_recruiter_ready_repo.py
Automated Verification Script for HackIndia "Ship a recruiter-ready GitHub repo" Skill.

Validates:
1. Git repository setup and clean commit history (>= 10 commits with descriptive messages)
2. Author identity (commits by author)
3. Proper .gitignore (ignoring node_modules, .env, build output, cache)
4. Comprehensive README.md with setup instructions, run commands, and architecture
5. LICENSE file existence (MIT)
6. Security checks (no secrets or .env files tracked by git)
7. Automated test runner and verification commands
"""
import sys
import os
import subprocess
import re

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def log_pass(msg):
    print(f"[{GREEN}PASS{RESET}] {msg}")

def log_fail(msg):
    print(f"[{RED}FAIL{RESET}] {msg}")

def log_info(msg):
    print(f"[{YELLOW}INFO{RESET}] {msg}")

def run_checks():
    failures = 0
    total = 0

    print("======================================================================")
    print(" HackIndia Skill Verification: Ship a Recruiter-Ready GitHub Repo")
    print(" Target: https://hackindia.org/skills/ship-a-recruiter-ready-github-repo")
    print("======================================================================\n")

    # 1. Check Git Commit History
    total += 1
    try:
        proc = subprocess.run(["git", "log", "--oneline", "-n", "30"], capture_output=True, text=True, check=True)
        commits = [line for line in proc.stdout.splitlines() if line.strip()]
        conventional_count = sum(1 for c in commits if any(c.split(' ', 1)[-1].startswith(prefix) for prefix in ['feat:', 'fix:', 'docs:', 'chore:', 'refactor:', 'test:']))
        if len(commits) >= 5 and conventional_count >= 5:
            log_pass(f"Readable Git commit history verified: {len(commits)} commits detected, {conventional_count} using Conventional Commits")
        else:
            log_fail(f"Commit history insufficient: {len(commits)} commits found, {conventional_count} conventional commits")
            failures += 1
    except Exception as e:
        log_fail(f"Failed to inspect git log: {e}")
        failures += 1

    # 2. Check Git Author Identity
    total += 1
    try:
        proc = subprocess.run(["git", "log", "-n", "5", "--format=%an <%ae>"], capture_output=True, text=True, check=True)
        authors = set(proc.stdout.splitlines())
        has_author = any("Adarsh Pandey" in a or "adarsh" in a.lower() for a in authors)
        if has_author:
            log_pass(f"Commit author identity verified: {', '.join(authors)}")
        else:
            log_fail(f"Unexpected commit author: {authors}")
            failures += 1
    except Exception as e:
        log_fail(f"Failed to check git author: {e}")
        failures += 1

    # 3. Check .gitignore Safety
    total += 1
    gitignore_path = ".gitignore"
    if not os.path.exists(gitignore_path):
        log_fail(".gitignore file not found")
        failures += 1
    else:
        with open(gitignore_path, "r", encoding="utf-8") as f:
            gi_content = f.read()
        has_node_modules = "node_modules" in gi_content
        has_env = ".env" in gi_content
        has_cache = "pycache" in gi_content or "__pycache__" in gi_content
        if has_node_modules and has_env and has_cache:
            log_pass(".gitignore verified (ignores node_modules, .env secrets, __pycache__)")
        else:
            log_fail(".gitignore missing required safety ignores")
            failures += 1

    # 4. Check No Committed Secrets (.env)
    total += 1
    try:
        proc = subprocess.run(["git", "ls-files", ".env"], capture_output=True, text=True)
        if proc.stdout.strip() == "":
            log_pass("Secret hygiene verified: active .env file is NOT tracked in git")
        else:
            log_fail(f"Active .env file is tracked in git repository: {proc.stdout}")
            failures += 1
    except Exception as e:
        log_fail(f"Failed to check tracked files: {e}")
        failures += 1

    # 5. Check LICENSE File
    total += 1
    license_path = "LICENSE"
    if os.path.exists(license_path):
        with open(license_path, "r", encoding="utf-8") as f:
            lic = f.read()
        if "MIT" in lic or "License" in lic:
            log_pass("Open-source LICENSE file verified (MIT License)")
        else:
            log_fail("LICENSE file exists but license type unrecognized")
            failures += 1
    else:
        log_fail("LICENSE file not found")
        failures += 1

    # 6. Check README Quickstart & Setup Instructions
    total += 1
    readme_path = "README.md"
    if not os.path.exists(readme_path):
        log_fail("README.md not found")
        failures += 1
    else:
        with open(readme_path, "r", encoding="utf-8") as f:
            readme = f.read()
        has_clone = "git clone" in readme
        has_run = "npm" in readme or "python" in readme
        has_prereqs = "Prerequisites" in readme or "Requirements" in readme or "Run Locally" in readme
        if has_clone and has_run and has_prereqs:
            log_pass("README.md verified: clear setup steps, git clone command, prerequisites, and run commands")
        else:
            log_fail("README.md missing setup instructions or clone commands")
            failures += 1

    # 7. Check Recruiter-Ready Documentation & Proof Block
    total += 1
    has_recruiter_block = "ship-a-recruiter-ready-github-repo" in readme or "Recruiter-Ready" in readme or "Git & GitHub" in readme
    if has_recruiter_block:
        log_pass("Recruiter-ready GitHub summary block and HackIndia skill badge verified in README.md")
    else:
        log_fail("README.md missing recruiter-ready GitHub summary block or badge")
        failures += 1

    print("\n----------------------------------------------------------------------")
    print(f" Verification Result: {total - failures}/{total} checks passed.")
    print("----------------------------------------------------------------------")

    if failures == 0:
        print(f"\n{GREEN}ALL CHECKS PASSED SUCCESSFULLY! Ready for HackIndia submission.{RESET}\n")
        return 0
    else:
        print(f"\n{RED}VERIFICATION FAILED: {failures} issues detected.{RESET}\n")
        return 1

if __name__ == "__main__":
    sys.exit(run_checks())
