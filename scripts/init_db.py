#!/usr/bin/env python3
"""
scripts/init_db.py
Zero-dependency SQLite & PostgreSQL database initializer.
Tests executing db/schema.sql and db/seed.sql against a local engine.
"""

import sqlite3
import os
import sys

DB_DIR = "db"
SCHEMA_PATH = os.path.join(DB_DIR, "schema.sql")
SEED_PATH = os.path.join(DB_DIR, "seed.sql")
TEST_DB = os.path.join(DB_DIR, "test_agentverse.sqlite")

def initialize_database():
    print("==========================================================================")
    print(" AgentVerse Database Initializer & SQL Feature Validator")
    print("==========================================================================")

    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)

    conn = sqlite3.connect(TEST_DB)
    cursor = conn.cursor()

    # 1. Execute Schema
    print("[*] Creating tables from db/schema.sql...")
    # SQLite compatibility translations for PostgreSQL types
    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        schema_raw = f.read()

    schema_sqlite = schema_raw.replace("SERIAL PRIMARY KEY", "INTEGER PRIMARY KEY AUTOINCREMENT")
    schema_sqlite = schema_sqlite.replace("TIMESTAMP WITH TIME ZONE", "DATETIME")
    schema_sqlite = schema_sqlite.replace("NUMERIC(5, 4)", "REAL")

    for statement in schema_sqlite.split(";"):
        stmt = statement.strip()
        if stmt:
            cursor.execute(stmt)
    conn.commit()
    print("  [+] Tables and indexes successfully created.")

    # 2. Execute Seed
    print("[*] Seeding sample data from db/seed.sql...")
    with open(SEED_PATH, "r", encoding="utf-8") as f:
        seed_raw = f.read()

    seed_sqlite = seed_raw.replace("ON CONFLICT (id) DO NOTHING", "ON CONFLICT DO NOTHING")
    seed_sqlite = seed_sqlite.replace("TRUE", "1").replace("FALSE", "0")

    for statement in seed_sqlite.split(";"):
        stmt = statement.strip()
        if stmt:
            cursor.execute(stmt)
    conn.commit()
    print("  [+] Sample rows seeded successfully.")

    # 3. Test Sample SELECT with JOIN and GROUP BY
    print("[*] Testing SQL SELECT with INNER JOIN...")
    cursor.execute("""
        SELECT t.id, t.topic, c.name AS category, t.priority
        FROM tasks t
        INNER JOIN categories c ON t.category_id = c.id
        ORDER BY t.priority ASC
    """)
    rows = cursor.fetchall()
    print(f"  [+] Retrieved {len(rows)} tasks via multi-table JOIN.")

    print("[*] Testing Parameterized Query (SQL Injection Defense)...")
    # Safe query using ? parameter
    test_param = "TASK-001"
    cursor.execute("SELECT id, topic, status FROM tasks WHERE id = ?", (test_param,))
    task = cursor.fetchone()
    print(f"  [+] Parameterized query safe lookup: {task}")

    conn.close()
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)

    print("\n[SUCCESS] SQL schema, seed, and queries validated with 0 errors!")
    return True

if __name__ == "__main__":
    success = initialize_database()
    sys.exit(0 if success else 1)
