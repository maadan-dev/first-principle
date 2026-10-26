import unittest
from exercise import reverse_integer

class TestReverseInteger(unittest.TestCase):
    def test_single_digit(self):
        self.assertEqual(reverse_integer(0), 0)
        self.assertEqual(reverse_integer(7), 7)

    def test_multi_digit(self):
        self.assertEqual(reverse_integer(1234), 4321)
        self.assertEqual(reverse_integer(100), 1)
        self.assertEqual(reverse_integer(987654321), 123456789)

if __name__ == "__main__":
    unittest.main()
