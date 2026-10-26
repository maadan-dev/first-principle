import ast
import inspect
import unittest
from exercise import calculate_total


class TestStep02(unittest.TestCase):

    def test_calculate_total_standard(self):
        result = calculate_total([12, 5, 27, 8, 14])
        self.assertEqual(result, 66, "Sum of [12, 5, 27, 8, 14] should be 66.")

    def test_calculate_total_empty(self):
        result = calculate_total([])
        self.assertEqual(result, 0, "Sum of empty list should be 0.")

    def test_calculate_total_negatives(self):
        result = calculate_total([10, -5, 20])
        self.assertEqual(result, 25, "Should handle negative numbers correctly.")

    def test_no_built_in_sum(self):
        source = inspect.getsource(calculate_total)
        tree = ast.parse(source)
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                self.assertNotEqual(node.func.id, "sum", "You must NOT use the built-in sum() function!")


if __name__ == "__main__":
    unittest.main()
