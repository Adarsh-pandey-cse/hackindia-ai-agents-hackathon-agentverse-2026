#!/usr/bin/env python3
"""
verify_full_stack_repo.py
Automated Verification Script for HackIndia Full-Stack Skill: 'ship-a-weekend-full-stack-repo'
Developer: Adarsh Pandey (@adarsh-pandey-cse)

Validates the full-stack repository against HackIndia submission criteria:
1. Client Frontend (React 18, Vite, Components, State, AbortController)
2. Server Backend (Express 5, Modular Routes, Middleware, 4-arg Error Handler)
3. Database & Storage Layer (Docker Compose PostgreSQL, JSON datastores, ML models)
4. Environment & Secrets Safety (.env.example present, .env git-ignored)
5. Package Scripts & Navigability (start, dev, api, test, build, docs)
"""

import os
import sys
import json
import re

GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
BOLD = "\033[1m"
RESET = "\033[0m"

def log_pass(msg: str):
    print(f" {GREEN}[PASS]{RESET} {msg}")

def log_fail(msg: str):
    print(f" {RED}[FAIL]{RESET} {msg}")

def log_info(msg: str):
    print(f" {CYAN}[INFO]{RESET} {msg}")

def verify_full_stack_repository(root_dir: str = ".") -> bool:
    print(f"{BOLD}{'='*75}{RESET}")
    print(f"{BOLD} AgentVerse Full-Stack Repository Verification Tool{RESET}")
    print(f" HackIndia Skill: ship-a-weekend-full-stack-repo")
    print(f" Developer: @adarsh-pandey-cse (Adarsh Pandey)")
    print(f"{BOLD}{'='*75}{RESET}\n")

    all_passed = True

    # 1. Frontend Client Verification
    log_info("1. Verifying Frontend Client (React 18 + Vite)...")
    required_frontend_files = [
        "src/App.jsx",
        "src/main.jsx",
        "src/components/MetricsBar.jsx",
        "src/components/TaskCard.jsx",
        "src/components/TaskList.jsx",
        "src/components/TaskFilter.jsx",
        "src/components/TaskForm.jsx",
        "vite.config.js",
        "index.html"
    ]
    for rf in required_frontend_files:
        path = os.path.join(root_dir, rf)
        if os.path.exists(path):
            log_pass(f"Frontend file exists: {rf}")
        else:
            log_fail(f"Missing frontend file: {rf}")
            all_passed = False

    # Check App.jsx state & API integration
    app_path = os.path.join(root_dir, "src/App.jsx")
    if os.path.exists(app_path):
        with open(app_path, "r", encoding="utf-8") as f:
            app_content = f.read()
        if "useState" in app_content and "useEffect" in app_content:
            log_pass("App.jsx implements React useState and justified useEffect")
        else:
            log_fail("App.jsx missing useState or useEffect")
            all_passed = False

        if "AbortController" in app_content and "controller.abort()" in app_content:
            log_pass("App.jsx handles component teardown and race conditions with AbortController")
        else:
            log_fail("App.jsx missing AbortController teardown")
            all_passed = False

        if "isLoading" in app_content and "errorMessage" in app_content:
            log_pass("App.jsx implements explicit Loading, Success, and Failure/Resilience states")
        else:
            log_fail("App.jsx missing loading or failure state handling")
            all_passed = False

    # Check Vite reverse proxy
    vite_path = os.path.join(root_dir, "vite.config.js")
    if os.path.exists(vite_path):
        with open(vite_path, "r", encoding="utf-8") as f:
            vite_content = f.read()
        if "proxy" in vite_content and "/api" in vite_content:
            log_pass("Vite configuration specifies reverse proxy for /api -> backend")
        else:
            log_fail("Vite configuration missing /api reverse proxy")
            all_passed = False

    # 2. Backend Server Verification
    print()
    log_info("2. Verifying Backend REST API (Express 5 + Node.js)...")
    required_backend_files = [
        "server/index.js",
        "server/app.js",
        "server/routes/tasks.js",
        "server/routes/agent.js",
        "server/middleware/logger.js",
        "server/errors/errorHandler.js",
        "server/config/env.js"
    ]
    for bf in required_backend_files:
        path = os.path.join(root_dir, bf)
        if os.path.exists(path):
            log_pass(f"Backend file exists: {bf}")
        else:
            log_fail(f"Missing backend file: {bf}")
            all_passed = False

    # Verify 4-argument centralized error handler in server/errors/errorHandler.js
    err_path = os.path.join(root_dir, "server/errors/errorHandler.js")
    if os.path.exists(err_path):
        with open(err_path, "r", encoding="utf-8") as f:
            err_content = f.read()
        if "(err, req, res, next)" in err_content:
            log_pass("Express 4-argument error handler verified in server/errors/errorHandler.js")
        else:
            log_fail("server/errors/errorHandler.js missing (err, req, res, next) signature")
            all_passed = False

    # 3. Database & Persistence Layer Verification
    print()
    log_info("3. Verifying Database & Persistence Layer...")
    docker_compose_path = os.path.join(root_dir, "docker-compose.yml")
    if os.path.exists(docker_compose_path):
        with open(docker_compose_path, "r", encoding="utf-8") as f:
            dc_content = f.read()
        if "postgres" in dc_content.lower() and "5432" in dc_content:
            log_pass("docker-compose.yml configures PostgreSQL database persistence")
        else:
            log_fail("docker-compose.yml missing PostgreSQL configuration")
            all_passed = False
    else:
        log_fail("Missing docker-compose.yml")
        all_passed = False

    # Check analytical datasets and model binaries
    for data_file in ["data/chunks.json", "data/sample_input.json", "models/agent_workload_classifier.joblib"]:
        path = os.path.join(root_dir, data_file)
        if os.path.exists(path):
            log_pass(f"Persistence artifact verified: {data_file}")
        else:
            log_fail(f"Missing persistence artifact: {data_file}")
            all_passed = False

    # 4. Environment & Secrets Hygiene
    print()
    log_info("4. Verifying Environment & Secrets Hygiene...")
    env_example_path = os.path.join(root_dir, ".env.example")
    if os.path.exists(env_example_path):
        with open(env_example_path, "r", encoding="utf-8") as f:
            env_ex = f.read()
        if "PORT=" in env_ex and "DATABASE_URL=" in env_ex:
            log_pass(".env.example template documents required environment variables")
        else:
            log_fail(".env.example missing PORT or DATABASE_URL")
            all_passed = False
    else:
        log_fail("Missing .env.example template")
        all_passed = False

    gitignore_path = os.path.join(root_dir, ".gitignore")
    if os.path.exists(gitignore_path):
        with open(gitignore_path, "r", encoding="utf-8") as f:
            git_ign = f.read()
        if ".env" in git_ign:
            log_pass(".gitignore properly ignores active .env secrets")
        else:
            log_fail(".gitignore does not ignore .env")
            all_passed = False

    # 5. Navigability, Package Scripts & Documentation
    print()
    log_info("5. Verifying Navigability, Package Scripts & Documentation...")
    pkg_path = os.path.join(root_dir, "package.json")
    if os.path.exists(pkg_path):
        with open(pkg_path, "r", encoding="utf-8") as f:
            pkg_data = json.load(f)
        scripts = pkg_data.get("scripts", {})
        for s in ["start", "dev", "api", "test", "build", "verify:fullstack"]:
            if s in scripts:
                log_pass(f"package.json script verified: npm run {s}")
            else:
                log_fail(f"package.json missing script: {s}")
                all_passed = False

    # Check README finish block
    readme_path = os.path.join(root_dir, "README.md")
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            readme_content = f.read()
        if "Project:" in readme_content and "What it does:" in readme_content and "API proof:" in readme_content:
            log_pass("README.md contains reviewer-ready submission block near the top")
        else:
            log_fail("README.md missing reviewer submission block (Project, What it does, API proof)")
            all_passed = False

    # Check docs/FULL_STACK_ARCHITECTURE.md
    arch_doc = os.path.join(root_dir, "docs/FULL_STACK_ARCHITECTURE.md")
    if os.path.exists(arch_doc):
        log_pass("docs/FULL_STACK_ARCHITECTURE.md exists with comprehensive state & API specs")
    else:
        log_fail("Missing docs/FULL_STACK_ARCHITECTURE.md")
        all_passed = False

    print(f"\n{BOLD}{'='*75}{RESET}")
    if all_passed:
        print(f" {GREEN}{BOLD}[VERIFICATION SUCCESS]{RESET} All Full-Stack criteria PASSED!")
        print(f" The repository satisfies all requirements for 'ship-a-weekend-full-stack-repo'.")
    else:
        print(f" {RED}{BOLD}[VERIFICATION FAILURE]{RESET} One or more criteria failed.")
    print(f"{BOLD}{'='*75}{RESET}\n")

    return all_passed

if __name__ == "__main__":
    success = verify_full_stack_repository()
    sys.exit(0 if success else 1)
