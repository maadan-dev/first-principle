import ast
import inspect
import unittest
from exercise import find_largest


class TestStep03(unittest.TestCase):

    def test_find_largest_standard(self):
        result = find_largest([12, 5, 27, 8, 14])
        self.assertEqual(result, 27, "Largest in [12, 5, 27, 8, 14] is 27.")

    def test_find_largest_at_beginning(self):
        result = find_largest([99, 10, 5])
        self.assertEqual(result, 99, "Should handle largest item at index 0.")

    def test_find_largest_all_negatives(self):
        result = find_largest([-50, -10, -5, -20])
        self.assertEqual(result, -5, "Largest of negative numbers [-50, -10, -5, -20] is -5.")

    def test_no_built_in_max(self):
        source = inspect.getsource(find_largest)
        tree = ast.parse(source)
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                self.assertNotEqual(node.func.id, "max", "You must NOT use built-in max()!")
                self.assertNotEqual(node.func.id, "sorted", "You must NOT use sorted()!")


if __name__ == "__main__":
    unittest.main()
