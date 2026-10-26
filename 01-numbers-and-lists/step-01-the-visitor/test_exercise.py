import unittest
from exercise import visit_all


class TestStep01(unittest.TestCase):

    def test_visit_standard_list(self):
        result = visit_all([10, 20, 30])
        self.assertEqual(result, [10, 20, 30], "Did not visit and return all items in order.")

    def test_visit_single_item(self):
        result = visit_all([42])
        self.assertEqual(result, [42], "Should handle single-item list.")

    def test_visit_empty_list(self):
        result = visit_all([])
        self.assertEqual(result, [], "Should handle an empty list.")


if __name__ == "__main__":
    unittest.main()
