"""
Test runner for Drill 04: Matrix Multiplication.
Pure Python standard library (zero external dependencies).
Run with: python test_exercise.py
"""
import ast
import inspect
import sys
from exercise import multiply_matrices


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

    print("\n--- Testing Drill 04: Matrix Multiplication ---")

    # 1. Output correctness checks
    print("\n[Stage 1: Testing Matrix Product Calculation]")
    a1 = [[1, 2], [3, 4]]
    b1 = [[5, 6], [7, 8]]
    expected_1 = [[19, 22], [43, 50]]
    res_1 = multiply_matrices(a1, b1)
    check("2x2 matrix product", res_1 == expected_1, f"Got: {res_1}")

    # Rectangular: 2x3 * 3x2 -> 2x2
    a2 = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    b2 = [
        [7, 8],
        [9, 1],
        [2, 3]
    ]
    # [1*7+2*9+3*2, 1*8+2*1+3*3] = [7+18+6, 8+2+9] = [31, 19]
    # [4*7+5*9+6*2, 4*8+5*1+6*3] = [28+45+12, 32+5+18] = [85, 55]
    expected_2 = [
        [31, 19],
        [85, 55]
    ]
    res_2 = multiply_matrices(a2, b2)
    check("2x3 times 3x2 rectangular product", res_2 == expected_2, f"Got: {res_2}")

    # Incompatible dimensions
    try:
        multiply_matrices([[1, 2]], [[3, 4]])
        check("Dimension mismatch raises ValueError", False, "Should raise ValueError")
    except ValueError:
        check("Dimension mismatch raises ValueError", True)

    # 2. Mentor Constraints
    print("\n[Stage 2: Verifying Mentor Constraints]")
    try:
        source = inspect.getsource(multiply_matrices)
        parsed = ast.parse(source)

        # Check list comprehension
        has_list_comp = any(isinstance(node, ast.ListComp) for node in ast.walk(parsed))
        check("Does NOT use list comprehensions", not has_list_comp, "Build lists manually using append and loops.")

        # Check numpy
        import_names = [
            alias.name for node in ast.walk(parsed)
            if isinstance(node, (ast.Import, ast.ImportFrom))
            for alias in node.names
        ]
        check("Does not import numpy", "numpy" not in import_names, "Do not use numpy.")

        # Check loop depth (at least 3 loop nodes)
        loop_nodes = [node for node in ast.walk(parsed) if isinstance(node, (ast.For, ast.While))]
        check("Uses at least 3 loops for calculation", len(loop_nodes) >= 3, "Matrix multiplication requires 3 loops.")

    except Exception as e:
        check("Code analysis", False, f"Could not inspect source: {e}")

    # Summary
    print(f"\n==========================================")
    print(f"Results: {passed}/{total} tests passed.")
    if passed == total:
        print("BIM!!! All checks passed. You conquered Question 4!")
        print("==========================================\n")
        return 0
    else:
        print("Keep going! Trace the 3-loop indices (i, j, k) and try again.")
        print("==========================================\n")
        return 1


if __name__ == "__main__":
    sys.exit(run_tests())
