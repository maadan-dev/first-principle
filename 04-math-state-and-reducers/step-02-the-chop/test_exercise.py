import unittest
from exercise import chop_last_digit

class TestChopLastDigit(unittest.TestCase):
    def test_single_digit(self):
        self.assertEqual(chop_last_digit(5), 0)
        self.assertEqual(chop_last_digit(9), 0)

    def test_multi_digit(self):
        self.assertEqual(chop_last_digit(42), 4)
        self.assertEqual(chop_last_digit(1234), 123)
        self.assertEqual(chop_last_digit(98765), 9876)

if __name__ == "__main__":
    unittest.main()
