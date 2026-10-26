import ast
import inspect
import unittest
from exercise import linear_search


class TestStep04(unittest.TestCase):

    def test_found_mid(self):
        values = [14, 7, 22, 9, 7, 31]
        self.assertEqual(linear_search(values, 22), 2)

    def test_not_found(self):
        values = [14, 7, 22, 9, 7, 31]
        self.assertEqual(linear_search(values, 18), "Target not found")

    def test_found_first_occurrence(self):
        values = [14, 7, 22, 9, 7, 31]
        # 7 appears at index 1 and index 4. Must stop at first match (1)!
        self.assertEqual(linear_search(values, 7), 1)

    def test_found_at_zero(self):
        values = [100, 200, 300]
        self.assertEqual(linear_search(values, 100), 0)

    def test_no_index_method(self):
        source = inspect.getsource(linear_search)
        tree = ast.parse(source)
        for node in ast.walk(tree):
            if isinstance(node, ast.Attribute) and node.attr == "index":
                self.fail("You must NOT use the .index() method!")


if __name__ == "__main__":
    unittest.main()
