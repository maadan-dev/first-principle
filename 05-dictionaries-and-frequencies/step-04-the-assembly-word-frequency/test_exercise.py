import unittest
from exercise import word_frequency_analyser

class TestWordFrequencyAnalyser(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(word_frequency_analyser(""), ({}, None, 0))

    def test_assessment_example(self):
        text = "Python is fun, and Python is powerful!"
        counts, best_word, best_count = word_frequency_analyser(text)
        self.assertEqual(counts["python"], 2)
        self.assertEqual(counts["is"], 2)
        self.assertEqual(counts["fun"], 1)
        self.assertEqual(counts["and"], 1)
        self.assertEqual(counts["powerful"], 1)
        # "python" or "is" both have 2
        self.assertIn(best_word, ["python", "is"])
        self.assertEqual(best_count, 2)

    def test_punctuation_stripping(self):
        text = "Hello! Hello? HELLO... world."
        counts, best_word, best_count = word_frequency_analyser(text)
        self.assertEqual(counts["hello"], 3)
        self.assertEqual(counts["world"], 1)
        self.assertEqual(best_word, "hello")
        self.assertEqual(best_count, 3)

if __name__ == "__main__":
    unittest.main()
