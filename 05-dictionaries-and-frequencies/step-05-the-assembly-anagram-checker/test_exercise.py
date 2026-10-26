import unittest
from exercise import are_anagrams

class TestAreAnagrams(unittest.TestCase):
    def test_basic_anagrams(self):
        self.assertTrue(are_anagrams("listen", "silent"))
        self.assertTrue(are_anagrams("evil", "vile"))

    def test_case_and_spaces(self):
        self.assertTrue(are_anagrams("Dormitory", "Dirty room"))
        self.assertTrue(are_anagrams("Conversation", "Voices, rant on!"))

    def test_non_anagrams(self):
        self.assertFalse(are_anagrams("hello", "world"))
        self.assertFalse(are_anagrams("apple", "aple"))
        self.assertFalse(are_anagrams("cat", "rat"))

if __name__ == "__main__":
    unittest.main()
