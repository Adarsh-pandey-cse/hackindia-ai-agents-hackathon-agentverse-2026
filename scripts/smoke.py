#!/usr/bin/env python3
"""
scripts/smoke.py - Cross-platform API smoke test
HackIndia Skill: design-an-api-teammates-can-use
"""
import urllib.request
import json
import sys

BASE_URL = "http://localhost:3000/api/v1"
HEALTH_URL = "http://localhost:3000/health"

def run_smoke():
    print("Running AgentVerse API Smoke Test...")
    try:
        req = urllib.request.Request(HEALTH_URL, headers={'User-Agent': 'SmokeTest'})
        res = urllib.request.urlopen(req, timeout=3)
        print(f"✓ Health Check: HTTP {res.status}")

        req2 = urllib.request.Request(f"{BASE_URL}/tasks?page=1&limit=5", headers={'User-Agent': 'SmokeTest'})
        res2 = urllib.request.urlopen(req2, timeout=3)
        print(f"✓ Tasks List: HTTP {res2.status}")
        return True
    except Exception as e:
        print(f"Smoke test note (ensure server is running via 'npm run api'): {e}")
        return False

if __name__ == "__main__":
    run_smoke()
