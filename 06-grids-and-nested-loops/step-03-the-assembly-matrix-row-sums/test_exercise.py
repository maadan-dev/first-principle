import unittest
from exercise import matrix_row_summary

class TestMatrixRowSummary(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(matrix_row_summary([]), ([], None, None))

    def test_matrix_row_sums(self):
        matrix = [
            [1, 2, 3],
            [10, 20, 30],
            [4, 5, 6]
        ]
        row_sums, best_idx, max_val = matrix_row_summary(matrix)
        self.assertEqual(row_sums, [6, 60, 15])
        self.assertEqual(best_idx, 1)
        self.assertEqual(max_val, 60)

    def test_matrix_with_negative_numbers(self):
        matrix = [
            [-10, -5],
            [-2, -1],
            [-20, -30]
        ]
        row_sums, best_idx, max_val = matrix_row_summary(matrix)
        self.assertEqual(row_sums, [-15, -3, -50])
        self.assertEqual(best_idx, 1)
        self.assertEqual(max_val, -3)

if __name__ == "__main__":
    unittest.main()
