"""
Drill 08: In-Place 90° Matrix Rotation
Fellowship Challenge: Set 4 — Question 8

CONSTRAINTS:
1. In-place only: modify the existing matrix directly. Do not return a new list.
2. Do not use [::-1] or reversed() to reverse rows.
3. Use nested loops.
4. Do not import any libraries.
"""


def rotate_90_clockwise(matrix: list[list[int]]) -> None:
    """
    Rotates an N x N matrix 90 degrees clockwise in-place.
    Modifies matrix directly and returns None.

    Example:
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        rotate_90_clockwise(matrix)
        # matrix is now:
        # [
        #     [7, 4, 1],
        #     [8, 5, 2],
        #     [9, 6, 3]
        # ]
    """
    n = len(matrix)
    if n <= 1:
        return

    # TODO: Step 1 - Transpose matrix in-place (swap matrix[r][c] with matrix[c][r])
    #       Hint: Outer loop r from 0 to n, inner loop c from r + 1 to n

    # TODO: Step 2 - Reverse each row in-place using two pointers (left and right)
    #       Hint: For each row in matrix:
    #                 left = 0, right = n - 1
    #                 while left < right:
    #                     swap row[left] and row[right]
    #                     left += 1
    #                     right -= 1
    pass


if __name__ == "__main__":
    sample = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Original:")
    for r in sample:
        print(r)

    rotate_90_clockwise(sample)

    print("\nRotated 90° Clockwise:")
    for r in sample:
        print(r)
