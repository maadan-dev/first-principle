import unittest
from exercise import clean_letters_only


class TestStep02(unittest.TestCase):

    def test_fellowship_sentence(self):
        text = "Was it a car or a cat I saw?"
        self.assertEqual(clean_letters_only(text), "wasitacaroracatisaw")

    def test_punctuation_and_spaces(self):
        text = "Hello, World! 123"
        self.assertEqual(clean_letters_only(text), "helloworld123")

    def test_empty(self):
        self.assertEqual(clean_letters_only(""), "")


if __name__ == "__main__":
    unittest.main()
