"""
Step 05: The Assembly — The List Analyser
Track: 01-numbers-and-lists

FELLOWSHIP CHALLENGE: Question 1

CONSTRAINTS:
1. Do NOT use min(), max(), or sum().
2. Do NOT use sort() or sorted().
3. You may use len() to calculate the average.
4. Assume numbers contains at least one item.
"""


def analyse_list(numbers: list[int]) -> dict:
    """
    Given a list of numbers, calculates smallest, largest, total, and average
    in a single loop pass without using min(), max(), or sum().

    Example:
        numbers = [12, 5, 27, 8, 14]
        -> {
            "smallest": 5,
            "largest": 27,
            "total": 66,
            "average": 13.2
        }
    """
    # TODO: 1. Set up your tracking variables:
    #       total = 0
    #       smallest = numbers[0]
    #       largest = numbers[0]

    # TODO: 2. Loop through every number in numbers:
    #       - Add num to total
    #       - Check if num > largest -> update largest
    #       - Check if num < smallest -> update smallest

    # TODO: 3. Calculate average = total / len(numbers)

    # TODO: 4. Return the result dictionary with keys:
    #       "smallest", "largest", "total", "average"
    pass
