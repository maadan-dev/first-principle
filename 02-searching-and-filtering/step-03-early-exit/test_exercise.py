import unittest
from exercise import find_first_negative


class TestStep03(unittest.TestCase):

    def test_find_first_negative(self):
        self.assertEqual(find_first_negative([4, 7, -2, 9, -5]), -2)

    def test_none_found(self):
        self.assertIsNone(find_first_negative([1, 2, 3]))

    def test_negative_at_start(self):
        self.assertEqual(find_first_negative([-10, 5, 20]), -10)


if __name__ == "__main__":
    unittest.main()
