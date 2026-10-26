import ast
import inspect
import unittest
from exercise import find_smallest


class TestStep04(unittest.TestCase):

    def test_find_smallest_standard(self):
        result = find_smallest([12, 5, 27, 8, 14])
        self.assertEqual(result, 5, "Smallest in [12, 5, 27, 8, 14] is 5.")

    def test_find_smallest_at_end(self):
        result = find_smallest([10, 20, 2])
        self.assertEqual(result, 2, "Should handle smallest item at the end of the list.")

    def test_find_smallest_all_negatives(self):
        result = find_smallest([-10, -50, -5, -20])
        self.assertEqual(result, -50, "Smallest of [-10, -50, -5, -20] is -50.")

    def test_no_built_in_min(self):
        source = inspect.getsource(find_smallest)
        tree = ast.parse(source)
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                self.assertNotEqual(node.func.id, "min", "You must NOT use built-in min()!")
                self.assertNotEqual(node.func.id, "sorted", "You must NOT use sorted()!")


if __name__ == "__main__":
    unittest.main()
