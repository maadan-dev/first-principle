import unittest
from exercise import is_match


class TestStep01(unittest.TestCase):

    def test_match(self):
        self.assertTrue(is_match(22, 22))

    def test_no_match(self):
        self.assertFalse(is_match(14, 22))


if __name__ == "__main__":
    unittest.main()
