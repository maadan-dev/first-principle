"""
Step 04: The Assembly — Linear Search
Track: 02-searching-and-filtering

FELLOWSHIP CHALLENGE: Question 2

CONSTRAINTS:
1. Use a loop; do NOT use the list's .index() method.
2. Stop searching once the first match is found.
3. If not found, return "Target not found".
"""


def linear_search(values: list[int], target: int) -> int | str:
    """
    Searches values one item at a time. Returns the index where target
    first appears, or 'Target not found' if absent.

    Examples:
        linear_search([14, 7, 22, 9, 7, 31], 22) -> 2
        linear_search([14, 7, 22, 9, 7, 31], 18) -> "Target not found"
    """
    # TODO: 1. Initialize index = 0
    # TODO: 2. Loop through val in values:
    #          - If val == target: return index immediately
    #          - Increment index by 1
    # TODO: 3. If loop finishes without returning, return "Target not found"
    pass
