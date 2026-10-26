import unittest
from exercise import count_vowels


class TestStep01(unittest.TestCase):

    def test_standard(self):
        self.assertEqual(count_vowels("Hello World"), 3)

    def test_uppercase(self):
        self.assertEqual(count_vowels("PYTHON"), 1)

    def test_no_vowels(self):
        self.assertEqual(count_vowels("rhythm"), 0)

    def test_empty(self):
        self.assertEqual(count_vowels(""), 0)


if __name__ == "__main__":
    unittest.main()
