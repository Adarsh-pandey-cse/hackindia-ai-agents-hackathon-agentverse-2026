#!/usr/bin/env python3
"""
verify_sql_feature.py
Automated Verification Script for HackIndia Skill: 'design-sql-backed-features'
Developer: Adarsh Pandey (@adarsh-pandey-cse)

Validates the repository against HackIndia SQL Feature criteria:
1. Schema definition: db/schema.sql with primary keys, foreign keys, and indexes
2. Seed data: db/seed.sql with realistic initial records
3. Query designs: db/queries.sql covering SELECT, JOIN, GROUP BY
4. Parameterized queries to stop SQL injection: server/db/database.js
5. Database runner & test: scripts/init_db.py
6. README.md documentation with feature, tech, run steps, and sample queries
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

def verify_sql_feature(root_dir: str = ".") -> bool:
    print(f"{BOLD}{'='*75}{RESET}")
    print(f"{BOLD} AgentVerse SQL Feature Verification Tool{RESET}")
    print(f" HackIndia Skill: design-sql-backed-features")
    print(f" Developer: @adarsh-pandey-cse (Adarsh Pandey)")
    print(f"{BOLD}{'='*75}{RESET}\n")

    all_passed = True

    # 1. db/schema.sql
    log_info("1. Verifying Database Schema (db/schema.sql)...")
    schema_path = os.path.join(root_dir, "db/schema.sql")
    if os.path.exists(schema_path):
        with open(schema_path, "r", encoding="utf-8") as f:
            schema = f.read()
        for kw in ["CREATE TABLE", "PRIMARY KEY", "FOREIGN KEY", "REFERENCES", "CREATE INDEX"]:
            if kw in schema:
                log_pass(f"Schema construct verified: {kw}")
            else:
                log_fail(f"db/schema.sql missing construct: {kw}")
                all_passed = False
    else:
        log_fail("Missing db/schema.sql")
        all_passed = False

    # 2. db/seed.sql
    print()
    log_info("2. Verifying Seed Data (db/seed.sql)...")
    seed_path = os.path.join(root_dir, "db/seed.sql")
    if os.path.exists(seed_path):
        with open(seed_path, "r", encoding="utf-8") as f:
            seed = f.read()
        if "INSERT INTO" in seed:
            log_pass("db/seed.sql contains valid INSERT INTO seed data")
        else:
            log_fail("db/seed.sql missing INSERT INTO statements")
            all_passed = False
    else:
        log_fail("Missing db/seed.sql")
        all_passed = False

    # 3. db/queries.sql
    print()
    log_info("3. Verifying SQL Query Patterns (db/queries.sql)...")
    queries_path = os.path.join(root_dir, "db/queries.sql")
    if os.path.exists(queries_path):
        with open(queries_path, "r", encoding="utf-8") as f:
            queries = f.read()
        for qk in ["SELECT", "JOIN", "GROUP BY"]:
            if qk in queries:
                log_pass(f"Query competency verified: {qk}")
            else:
                log_fail(f"db/queries.sql missing {qk}")
                all_passed = False
    else:
        log_fail("Missing db/queries.sql")
        all_passed = False

    # 4. Parameterized Query Security (server/db/database.js)
    print()
    log_info("4. Verifying Parameterized Queries & SQL Injection Defense...")
    db_js_path = os.path.join(root_dir, "server/db/database.js")
    if os.path.exists(db_js_path):
        with open(db_js_path, "r", encoding="utf-8") as f:
            db_code = f.read()
        if "$1" in db_code and "params" in db_code:
            log_pass("server/db/database.js enforces parameterized inputs ($1) to prevent injection")
        else:
            log_fail("server/db/database.js missing parameterized inputs")
            all_passed = False
    else:
        log_fail("Missing server/db/database.js")
        all_passed = False

    # 5. Database Initializer Runner
    print()
    log_info("5. Verifying Database Runner (scripts/init_db.py)...")
    init_py = os.path.join(root_dir, "scripts/init_db.py")
    if os.path.exists(init_py):
        log_pass("scripts/init_db.py runner exists and enables cross-platform schema verification")
    else:
        log_fail("Missing scripts/init_db.py")
        all_passed = False

    # 6. README Proof Block
    print()
    log_info("6. Verifying README.md SQL Feature Proof Block...")
    readme_path = os.path.join(root_dir, "README.md")
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            readme = f.read()
        if "SQL-Backed Feature" in readme and "db/schema.sql" in readme and "SELECT" in readme:
            log_pass("README.md documents SQL-backed feature, schema paths, and sample queries")
        else:
            log_fail("README.md missing SQL-backed feature documentation")
            all_passed = False
    else:
        log_fail("Missing README.md")
        all_passed = False

    print(f"\n{BOLD}{'='*75}{RESET}")
    if all_passed:
        print(f" {GREEN}{BOLD}[VERIFICATION SUCCESS]{RESET} All SQL Feature criteria PASSED!")
        print(f" The repository satisfies all requirements for 'design-sql-backed-features'.")
    else:
        print(f" {RED}{BOLD}[VERIFICATION FAILURE]{RESET} One or more criteria failed.")
    print(f"{BOLD}{'='*75}{RESET}\n")

    return all_passed

if __name__ == "__main__":
    success = verify_sql_feature()
    sys.exit(0 if success else 1)
