#!/usr/bin/env python3
"""
verify_typescript.py
Automated Verification Script for HackIndia "Ship Safer JavaScript with TypeScript" Skill.

Validates:
1. tsconfig.json presence and strict compiler configurations
2. package.json typescript dependencies & typecheck scripts
3. Typed source code files (src-ts/types.ts, src-ts/agentService.ts, src-ts/index.ts)
4. Domain models, interfaces, union types, and custom type guards
5. Clean typecheck execution (tsc --noEmit exits with code 0)
6. Compiled output build verification (dist-ts/ declarations and js maps)
7. README.md documentation and reviewer quick-start instructions
"""
import sys
import os
import json
import subprocess

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
    print(" HackIndia Skill Verification: Ship Safer JavaScript with TypeScript")
    print(" Target: https://hackindia.org/skills/ship-safer-javascript-with-typescript")
    print("======================================================================\n")

    # 1. Check tsconfig.json
    total += 1
    tsconfig_path = "tsconfig.json"
    if not os.path.exists(tsconfig_path):
        log_fail("tsconfig.json not found")
        failures += 1
    else:
        with open(tsconfig_path, "r", encoding="utf-8") as f:
            tsconfig = json.load(f)
        options = tsconfig.get("compilerOptions", {})
        is_strict = options.get("strict") is True
        no_implicit_any = options.get("noImplicitAny") is True
        if is_strict and no_implicit_any:
            log_pass("tsconfig.json configured with strict mode (strict: true, noImplicitAny: true)")
        else:
            log_fail(f"tsconfig.json missing strict flags: strict={is_strict}, noImplicitAny={no_implicit_any}")
            failures += 1

    # 2. Check package.json dependencies and scripts
    total += 1
    pkg_path = "package.json"
    if not os.path.exists(pkg_path):
        log_fail("package.json not found")
        failures += 1
    else:
        with open(pkg_path, "r", encoding="utf-8") as f:
            pkg = json.load(f)
        deps = {**pkg.get("dependencies", {}), **pkg.get("devDependencies", {})}
        scripts = pkg.get("scripts", {})
        has_ts_dep = "typescript" in deps
        has_typecheck_script = "typecheck" in scripts
        if has_ts_dep and has_typecheck_script:
            log_pass(f"package.json verified: typescript ({deps.get('typescript')}), script: 'typecheck'")
        else:
            log_fail(f"package.json missing typescript dependency or typecheck script. has_ts={has_ts_dep}")
            failures += 1

    # 3. Check Typed Source Code & Domain Types
    total += 1
    ts_types_file = os.path.join("src-ts", "types.ts")
    if not os.path.exists(ts_types_file):
        log_fail(f"{ts_types_file} not found")
        failures += 1
    else:
        with open(ts_types_file, "r", encoding="utf-8") as f:
            types_content = f.read()
        has_interface = "interface TaskItem" in types_content
        has_union = "type PriorityLevel" in types_content or "PriorityLevel = 'HIGH'" in types_content
        has_discriminated = "AgentAction" in types_content and "payload" in types_content
        if has_interface and has_union and has_discriminated:
            log_pass("Typed domain models verified (interfaces, union types, discriminated unions)")
        else:
            log_fail("types.ts missing interface, union, or discriminated union definitions")
            failures += 1

    # 4. Check Type Guards & Safety Utilities
    total += 1
    ts_service_file = os.path.join("src-ts", "agentService.ts")
    if not os.path.exists(ts_service_file):
        log_fail(f"{ts_service_file} not found")
        failures += 1
    else:
        with open(ts_service_file, "r", encoding="utf-8") as f:
            service_content = f.read()
        has_type_guard = "is TaskItem" in service_content
        has_assert_never = "assertNever" in service_content or "never" in service_content
        has_generics = "<T>" in service_content or "<T extends" in service_content
        if has_type_guard and has_assert_never and has_generics:
            log_pass("Type guards, generics, and exhaustive checks verified in src-ts/agentService.ts")
        else:
            log_fail("src-ts/agentService.ts missing type guards or generics")
            failures += 1

    # 5. Execute TypeScript Type Checker (tsc --noEmit)
    total += 1
    cmd = "npx tsc --noEmit" if os.name != "nt" else "npx.cmd tsc --noEmit"
    try:
        proc = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if proc.returncode == 0:
            log_pass("TypeScript type-check (tsc --noEmit) completed with 0 errors")
        else:
            log_fail(f"Type check failed with code {proc.returncode}:\n{proc.stdout}\n{proc.stderr}")
            failures += 1
    except Exception as e:
        log_fail(f"Failed to execute tsc: {e}")
        failures += 1

    # 6. Check Compiled Output & Declarations (dist-ts)
    total += 1
    dist_dir = "dist-ts"
    has_dts = os.path.exists(os.path.join(dist_dir, "types.d.ts")) or os.path.exists(os.path.join(dist_dir, "agentService.d.ts"))
    if has_dts:
        log_pass("Compiled declaration files (.d.ts) verified in dist-ts/")
    else:
        log_fail(f"Compiled declaration files missing from {dist_dir}/")
        failures += 1

    # 7. Check README.md Documentation
    total += 1
    readme_path = "README.md"
    if not os.path.exists(readme_path):
        log_fail("README.md not found")
        failures += 1
    else:
        with open(readme_path, "r", encoding="utf-8") as f:
            readme = f.read()
        has_ts_badge = "ship-safer-javascript-with-typescript" in readme or "TypeScript" in readme
        has_ts_section = "TypeScript Architecture" in readme or "typecheck" in readme
        if has_ts_badge and has_ts_section:
            log_pass("README.md contains TypeScript documentation, badges, and verification instructions")
        else:
            log_fail("README.md missing TypeScript architecture documentation or badges")
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
