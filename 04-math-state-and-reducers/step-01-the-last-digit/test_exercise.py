import unittest
from exercise import get_last_digit

class TestGetLastDigit(unittest.TestCase):
    def test_single_digit(self):
        self.assertEqual(get_last_digit(7), 7)
        self.assertEqual(get_last_digit(0), 0)

    def test_multi_digit(self):
        self.assertEqual(get_last_digit(42), 2)
        self.assertEqual(get_last_digit(1234), 4)
        self.assertEqual(get_last_digit(987650), 0)

if __name__ == "__main__":
    unittest.main()
