"""
Test runner for Drill 08: In-Place 90° Matrix Rotation.
Pure Python standard library (zero external dependencies).
Run with: python test_exercise.py
"""
import ast
import inspect
import sys
from exercise import rotate_90_clockwise


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

    print("\n--- Testing Drill 08: In-Place 90° Matrix Rotation ---")

    # 1. Output correctness checks
    print("\n[Stage 1: Testing Rotation Correctness]")
    m3 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    id_before = id(m3)
    rotate_90_clockwise(m3)
    expected_3 = [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3]
    ]
    check("3x3 Matrix rotated correctly", m3 == expected_3, f"Got: {m3}")
    check("In-place check: object ID did not change", id(m3) == id_before, "Matrix must be modified in-place.")

    m2 = [
        [1, 2],
        [3, 4]
    ]
    rotate_90_clockwise(m2)
    expected_2 = [
        [3, 1],
        [4, 2]
    ]
    check("2x2 Matrix rotated correctly", m2 == expected_2, f"Got: {m2}")

    m4 = [
        [ 5,  1,  9, 11],
        [ 2,  4,  8, 10],
        [13,  3,  6,  7],
        [15, 14, 12, 16]
    ]
    rotate_90_clockwise(m4)
    expected_4 = [
        [15, 13,  2,  5],
        [14,  3,  4,  1],
        [12,  6,  8,  9],
        [16,  7, 10, 11]
    ]
    check("4x4 Matrix rotated correctly", m4 == expected_4, f"Got: {m4}")

    # 2. Mentor Constraints
    print("\n[Stage 2: Verifying Mentor Constraints]")
    try:
        source = inspect.getsource(rotate_90_clockwise)
        parsed = ast.parse(source)

        all_calls = [
            node.func.id for node in ast.walk(parsed)
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
        ]
        all_attrs = [
            node.attr for node in ast.walk(parsed)
            if isinstance(node, ast.Attribute)
        ]

        # Check reversed / reverse
        check("Does not use reversed()", "reversed" not in all_calls, "Do not use reversed().")
        check("Does not use .reverse()", "reverse" not in all_attrs, "Do not use .reverse().")

        # Check [::-1]
        has_negative_slice = False
        for node in ast.walk(parsed):
            if isinstance(node, ast.Slice) and node.step is not None:
                if isinstance(node.step, ast.UnaryOp) and isinstance(node.step.op, ast.USub):
                    has_negative_slice = True
                elif isinstance(node.step, ast.Constant) and node.step.value == -1:
                    has_negative_slice = True
        check("Does not use [::-1] slice step", not has_negative_slice, "Reverse rows with two pointers.")

        # Check nested loops
        for_count = sum(1 for node in ast.walk(parsed) if isinstance(node, (ast.For, ast.While)))
        check("Uses multiple loop structures", for_count >= 2, "Use nested loops for transpose and reversal.")

    except Exception as e:
        check("Code analysis", False, f"Could not inspect source: {e}")

    # Summary
    print(f"\n==========================================")
    print(f"Results: {passed}/{total} tests passed.")
    if passed == total:
        print("BIM!!! All checks passed. You conquered Question 8!")
        print("==========================================\n")
        return 0
    else:
        print("Keep going! Trace the transpose and swap steps.")
        print("==========================================\n")
        return 1


if __name__ == "__main__":
    sys.exit(run_tests())
