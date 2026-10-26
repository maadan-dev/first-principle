"""
Master Solution for Drill 04: Matrix Multiplication.
Fellowship Challenge: Set 4 — Question 4
"""


def multiply_matrices(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    """
    Multiplies matrix A (m x k) by matrix B (k x n) into matrix C (m x n)
    using 3 nested loops.
    """
    rows_a = len(a)
    cols_a = len(a[0])
    rows_b = len(b)
    cols_b = len(b[0])

    if cols_a != rows_b:
        raise ValueError(f"Incompatible dimensions: A has {cols_a} cols, B has {rows_b} rows")

    # Step 1: Initialize result matrix of size rows_a x cols_b without list comprehensions
    result = []
    for _ in range(rows_a):
        row = []
        for _ in range(cols_b):
            row.append(0)
        result.append(row)

    # Step 2: 3-loop accumulation engine
    for i in range(rows_a):
        for j in range(cols_b):
            cell_sum = 0
            for k in range(cols_a):
                cell_sum += a[i][k] * b[k][j]
            result[i][j] = cell_sum

    return result


if __name__ == "__main__":
    mat_a = [[1, 2], [3, 4]]
    mat_b = [[5, 6], [7, 8]]
    prod = multiply_matrices(mat_a, mat_b)
    print("Product Matrix:")
    for r in prod:
        print(r)
