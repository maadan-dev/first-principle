"""
Test runner for Drill 05: ASCII Word Capitalizer & Space Stripper.
Pure Python standard library (zero external dependencies).
Run with: python test_exercise.py
"""
import ast
import inspect
import sys
from exercise import to_upper_ascii, format_sentence


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

    print("\n--- Testing Drill 05: ASCII Capitalizer & Space Stripper ---")

    # 1. ASCII Helper Tests
    print("\n[Stage 1: Testing to_upper_ascii()]")
    check("to_upper_ascii('a') == 'A'", to_upper_ascii('a') == 'A')
    check("to_upper_ascii('z') == 'Z'", to_upper_ascii('z') == 'Z')
    check("to_upper_ascii('m') == 'M'", to_upper_ascii('m') == 'M')
    check("to_upper_ascii('A') == 'A' (already upper)", to_upper_ascii('A') == 'A')
    check("to_upper_ascii('!') == '!' (punctuation)", to_upper_ascii('!') == '!')

    # 2. Sentence Formatting Tests
    print("\n[Stage 2: Testing format_sentence()]")
    res1 = format_sentence("hello world from python")
    if isinstance(res1, (tuple, list)) and len(res1) == 2:
        c1, s1 = res1
        check(
            "Standard sentence formatting",
            c1 == "Hello World From Python" and s1 == "HelloWorldFromPython",
            f"Got: ({c1!r}, {s1!r})"
        )
    else:
        check("Standard sentence formatting", False, f"Expected tuple of 2 strings, got: {res1!r}")

    res2 = format_sentence("python is amazing")
    if isinstance(res2, (tuple, list)) and len(res2) == 2:
        c2, s2 = res2
        check(
            "Three word sentence",
            c2 == "Python Is Amazing" and s2 == "PythonIsAmazing",
            f"Got: ({c2!r}, {s2!r})"
        )
    else:
        check("Three word sentence", False, f"Expected tuple of 2 strings, got: {res2!r}")

    res3 = format_sentence("already Capitalized")
    if isinstance(res3, (tuple, list)) and len(res3) == 2:
        c3, s3 = res3
        check(
            "Handles already capitalized words",
            c3 == "Already Capitalized" and s3 == "AlreadyCapitalized",
            f"Got: ({c3!r}, {s3!r})"
        )
    else:
        check("Handles already capitalized words", False, f"Expected tuple of 2 strings, got: {res3!r}")

    # 3. Mentor Constraints
    print("\n[Stage 3: Verifying Mentor Constraints]")
    try:
        source_format = inspect.getsource(format_sentence)
        source_upper = inspect.getsource(to_upper_ascii)
        parsed_format = ast.parse(source_format)
        parsed_upper = ast.parse(source_upper)

        # Check .replace()
        all_attrs = [
            node.attr for node in ast.walk(parsed_format)
            if isinstance(node, ast.Attribute)
        ]
        check("Does not use .replace()", "replace" not in all_attrs, "Do not use .replace() to remove spaces.")

        # Check .title() and .capitalize()
        check("Does not use .title()", "title" not in all_attrs, "Do not use .title().")
        check("Does not use .capitalize()", "capitalize" not in all_attrs, "Do not use .capitalize().")
        check("Does not use .upper()", "upper" not in all_attrs, "Use ASCII math (ord/chr - 32) instead.")

        # Check ord() and chr() in ASCII helper
        upper_calls = [
            node.func.id for node in ast.walk(parsed_upper)
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
        ]
        check("Uses ord() in to_upper_ascii", "ord" in upper_calls, "Use ord() to get ASCII code.")
        check("Uses chr() in to_upper_ascii", "chr" in upper_calls, "Use chr() to convert ASCII code back.")

    except Exception as e:
        check("Code analysis", False, f"Could not inspect source: {e}")

    # Summary
    print(f"\n==========================================")
    print(f"Results: {passed}/{total} tests passed.")
    if passed == total:
        print("BIM!!! All checks passed. You conquered Question 5!")
        print("==========================================\n")
        return 0
    else:
        print("Keep going! Trace the state machine and try again.")
        print("==========================================\n")
        return 1


if __name__ == "__main__":
    sys.exit(run_tests())
