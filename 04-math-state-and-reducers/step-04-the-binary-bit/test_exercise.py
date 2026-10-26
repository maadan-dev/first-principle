import unittest
from exercise import get_binary_bit_and_chop

class TestBinaryBitAndChop(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(get_binary_bit_and_chop(13), (1, 6))
        self.assertEqual(get_binary_bit_and_chop(6), (0, 3))
        self.assertEqual(get_binary_bit_and_chop(3), (1, 1))
        self.assertEqual(get_binary_bit_and_chop(1), (1, 0))

if __name__ == "__main__":
    unittest.main()
