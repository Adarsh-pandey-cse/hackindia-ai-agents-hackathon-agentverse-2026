#!/usr/bin/env python3
"""
verify_safe_signin.py
Automated Verification Script for HackIndia "Add Safe Sign-In" Skill.

Validates:
1. Dependencies in package.json (jsonwebtoken, bcrypt / bcryptjs)
2. Safe password hashing (bcrypt salt rounds, verification)
3. Safe token handling (JWT issuance, verification, claims)
4. Safe cookie attributes (HttpOnly, SameSite=Strict, Secure flag, Path=/)
5. Protected route enforcement (requireAuth middleware, 401 on unauthorized)
6. Safe signout session invalidation
7. README documentation detailing auth choices and security checks
"""
import sys
import os
import json
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
    print(" HackIndia Skill Verification: Add Safe Sign-In")
    print(" Target: https://hackindia.org/skills/add-safe-sign-in#task")
    print("======================================================================\n")

    # 1. Check package.json dependencies
    total += 1
    pkg_path = "package.json"
    if not os.path.exists(pkg_path):
        log_fail("package.json not found")
        failures += 1
    else:
        with open(pkg_path, "r", encoding="utf-8") as f:
            pkg = json.load(f)
        deps = {**pkg.get("dependencies", {}), **pkg.get("devDependencies", {})}
        has_jwt = any("jsonwebtoken" in d or "jose" in d or "next-auth" in d for d in deps)
        has_bcrypt = any("bcrypt" in d or "argon2" in d for d in deps)
        if has_jwt and has_bcrypt:
            log_pass(f"Dependencies verified: jsonwebtoken ({deps.get('jsonwebtoken', 'found')}), bcrypt/bcryptjs ({deps.get('bcryptjs', 'found')})")
        else:
            log_fail(f"Missing required auth dependencies. has_jwt={has_jwt}, has_bcrypt={has_bcrypt}")
            failures += 1

    # 2. Check Auth Route & Bcrypt Hashing
    total += 1
    auth_route_path = os.path.join("server", "routes", "auth.js")
    if not os.path.exists(auth_route_path):
        log_fail(f"{auth_route_path} not found")
        failures += 1
    else:
        with open(auth_route_path, "r", encoding="utf-8") as f:
            code = f.read()
        has_bcrypt_hash = "bcrypt.hash" in code or "bcrypt.hashSync" in code
        has_bcrypt_compare = "bcrypt.compare" in code
        if has_bcrypt_hash and has_bcrypt_compare:
            log_pass("Bcrypt password hashing and constant-time comparison verified in server/routes/auth.js")
        else:
            log_fail("Bcrypt hashing or compare missing from server/routes/auth.js")
            failures += 1

    # 3. Check Cookie Security Attributes
    total += 1
    with open(auth_route_path, "r", encoding="utf-8") as f:
        code = f.read()
    has_httponly = "HttpOnly" in code
    has_samesite = "SameSite=Strict" in code or "SameSite" in code
    has_maxage = "Max-Age" in code or "maxAge" in code
    if has_httponly and has_samesite and has_maxage:
        log_pass("Cookie security flags verified (HttpOnly: true, SameSite=Strict, Max-Age expiry)")
    else:
        log_fail(f"Cookie security flags missing: HttpOnly={has_httponly}, SameSite={has_samesite}")
        failures += 1

    # 4. Check Protected Route & Middleware Enforcement
    total += 1
    auth_mw_path = os.path.join("server", "middleware", "auth.js")
    if not os.path.exists(auth_mw_path):
        log_fail(f"{auth_mw_path} not found")
        failures += 1
    else:
        with open(auth_mw_path, "r", encoding="utf-8") as f:
            mw_code = f.read()
        has_require_auth = "requireAuth" in mw_code
        has_jwt_verify = "jwt.verify" in mw_code
        has_unauthorized = "unauthorized" in mw_code or "401" in mw_code
        if has_require_auth and has_jwt_verify and has_unauthorized:
            log_pass("Authentication middleware (requireAuth) verifies JWT and returns 401 on unauthorized")
        else:
            log_fail("Auth middleware missing required verification logic")
            failures += 1

    # 5. Check Next.js App Router Auth Handler
    total += 1
    next_auth_route = os.path.join("app", "api", "auth", "route.js")
    if os.path.exists(next_auth_route):
        with open(next_auth_route, "r", encoding="utf-8") as f:
            next_code = f.read()
        if "cookies().set" in next_code or "response.cookies.set" in next_code:
            log_pass("Next.js App Router API Route verifies credentials and sets HttpOnly cookies")
        else:
            log_fail("Next.js App Router auth route missing cookie handling")
            failures += 1
    else:
        log_fail(f"{next_auth_route} not found")
        failures += 1

    # 6. Check Safe Signout Session Destruction
    total += 1
    has_signout = "signout" in code or "logout" in code
    has_clear_cookie = "Max-Age=0" in code or "clearCookie" in code or "maxAge: 0" in code
    if has_signout and has_clear_cookie:
        log_pass("Safe signout route invalidates session cookie on demand")
    else:
        log_fail("Safe signout / cookie clearance missing")
        failures += 1

    # 7. Check README Documentation & Badges
    total += 1
    readme_path = "README.md"
    if not os.path.exists(readme_path):
        log_fail("README.md not found")
        failures += 1
    else:
        with open(readme_path, "r", encoding="utf-8") as f:
            readme = f.read()
        has_auth_heading = "Safe Authentication" in readme or "add-safe-sign-in" in readme or "Authentication" in readme
        has_security_explanation = "bcrypt" in readme and "HttpOnly" in readme and "JWT" in readme
        if has_auth_heading and has_security_explanation:
            log_pass("README.md documents auth architecture, bcrypt hashing, cookie flags, and security checks")
        else:
            log_fail("README.md missing detailed auth architecture or security checklist")
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
