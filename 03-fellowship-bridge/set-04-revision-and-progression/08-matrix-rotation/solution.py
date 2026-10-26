"""
Master Solution for Drill 08: In-Place 90° Matrix Rotation.
Fellowship Challenge: Set 4 — Question 8
"""


def rotate_90_clockwise(matrix: list[list[int]]) -> None:
    """
    Rotates an N x N matrix 90 degrees clockwise in-place.

    Two-step First Principles strategy:
    1. Transpose: Swap matrix[r][c] with matrix[c][r] across the main diagonal.
    2. Horizontal Reflection: Reverse each row using two pointers.
    """
    n = len(matrix)
    if n <= 1:
        return

    # Step 1: Transpose in-place
    # Notice: c starts at r + 1 to only visit elements above the diagonal
    for r in range(n):
        for c in range(r + 1, n):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

    # Step 2: Reverse each row in-place (two-pointer technique)
    for row in matrix:
        left = 0
        right = n - 1
        while left < right:
            row[left], row[right] = row[right], row[left]
            left += 1
            right -= 1


if __name__ == "__main__":
    sample = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Before Rotation:")
    for row in sample:
        print(row)

    rotate_90_clockwise(sample)

    print("\nAfter 90° Clockwise Rotation:")
    for row in sample:
        print(row)
