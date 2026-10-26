import unittest
from exercise import safe_lookup

class TestSafeLookup(unittest.TestCase):
    def test_existing_key(self):
        d = {"a": 10, "b": 20}
        self.assertEqual(safe_lookup(d, "a", 0), 10)
        self.assertEqual(safe_lookup(d, "b", -1), 20)

    def test_missing_key(self):
        d = {"a": 10}
        self.assertEqual(safe_lookup(d, "z", 0), 0)
        self.assertEqual(safe_lookup(d, "missing", 999), 999)

if __name__ == "__main__":
    unittest.main()
