import ast
import inspect
import unittest
from exercise import is_simple_palindrome


class TestStep04(unittest.TestCase):

    def test_palindromes(self):
        self.assertTrue(is_simple_palindrome("racecar"))
        self.assertTrue(is_simple_palindrome("noon"))
        self.assertTrue(is_simple_palindrome("a"))
        self.assertTrue(is_simple_palindrome(""))

    def test_non_palindromes(self):
        self.assertFalse(is_simple_palindrome("hello"))
        self.assertFalse(is_simple_palindrome("python"))

    def test_uses_while_loop(self):
        source = inspect.getsource(is_simple_palindrome)
        tree = ast.parse(source)
        has_while = any(isinstance(node, ast.While) for node in ast.walk(tree))
        self.assertTrue(has_while, "You must use a 'while left < right:' two-pointer loop!")


if __name__ == "__main__":
    unittest.main()
