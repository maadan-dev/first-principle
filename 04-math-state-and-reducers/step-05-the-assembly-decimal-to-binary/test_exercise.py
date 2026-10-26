import unittest
from exercise import decimal_to_binary

class TestDecimalToBinary(unittest.TestCase):
    def test_zero_and_one(self):
        self.assertEqual(decimal_to_binary(0), "0")
        self.assertEqual(decimal_to_binary(1), "1")

    def test_assessment_examples(self):
        self.assertEqual(decimal_to_binary(10), "1010")
        self.assertEqual(decimal_to_binary(25), "11001")
        self.assertEqual(decimal_to_binary(42), "101010")

    def test_powers_of_two(self):
        self.assertEqual(decimal_to_binary(2), "10")
        self.assertEqual(decimal_to_binary(4), "100")
        self.assertEqual(decimal_to_binary(8), "1000")
        self.assertEqual(decimal_to_binary(16), "10000")

if __name__ == "__main__":
    unittest.main()
