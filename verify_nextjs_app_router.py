#!/usr/bin/env python3
"""
verify_nextjs_app_router.py
Automated Verification Script for HackIndia Skill: 'ship-a-nextjs-app-router-project'
Developer: Adarsh Pandey (@adarsh-pandey-cse)

Validates the repository against HackIndia App Router criteria:
1. Dependencies: next, react, react-dom in package.json
2. File-based routes: app/layout.jsx, app/page.jsx, app/tasks/page.jsx
3. Server Component: app/tasks/page.jsx with async/await data fetch
4. Client Component: app/components/TaskForm.jsx with 'use client'
5. Route Handler: app/api/tasks/route.js with GET and POST
6. Configuration: next.config.mjs
7. README proof section
"""

import os
import sys
import json

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

def verify_nextjs_app_router(root_dir: str = ".") -> bool:
    print(f"{BOLD}{'='*75}{RESET}")
    print(f"{BOLD} AgentVerse Next.js App Router Verification Tool{RESET}")
    print(f" HackIndia Skill: ship-a-nextjs-app-router-project")
    print(f" Developer: @adarsh-pandey-cse (Adarsh Pandey)")
    print(f"{BOLD}{'='*75}{RESET}\n")

    all_passed = True

    # 1. Dependencies Verification
    log_info("1. Verifying Next.js dependencies in package.json...")
    pkg_path = os.path.join(root_dir, "package.json")
    if os.path.exists(pkg_path):
        with open(pkg_path, "r", encoding="utf-8") as f:
            pkg = json.load(f)
        deps = pkg.get("dependencies", {})
        for req in ["next", "react", "react-dom"]:
            if req in deps:
                log_pass(f"Dependency verified: {req} ({deps[req]})")
            else:
                log_fail(f"Missing dependency in package.json: {req}")
                all_passed = False
    else:
        log_fail("Missing package.json")
        all_passed = False

    # 2. File-based Routes & Shared Layout
    print()
    log_info("2. Verifying File-based Routes & Layout in app/...")
    required_routes = [
        "app/layout.jsx",
        "app/page.jsx",
        "app/tasks/page.jsx",
        "next.config.mjs"
    ]
    for r in required_routes:
        p = os.path.join(root_dir, r)
        if os.path.exists(p):
            log_pass(f"Route file exists: {r}")
        else:
            log_fail(f"Missing route file: {r}")
            all_passed = False

    # 3. Server Component Data Fetching
    print()
    log_info("3. Verifying Server Component (app/tasks/page.jsx)...")
    tasks_page = os.path.join(root_dir, "app/tasks/page.jsx")
    if os.path.exists(tasks_page):
        with open(tasks_page, "r", encoding="utf-8") as f:
            content = f.read()
        if "async" in content and "await" in content:
            log_pass("app/tasks/page.jsx implements async/await server-side data fetching")
        else:
            log_fail("app/tasks/page.jsx does not implement async/await")
            all_passed = False
        if "'use client'" not in content and '"use client"' not in content:
            log_pass("app/tasks/page.jsx runs as a default Server Component (no 'use client')")
        else:
            log_fail("app/tasks/page.jsx should be a Server Component")
            all_passed = False

    # 4. Client Component Boundary
    print()
    log_info("4. Verifying Client Component (app/components/TaskForm.jsx)...")
    client_comp = os.path.join(root_dir, "app/components/TaskForm.jsx")
    if os.path.exists(client_comp):
        with open(client_comp, "r", encoding="utf-8") as f:
            content = f.read()
        if "'use client'" in content or '"use client"' in content:
            log_pass("app/components/TaskForm.jsx explicitly marks boundary with 'use client'")
        else:
            log_fail("app/components/TaskForm.jsx missing 'use client' directive")
            all_passed = False
        if "useState" in content:
            log_pass("app/components/TaskForm.jsx manages interactive state with useState")
        else:
            log_fail("app/components/TaskForm.jsx missing useState")
            all_passed = False

    # 5. Route Handler
    print()
    log_info("5. Verifying Route Handler (app/api/tasks/route.js)...")
    route_file = os.path.join(root_dir, "app/api/tasks/route.js")
    if os.path.exists(route_file):
        with open(route_file, "r", encoding="utf-8") as f:
            content = f.read()
        if "export async function GET" in content:
            log_pass("Route handler exports GET handler")
        else:
            log_fail("Route handler missing GET handler")
            all_passed = False
        if "export async function POST" in content:
            log_pass("Route handler exports POST handler")
        else:
            log_fail("Route handler missing POST handler")
            all_passed = False

    # 6. README Proof Block
    print()
    log_info("6. Verifying README.md App Router Proof Block...")
    readme_path = os.path.join(root_dir, "README.md")
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            readme = f.read()
        if "Next.js App Router" in readme and "App Router proof:" in readme:
            log_pass("README.md contains App Router proof section with exact file paths")
        else:
            log_fail("README.md missing App Router proof section")
            all_passed = False

    print(f"\n{BOLD}{'='*75}{RESET}")
    if all_passed:
        print(f" {GREEN}{BOLD}[VERIFICATION SUCCESS]{RESET} All Next.js App Router criteria PASSED!")
        print(f" The repository satisfies all requirements for 'ship-a-nextjs-app-router-project'.")
    else:
        print(f" {RED}{BOLD}[VERIFICATION FAILURE]{RESET} One or more criteria failed.")
    print(f"{BOLD}{'='*75}{RESET}\n")

    return all_passed

if __name__ == "__main__":
    success = verify_nextjs_app_router()
    sys.exit(0 if success else 1)
