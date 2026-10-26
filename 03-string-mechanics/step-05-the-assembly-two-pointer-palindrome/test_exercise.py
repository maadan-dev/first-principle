import ast
import inspect
import unittest
from exercise import is_palindrome_sentence


class TestStep05(unittest.TestCase):

    def test_fellowship_palindromes(self):
        self.assertTrue(is_palindrome_sentence("Was it a car or a cat I saw?"))
        self.assertTrue(is_palindrome_sentence("No 'x' in Nixon"))
        self.assertTrue(is_palindrome_sentence("Madam, I'm Adam."))
        self.assertTrue(is_palindrome_sentence("A man, a plan, a canal: Panama!"))

    def test_non_palindromes(self):
        self.assertFalse(is_palindrome_sentence("Hello, World!"))
        self.assertFalse(is_palindrome_sentence("This is not a palindrome."))

    def test_empty_or_punctuation_only(self):
        self.assertTrue(is_palindrome_sentence("   "))
        self.assertTrue(is_palindrome_sentence("!.,?"))

    def test_constraints(self):
        source = inspect.getsource(is_palindrome_sentence)
        tree = ast.parse(source)
        for node in ast.walk(tree):
            if isinstance(node, ast.Slice) and node.step is not None:
                self.fail("You must NOT use [::-1] slice reversal!")
            if isinstance(node, ast.Attribute) and node.attr == "reverse":
                self.fail("Do not use .reverse()!")


if __name__ == "__main__":
    unittest.main()
