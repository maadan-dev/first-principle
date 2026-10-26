import ast
import inspect
import unittest
from exercise import find_all_occurrences


class TestStep05(unittest.TestCase):

    def test_multiple_occurrences(self):
        values = [14, 7, 22, 9, 7, 31, 7]
        self.assertEqual(find_all_occurrences(values, 7), [1, 4, 6])

    def test_single_occurrence(self):
        values = [14, 7, 22, 9]
        self.assertEqual(find_all_occurrences(values, 22), [2])

    def test_no_occurrence(self):
        values = [14, 7, 22]
        self.assertEqual(find_all_occurrences(values, 99), [])

    def test_constraints(self):
        source = inspect.getsource(find_all_occurrences)
        tree = ast.parse(source)
        for node in ast.walk(tree):
            if isinstance(node, ast.Attribute) and node.attr in ["index", "count"]:
                self.fail(f"You must NOT use .{node.attr}()!")
            if isinstance(node, ast.ListComp):
                self.fail("You must NOT use list comprehensions; use a manual loop!")


if __name__ == "__main__":
    unittest.main()
