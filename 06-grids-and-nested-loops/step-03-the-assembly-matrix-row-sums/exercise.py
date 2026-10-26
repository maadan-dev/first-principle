def matrix_row_summary(matrix: list[list[int]]) -> tuple[list[int], int, int]:
    """
    Calculates the sum of each row in a matrix, returning:
    (list_of_row_sums, best_row_index, max_row_sum)

    Example:
        matrix = [
            [1, 2, 3],     # sum = 6
            [10, 20, 30],  # sum = 60 (highest!)
            [4, 5, 6]      # sum = 15
        ]
        matrix_row_summary(matrix) -> ([6, 60, 15], 1, 60)

    Constraints:
        Do NOT use built-in sum() or max().
        Do NOT use list comprehensions.
        Use nested loops and the Champion Pattern.
    """
    # TODO: Handle empty matrix: if not matrix, return ([], None, None)
    # TODO: Initialize row_sums = []
    # TODO: Initialize best_row_index = 0, max_row_sum = None
    # TODO: Outer loop over rows:
    #       - Initialize row_total = 0
    #       - Inner loop over numbers in row:
    #           - row_total += num
    #       - Append row_total to row_sums
    #       - If max_row_sum is None or row_total > max_row_sum:
    #           - max_row_sum = row_total
    #           - best_row_index = current_index
    # TODO: Return (row_sums, best_row_index, max_row_sum)
    pass
