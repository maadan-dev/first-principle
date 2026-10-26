import ast
import inspect
import unittest
from exercise import analyse_list


class TestStep05(unittest.TestCase):

    def test_fellowship_example(self):
        numbers = [12, 5, 27, 8, 14]
        res = analyse_list(numbers)
        self.assertIsInstance(res, dict, "Must return a dictionary.")
        self.assertEqual(res["smallest"], 5, "Smallest should be 5.")
        self.assertEqual(res["largest"], 27, "Largest should be 27.")
        self.assertEqual(res["total"], 66, "Total should be 66.")
        self.assertAlmostEqual(res["average"], 13.2, places=2, msg="Average should be 13.2.")

    def test_single_element(self):
        numbers = [42]
        res = analyse_list(numbers)
        self.assertEqual(res["smallest"], 42)
        self.assertEqual(res["largest"], 42)
        self.assertEqual(res["total"], 42)
        self.assertEqual(res["average"], 42.0)

    def test_with_negatives(self):
        numbers = [-10, 0, 10]
        res = analyse_list(numbers)
        self.assertEqual(res["smallest"], -10)
        self.assertEqual(res["largest"], 10)
        self.assertEqual(res["total"], 0)
        self.assertEqual(res["average"], 0.0)

    def test_mentor_constraints(self):
        source = inspect.getsource(analyse_list)
        tree = ast.parse(source)
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                self.assertNotIn(
                    node.func.id,
                    ["min", "max", "sum", "sorted"],
                    f"Forbidden built-in function '{node.func.id}' used!"
                )


if __name__ == "__main__":
    unittest.main()
