"""
Test runner for Drill 07: Roman to Integer.
Pure Python standard library (zero external dependencies).
Run with: python test_exercise.py
"""
import ast
import inspect
import sys
from exercise import roman_to_int


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

    print("\n--- Testing Drill 07: Roman to Integer ---")

    # 1. Output correctness checks
    print("\n[Stage 1: Testing Roman Numeral Conversions]")
    test_cases = [
        ("III", 3),
        ("IV", 4),
        ("IX", 9),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
        ("XL", 40),
        ("XC", 90),
        ("CD", 400),
        ("CM", 900),
        ("MMXXVI", 2026),
    ]

    for roman, expected in test_cases:
        res = roman_to_int(roman)
        check(f"'{roman}' == {expected}", res == expected, f"Got: {res}")

    # 2. Mentor Constraints
    print("\n[Stage 2: Verifying Mentor Constraints]")
    try:
        source = inspect.getsource(roman_to_int)
        parsed = ast.parse(source)

        # Constraint: must use a while loop
        has_while = any(isinstance(node, ast.While) for node in ast.walk(parsed))
        check("Uses a 'while' loop for index control", has_while, "Must use a while loop to control variable steps.")

        # Constraint: uses a dictionary
        has_dict = any(isinstance(node, ast.Dict) for node in ast.walk(parsed))
        check("Stores mappings in a dictionary", has_dict, "Define Roman numeral mappings in a dictionary.")

    except Exception as e:
        check("Code analysis", False, f"Could not inspect source: {e}")

    # Summary
    print(f"\n==========================================")
    print(f"Results: {passed}/{total} tests passed.")
    if passed == total:
        print("BIM!!! All checks passed. You conquered Question 7!")
        print("==========================================\n")
        return 0
    else:
        print("Keep going! Trace the look-ahead steps and try again.")
        print("==========================================\n")
        return 1


if __name__ == "__main__":
    sys.exit(run_tests())
