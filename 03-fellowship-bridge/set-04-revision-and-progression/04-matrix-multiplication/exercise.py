"""
Drill 04: Matrix Multiplication (3-Tier Nested Loops)
Fellowship Challenge: Set 4 — Question 4

CONSTRAINTS:
1. Use nested loops (three levels of loops are needed).
2. Do not import libraries such as numpy.
3. Do not use list comprehensions.
4. Dynamically build the result matrix based on dimensions.
"""


def multiply_matrices(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    """
    Multiplies matrix A (size m x k) by matrix B (size k x n).
    Returns result matrix C (size m x n).
    Raises ValueError if cols of A != rows of B.

    Example:
        A = [[1, 2], [3, 4]]
        B = [[5, 6], [7, 8]]
        multiply_matrices(A, B) -> [[19, 22], [43, 50]]
    """
    rows_a = len(a)
    cols_a = len(a[0])
    rows_b = len(b)
    cols_b = len(b[0])

    if cols_a != rows_b:
        raise ValueError(f"Incompatible dimensions: {cols_a} cols != {rows_b} rows")

    # TODO: Step 1 - Initialize the result matrix of size rows_a x cols_b filled with 0s
    #       (Reminder: do NOT use list comprehensions like [[0]*cols_b for _ in ...])

    # TODO: Step 2 - Use three nested loops:
    #       for i in range(rows_a):        # iterate through rows of A
    #           for j in range(cols_b):    # iterate through cols of B
    #               cell_sum = 0
    #               for k in range(cols_a): # iterate across row i and down col j
    #                   cell_sum += a[i][k] * b[k][j]
    #               result[i][j] = cell_sum

    # TODO: Step 3 - Return result matrix
    pass


if __name__ == "__main__":
    mat_a = [[1, 2], [3, 4]]
    mat_b = [[5, 6], [7, 8]]
    prod = multiply_matrices(mat_a, mat_b)
    print("Product Matrix:")
    for r in prod:
        print(r)
