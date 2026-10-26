"""
Test runner for Drill 01: Optimized Prime Checker & Prime Sum.
Runs using pure Python standard library (no external packages required).
Run with: python test_exercise.py
"""
import ast
import inspect
import sys
from exercise import is_prime, analyze_primes


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

    print("\n--- Testing Drill 01: Optimized Primes ---")

    # 1. Check is_prime logic
    print("\n[Stage 1: Testing is_prime()]")
    check("is_prime(2) is True", is_prime(2) is True)
    check("is_prime(3) is True", is_prime(3) is True)
    check("is_prime(4) is False", is_prime(4) is False)
    check("is_prime(7) is True", is_prime(7) is True)
    check("is_prime(10) is False", is_prime(10) is False)
    check("is_prime(1) is False (edge case: 1 is not prime)", is_prime(1) is False)
    check("is_prime(0) is False (edge case)", is_prime(0) is False)
    check("is_prime(29) is True", is_prime(29) is True)
    check("is_prime(35) is False (5 * 7)", is_prime(35) is False)

    # 2. Check analyze_primes
    print("\n[Stage 2: Testing analyze_primes(N)]")
    res_10 = analyze_primes(10)
    check(
        "N = 10 returns correct tuple",
        res_10 == (False, [2, 3, 5, 7], 17),
        f"Got: {res_10}, Expected: (False, [2, 3, 5, 7], 17)"
    )

    res_7 = analyze_primes(7)
    check(
        "N = 7 returns correct tuple",
        res_7 == (True, [2, 3, 5, 7], 17),
        f"Got: {res_7}, Expected: (True, [2, 3, 5, 7], 17)"
    )

    res_2 = analyze_primes(2)
    check(
        "N = 2 returns correct tuple",
        res_2 == (True, [2], 2),
        f"Got: {res_2}, Expected: (True, [2], 2)"
    )

    # 3. Check Fellowship Constraints (AST Inspection)
    print("\n[Stage 3: Verifying Mentor Constraints]")
    try:
        source_is_prime = inspect.getsource(is_prime)
        source_analyze = inspect.getsource(analyze_primes)
        parsed_is_prime = ast.parse(source_is_prime)
        parsed_analyze = ast.parse(source_analyze)

        # Constraint: is_prime must use a While loop
        has_while = any(isinstance(node, ast.While) for node in ast.walk(parsed_is_prime))
        has_for_in_prime = any(isinstance(node, ast.For) for node in ast.walk(parsed_is_prime))
        check("is_prime uses a 'while' loop", has_while, "You must use a while loop for the primality check.")
        check("is_prime does NOT use a 'for' loop", not has_for_in_prime, "Do not use a for loop in is_prime().")

        # Constraint: no sum() function used
        all_calls = [
            node.func.id for node in ast.walk(parsed_analyze)
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
        ]
        has_sum = "sum" in all_calls
        check("Does not use built-in sum()", not has_sum, "Use an accumulator loop instead of sum().")

        # Constraint: no math imported
        import_names = [
            alias.name for node in ast.walk(parsed_analyze)
            if isinstance(node, (ast.Import, ast.ImportFrom))
            for alias in node.names
        ]
        has_math = "math" in import_names
        check("Does not import math library", not has_math, "Use i * i <= num instead of math.sqrt().")

    except Exception as e:
        check("Code analysis", False, f"Could not inspect source: {e}")

    # Summary
    print(f"\n==========================================")
    print(f"Results: {passed}/{total} tests passed.")
    if passed == total:
        print("BIM!!! All checks passed. You conquered Question 1!")
        print("==========================================\n")
        return 0
    else:
        print("Keep going! Trace the variables and try again.")
        print("==========================================\n")
        return 1


if __name__ == "__main__":
    sys.exit(run_tests())
