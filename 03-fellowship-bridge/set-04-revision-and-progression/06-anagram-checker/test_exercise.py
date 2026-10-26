"""
Test runner for Drill 06: Anagram Checker.
Pure Python standard library (zero external dependencies).
Run with: python test_exercise.py
"""
import ast
import inspect
import sys
from exercise import build_frequency_map, is_anagram


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

    print("\n--- Testing Drill 06: Anagram Checker ---")

    # 1. Frequency Map Tests
    print("\n[Stage 1: Testing build_frequency_map()]")
    f_abc = build_frequency_map("aab")
    check(
        "Tally for 'aab'",
        f_abc == {'a': 2, 'b': 1},
        f"Got: {f_abc}, Expected: {{'a': 2, 'b': 1}}"
    )
    f_case = build_frequency_map("Aa")
    check(
        "Handles case-insensitivity ('Aa' -> {'a': 2})",
        f_case == {'a': 2},
        f"Got: {f_case}, Expected: {{'a': 2}}"
    )

    # 2. Anagram Tests
    print("\n[Stage 2: Testing is_anagram()]")
    check("listen vs silent -> True", is_anagram("listen", "silent") is True)
    check("hello vs world -> False", is_anagram("hello", "world") is False)
    check("Dormitory vs dirtyroom -> True", is_anagram("Dormitory", "dirtyroom") is True)
    check("Conversation vs Voices rant on -> True", is_anagram("Conversation", "Voices rant on") is True)
    check("rat vs car -> False", is_anagram("rat", "car") is False)
    check("a vs aa -> False (different frequencies)", is_anagram("a", "aa") is False)

    # 3. Mentor Constraints
    print("\n[Stage 3: Verifying Mentor Constraints]")
    try:
        source_build = inspect.getsource(build_frequency_map)
        source_anagram = inspect.getsource(is_anagram)
        parsed = ast.parse(source_build + "\n" + source_anagram)

        all_calls = [
            node.func.id for node in ast.walk(parsed)
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
        ]
        all_attrs = [
            node.attr for node in ast.walk(parsed)
            if isinstance(node, ast.Attribute)
        ]

        # Check sort() and sorted()
        check("Does not use sorted()", "sorted" not in all_calls, "Do not use sorted().")
        check("Does not use .sort()", "sort" not in all_attrs, "Do not use .sort().")

        # Check set()
        check("Does not use set()", "set" not in all_calls, "Do not use set().")

        # Check collections.Counter
        import_names = [
            alias.name for node in ast.walk(parsed)
            if isinstance(node, (ast.Import, ast.ImportFrom))
            for alias in node.names
        ]
        check("Does not import Counter", "Counter" not in import_names, "Build frequency dictionary manually.")

    except Exception as e:
        check("Code analysis", False, f"Could not inspect source: {e}")

    # Summary
    print(f"\n==========================================")
    print(f"Results: {passed}/{total} tests passed.")
    if passed == total:
        print("BIM!!! All checks passed. You conquered Question 6!")
        print("==========================================\n")
        return 0
    else:
        print("Keep going! Trace the frequency maps and try again.")
        print("==========================================\n")
        return 1


if __name__ == "__main__":
    sys.exit(run_tests())
