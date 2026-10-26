"""
Master Test Runner for First Principles
Walks through all track directories, runs each test_exercise.py in an isolated subprocess,
and provides a clean, clear progress summary.
"""

import os
import sys
import subprocess

def discover_test_files(root_dir):
    test_files = []
    for dirpath, _, filenames in os.walk(root_dir):
        if "test_exercise.py" in filenames:
            test_files.append(os.path.join(dirpath, "test_exercise.py"))
    # Sort deterministically by path
    return sorted(test_files)

def run_test_file(test_path, root_dir):
    step_dir = os.path.dirname(test_path)
    rel_path = os.path.relpath(step_dir, root_dir)
    
    # Run test in an isolated process to avoid sys.modules caching
    result = subprocess.run(
        [sys.executable, "test_exercise.py"],
        cwd=step_dir,
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0:
        return rel_path, "PASSED", "All tests passed"
    else:
        # Check stderr / stdout for failure details
        output = result.stderr + "\n" + result.stdout
        if "AssertionError" in output or "FAILED" in output:
            return rel_path, "PENDING", "Awaiting implementation (tests failing as expected)"
        elif "SyntaxError" in output:
            return rel_path, "ERROR", "SyntaxError in exercise.py"
        else:
            return rel_path, "PENDING", "Starter stub ready (implement code to pass)"

def main():
    root = os.path.dirname(os.path.abspath(__file__))
    test_files = discover_test_files(root)
    
    if not test_files:
        print("No test files found!")
        return

    print("=" * 80)
    print(" FIRST PRINCIPLES: PROGRESS TRACKER ")
    print("=" * 80)
    print(f"{'STEP / DIRECTORY':<56} {'STATUS':<10} {'DETAILS'}")
    print("-" * 80)

    passed_count = 0
    pending_count = 0
    error_count = 0

    for tf in test_files:
        rel_path, status, details = run_test_file(tf, root)
        if status == "PASSED":
            symbol = "[OK] PASS"
            passed_count += 1
        elif status == "PENDING":
            symbol = "[ ] TODO"
            pending_count += 1
        else:
            symbol = "[!] ERR "
            error_count += 1

        display_path = rel_path.replace("\\", "/")
        print(f"{display_path:<56} {symbol:<10} {details}")

    total = len(test_files)
    print("-" * 80)
    print(f"Summary: {passed_count}/{total} Passed | {pending_count}/{total} Pending | {error_count}/{total} Errors")
    print("=" * 80)
    if passed_count == total:
        print("\nAll steps across all tracks are complete and passing!")
    else:
        print(f"\nKeep going! Pick the next incomplete step, read its README.md, and code it out.")

if __name__ == "__main__":
    main()
