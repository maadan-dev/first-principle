"""
Master Test Runner for Fellowship Bridge: Set 4.
Runs all 8 drill test suites with zero external dependencies.
Usage: python run_all_tests.py
"""
import os
import subprocess
import sys

DRILLS = [
    ("Drill 01: Optimized Primes", "01-optimized-primes"),
    ("Drill 02: Fibonacci Even Sum", "02-fibonacci-even-sum"),
    ("Drill 03: Decimal to Binary", "03-decimal-to-binary"),
    ("Drill 04: Matrix Multiplication", "04-matrix-multiplication"),
    ("Drill 05: ASCII Capitalizer", "05-ascii-capitalize"),
    ("Drill 06: Anagram Checker", "06-anagram-checker"),
    ("Drill 07: Roman to Integer", "07-roman-to-integer"),
    ("Drill 08: 90° Matrix Rotation", "08-matrix-rotation"),
]

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    total_drills = len(DRILLS)
    passed_drills = 0

    print("=" * 60)
    print("  FELLOWSHIP BRIDGE: SET 4 MASTER TEST SUITE")
    print("=" * 60)

    for title, folder in DRILLS:
        test_file = os.path.join(base_dir, folder, "test_exercise.py")
        if not os.path.exists(test_file):
            print(f"\n[SKIP] {title} (test file not found)")
            continue

        print(f"\n>> Running {title}...")
        result = subprocess.run(
            [sys.executable, "test_exercise.py"],
            cwd=os.path.join(base_dir, folder),
            capture_output=True,
            text=True
        )

        # Print output indented
        print(result.stdout.strip())
        if result.returncode == 0:
            passed_drills += 1

    print("\n" + "=" * 60)
    print(f"OVERALL SUMMARY: {passed_drills}/{total_drills} drills fully passed.")
    print("=" * 60 + "\n")

    return 0 if passed_drills == total_drills else 1

if __name__ == "__main__":
    sys.exit(main())
