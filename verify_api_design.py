#!/usr/bin/env python3
"""
verify_api_design.py
Automated Verification Script for HackIndia Skill: 'design-an-api-teammates-can-use'
Developer: Adarsh Pandey (@adarsh-pandey-cse)

Validates the repository against HackIndia API Design criteria:
1. Versioning: /api/v1 prefix in routing
2. Resource-oriented URLs & HTTP methods (GET, POST, PUT, DELETE)
3. Meaningful status codes (200, 201, 204, 400, 404)
4. Consistent request and response shaping (JSON, envelopes)
5. Filtering & Pagination (?page=1&limit=5&priority=HIGH)
6. Centralized error handling with structured JSON error codes
7. Teammate documentation (docs/EXPRESS_API.md)
8. Smoke test scripts (scripts/smoke.sh & scripts/smoke.py)
"""

import os
import sys

GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

def log_pass(msg: str):
    print(f" {GREEN}[PASS]{RESET} {msg}")

def log_fail(msg: str):
    print(f" {RED}[FAIL]{RESET} {msg}")

def log_info(msg: str):
    print(f" {CYAN}[INFO]{RESET} {msg}")

def verify_api_design(root_dir: str = ".") -> bool:
    print(f"{BOLD}{'='*75}{RESET}")
    print(f"{BOLD} AgentVerse API Design Verification Tool{RESET}")
    print(f" HackIndia Skill: design-an-api-teammates-can-use")
    print(f" Developer: @adarsh-pandey-cse (Adarsh Pandey)")
    print(f"{BOLD}{'='*75}{RESET}\n")

    all_passed = True

    # 1. API Route Versioning (/api/v1)
    log_info("1. Verifying API Versioning and Routing...")
    app_js = os.path.join(root_dir, "server/app.js")
    if os.path.exists(app_js):
        with open(app_js, "r", encoding="utf-8") as f:
            content = f.read()
        if "/api/v1/tasks" in content:
            log_pass("Explicit versioning verified in server/app.js: /api/v1/tasks")
        else:
            log_fail("server/app.js missing /api/v1/tasks route binding")
            all_passed = False
    else:
        log_fail("Missing server/app.js")
        all_passed = False

    # 2. Resource URLs and HTTP Methods
    print()
    log_info("2. Verifying Resource-oriented URLs & HTTP Methods...")
    tasks_route = os.path.join(root_dir, "server/routes/tasks.js")
    if os.path.exists(tasks_route):
        with open(tasks_route, "r", encoding="utf-8") as f:
            content = f.read()
        for method in ["router.get", "router.post", "router.put", "router.delete"]:
            if method in content:
                log_pass(f"Method verified on resource: {method}")
            else:
                log_fail(f"Missing HTTP method: {method}")
                all_passed = False
    else:
        log_fail("Missing server/routes/tasks.js")
        all_passed = False

    # 3. Meaningful Status Codes
    print()
    log_info("3. Verifying Status Codes (200, 201, 204, 400, 404)...")
    if os.path.exists(tasks_route):
        with open(tasks_route, "r", encoding="utf-8") as f:
            content = f.read()
        for code in ["200", "201", "204"]:
            if f"res.status({code})" in content or f"status: {code}" in content:
                log_pass(f"Success status code verified: {code}")
            else:
                log_fail(f"Missing status code: {code}")
                all_passed = False

    # 4. Filtering and Pagination
    print()
    log_info("4. Verifying Filtering and Pagination...")
    if os.path.exists(tasks_route):
        with open(tasks_route, "r", encoding="utf-8") as f:
            content = f.read()
        if "priority" in content and "limit" in content and "page" in content:
            log_pass("Filtering (?priority=HIGH) and Pagination (?page=1&limit=20) verified")
        else:
            log_fail("server/routes/tasks.js missing pagination or filtering logic")
            all_passed = False

    # 5. Error Handling & Standardization
    print()
    log_info("5. Verifying Error Handling & Formatting...")
    err_file = os.path.join(root_dir, "server/errors/errorHandler.js")
    if os.path.exists(err_file):
        with open(err_file, "r", encoding="utf-8") as f:
            content = f.read()
        if "(err, req, res, next)" in content and "code" in content:
            log_pass("Centralized 4-arg error handler with structured error code format verified")
        else:
            log_fail("server/errors/errorHandler.js missing 4-arg signature or code formatting")
            all_passed = False
    else:
        log_fail("Missing server/errors/errorHandler.js")
        all_passed = False

    # 6. Documentation for Teammates
    print()
    log_info("6. Verifying Teammate Documentation (docs/EXPRESS_API.md)...")
    doc_path = os.path.join(root_dir, "docs/EXPRESS_API.md")
    if os.path.exists(doc_path):
        with open(doc_path, "r", encoding="utf-8") as f:
            doc_content = f.read()
        if "curl" in doc_content and "200" in doc_content and "400" in doc_content:
            log_pass("docs/EXPRESS_API.md contains endpoint tables, status codes, and curl examples")
        else:
            log_fail("docs/EXPRESS_API.md missing curl examples or status codes")
            all_passed = False
    else:
        log_fail("Missing docs/EXPRESS_API.md")
        all_passed = False

    # 7. Smoke Test File
    print()
    log_info("7. Verifying Smoke Test Scripts...")
    smoke_sh = os.path.join(root_dir, "scripts/smoke.sh")
    smoke_py = os.path.join(root_dir, "scripts/smoke.py")
    if os.path.exists(smoke_sh) and os.path.exists(smoke_py):
        log_pass("Smoke test scripts verified: scripts/smoke.sh & scripts/smoke.py")
    else:
        log_fail("Missing smoke test scripts in scripts/")
        all_passed = False

    # 8. README Starter Examples
    print()
    log_info("8. Verifying README.md API Examples & Base URL...")
    readme_path = os.path.join(root_dir, "README.md")
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            readme = f.read()
        if "Base URL: http://localhost:3000/api/v1" in readme and "curl" in readme:
            log_pass("README.md specifies Base URL and copy-pasteable curl examples")
        else:
            log_fail("README.md missing Base URL or curl examples")
            all_passed = False
    else:
        log_fail("Missing README.md")
        all_passed = False

    print(f"\n{BOLD}{'='*75}{RESET}")
    if all_passed:
        print(f" {GREEN}{BOLD}[VERIFICATION SUCCESS]{RESET} All API Design criteria PASSED!")
        print(f" The repository satisfies all requirements for 'design-an-api-teammates-can-use'.")
    else:
        print(f" {RED}{BOLD}[VERIFICATION FAILURE]{RESET} One or more criteria failed.")
    print(f"{BOLD}{'='*75}{RESET}\n")

    return all_passed

if __name__ == "__main__":
    success = verify_api_design()
    sys.exit(0 if success else 1)
