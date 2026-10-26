import unittest
from exercise import count_frequencies

class TestCountFrequencies(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(count_frequencies([]), {})

    def test_fruits(self):
        items = ["apple", "banana", "apple", "orange", "banana", "apple"]
        expected = {"apple": 3, "banana": 2, "orange": 1}
        self.assertEqual(count_frequencies(items), expected)

    def test_numbers(self):
        self.assertEqual(count_frequencies([1, 1, 2, 3, 2, 1]), {1: 3, 2: 2, 3: 1})

if __name__ == "__main__":
    unittest.main()
