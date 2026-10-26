"""
Test runner for Drill 03: Decimal to Binary.
Pure Python standard library (zero external dependencies).
Run with: python test_exercise.py
"""
import ast
import inspect
import sys
from exercise import decimal_to_binary


def run_tests():
    passed = 0
    total = 0

    def check(name, condition, error_detail=""):
        nonlocal passed, total
        total += 1
        if condition:
            print(f"  [PASS] {name}")
            passed += 1
        else:
            print(f"  [FAIL] {name}")
            if error_detail:
                print(f"         -> {error_detail}")

    print("\n--- Testing Drill 03: Decimal to Binary ---")

    # 1. Output correctness checks
    print("\n[Stage 1: Testing Conversion Output]")
    test_cases = [
        (10, "1010"),
        (25, "11001"),
        (1, "1"),
        (0, "0"),
        (2, "10"),
        (7, "111"),
        (16, "10000"),
        (63, "111111"),
    ]

    for val, expected in test_cases:
        res = decimal_to_binary(val)
        check(f"decimal_to_binary({val}) == '{expected}'", res == expected, f"Got: '{res}'")

    # 2. Mentor Constraints
    print("\n[Stage 2: Verifying Mentor Constraints]")
    try:
        source = inspect.getsource(decimal_to_binary)
        parsed = ast.parse(source)

        all_calls = [
            node.func.id for node in ast.walk(parsed)
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
        ]

        # Constraint: no bin()
        check("Does not use bin()", "bin" not in all_calls, "Do not use built-in bin().")

        # Constraint: no f"{...:b}"
        has_binary_format = False
        for node in ast.walk(parsed):
            if isinstance(node, ast.FormattedValue) and node.format_spec is not None:
                has_binary_format = True
        check("Does not use format string conversion (:b)", not has_binary_format, "Use pure math (% and //).")

        # Constraint: uses a loop
        has_loop = any(isinstance(node, (ast.For, ast.While)) for node in ast.walk(parsed))
        check("Uses a loop to divide by 2", has_loop, "Use a while loop to repeatedly divide by 2.")

    except Exception as e:
        check("Code analysis", False, f"Could not inspect source: {e}")

    # Summary
    print(f"\n==========================================")
    print(f"Results: {passed}/{total} tests passed.")
    if passed == total:
        print("BIM!!! All checks passed. You conquered Question 3!")
        print("==========================================\n")
        return 0
    else:
        print("Keep going! Trace the remainders and try again.")
        print("==========================================\n")
        return 1


if __name__ == "__main__":
    sys.exit(run_tests())
