import ast
import inspect
import unittest
from exercise import reverse_string_manual


class TestStep03(unittest.TestCase):

    def test_standard(self):
        self.assertEqual(reverse_string_manual("python"), "nohtyp")

    def test_single_char(self):
        self.assertEqual(reverse_string_manual("a"), "a")

    def test_palindrome_word(self):
        self.assertEqual(reverse_string_manual("racecar"), "racecar")

    def test_empty(self):
        self.assertEqual(reverse_string_manual(""), "")

    def test_constraints(self):
        source = inspect.getsource(reverse_string_manual)
        tree = ast.parse(source)
        for node in ast.walk(tree):
            if isinstance(node, ast.Slice):
                if node.step is not None:
                    self.fail("You must NOT use [::-1] slice reversal!")
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                self.assertNotIn(node.func.id, ["reversed"], "Do NOT use reversed()!")


if __name__ == "__main__":
    unittest.main()
