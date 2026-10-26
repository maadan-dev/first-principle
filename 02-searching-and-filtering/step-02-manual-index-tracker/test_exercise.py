import ast
import inspect
import unittest
from exercise import pair_with_indices


class TestStep02(unittest.TestCase):

    def test_standard(self):
        items = ["apple", "banana", "cherry"]
        expected = [(0, "apple"), (1, "banana"), (2, "cherry")]
        self.assertEqual(pair_with_indices(items), expected)

    def test_empty(self):
        self.assertEqual(pair_with_indices([]), [])

    def test_no_index_method(self):
        source = inspect.getsource(pair_with_indices)
        tree = ast.parse(source)
        for node in ast.walk(tree):
            if isinstance(node, ast.Attribute) and node.attr == "index":
                self.fail("You must NOT use the .index() method!")


if __name__ == "__main__":
    unittest.main()
