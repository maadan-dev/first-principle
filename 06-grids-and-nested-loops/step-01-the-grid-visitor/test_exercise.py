import unittest
from exercise import flatten_grid

class TestFlattenGrid(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(flatten_grid([]), [])

    def test_square_matrix(self):
        m = [
            [1, 2],
            [3, 4]
        ]
        self.assertEqual(flatten_grid(m), [1, 2, 3, 4])

    def test_rectangular_matrix(self):
        m = [
            [10, 20, 30],
            [40, 50, 60]
        ]
        self.assertEqual(flatten_grid(m), [10, 20, 30, 40, 50, 60])

if __name__ == "__main__":
    unittest.main()
