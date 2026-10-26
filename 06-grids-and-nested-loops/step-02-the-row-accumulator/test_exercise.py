import unittest
from exercise import sum_single_row

class TestSumSingleRow(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(sum_single_row([]), 0)

    def test_positive_numbers(self):
        self.assertEqual(sum_single_row([1, 2, 3, 4]), 10)

    def test_negative_numbers(self):
        self.assertEqual(sum_single_row([-5, 5, 10, -2]), 8)

if __name__ == "__main__":
    unittest.main()
