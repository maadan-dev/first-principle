import unittest
from exercise import find_most_frequent

class TestFindMostFrequent(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(find_most_frequent({}), (None, 0))

    def test_winner(self):
        counts = {"python": 4, "is": 2, "fun": 1}
        self.assertEqual(find_most_frequent(counts), ("python", 4))

    def test_single_element(self):
        self.assertEqual(find_most_frequent({"lonely": 10}), ("lonely", 10))

if __name__ == "__main__":
    unittest.main()
