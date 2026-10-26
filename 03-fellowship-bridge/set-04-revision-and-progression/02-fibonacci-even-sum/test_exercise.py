"""
Test runner for Drill 02: Fibonacci Sequence — Even Sum & Inverted Stream.
Pure Python standard library (zero external dependencies).
Run with: python test_exercise.py
"""
import ast
import inspect
import sys
from exercise import fibonacci_analysis


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

    print("\n--- Testing Drill 02: Fibonacci Even Sum & Inverted Stream ---")

    # 1. Output correctness checks
    print("\n[Stage 1: Testing Fibonacci Output & Logic]")
    res_8 = fibonacci_analysis(8)
    expected_8 = ("0, 1, 1, 2, 3, 5, 8, 13", 10, "13, 8, 5, 3, 2, 1, 1, 0")
    check(
        "N = 8 output matches spec",
        res_8 == expected_8,
        f"Got: {res_8}\n         Expected: {expected_8}"
    )

    res_1 = fibonacci_analysis(1)
    expected_1 = ("0", 0, "0")
    check(
        "N = 1 (single element base case)",
        res_1 == expected_1,
        f"Got: {res_1}\n         Expected: {expected_1}"
    )

    res_4 = fibonacci_analysis(4)
    expected_4 = ("0, 1, 1, 2", 2, "2, 1, 1, 0")
    check(
        "N = 4 output matches spec",
        res_4 == expected_4,
        f"Got: {res_4}\n         Expected: {expected_4}"
    )

    # 2. Mentor Constraints
    print("\n[Stage 2: Verifying Mentor Constraints]")
    try:
        source = inspect.getsource(fibonacci_analysis)
        parsed = ast.parse(source)

        # Constraint: Uses loop, not recursion
        has_loop = any(isinstance(node, (ast.For, ast.While)) for node in ast.walk(parsed))
        check("Generates sequence using a loop", has_loop, "Must use a for or while loop.")

        # Check self-recursion
        recursive_calls = [
            node.func.id for node in ast.walk(parsed)
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "fibonacci_analysis"
        ]
        check("Does not use recursion", len(recursive_calls) == 0, "Do not call fibonacci_analysis recursively.")

        # Constraint: no sum()
        all_calls = [
            node.func.id for node in ast.walk(parsed)
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
        ]
        check("Does not use built-in sum()", "sum" not in all_calls, "Accumulate even numbers manually.")

        # Constraint: no .reverse() or reversed()
        check("Does not use reversed()", "reversed" not in all_calls, "Do not use reversed().")
        method_calls = [
            node.attr for node in ast.walk(parsed)
            if isinstance(node, ast.Attribute)
        ]
        check("Does not use .reverse() method", "reverse" not in method_calls, "Do not use .reverse().")

        # Constraint: no [::-1]
        has_negative_slice = False
        for node in ast.walk(parsed):
            if isinstance(node, ast.Slice) and node.step is not None:
                if isinstance(node.step, ast.UnaryOp) and isinstance(node.step.op, ast.USub):
                    has_negative_slice = True
                elif isinstance(node.step, ast.Constant) and node.step.value == -1:
                    has_negative_slice = True
        check("Does not use [::-1] slice step", not has_negative_slice, "Reverse string via prepending.")

    except Exception as e:
        check("Code analysis", False, f"Could not inspect source: {e}")

    # Summary
    print(f"\n==========================================")
    print(f"Results: {passed}/{total} tests passed.")
    if passed == total:
        print("BIM!!! All checks passed. You conquered Question 2!")
        print("==========================================\n")
        return 0
    else:
        print("Keep going! Trace the variables and try again.")
        print("==========================================\n")
        return 1


if __name__ == "__main__":
    sys.exit(run_tests())
