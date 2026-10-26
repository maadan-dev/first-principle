"""
Drill 03: Decimal to Binary (The Reducer Engine)
Fellowship Challenge: Set 4 — Question 3

CONSTRAINTS:
1. Do not use bin().
2. Do not use string formatting like f"{num:b}".
3. Use the mathematical method: repeatedly divide by 2 and track remainders.
4. Build the final binary string manually using string concatenation.
5. Do not import any libraries.
"""


def decimal_to_binary(n: int) -> str:
    """
    Converts a non-negative integer N to its binary representation as a string.

    Examples:
        decimal_to_binary(10) -> "1010"
        decimal_to_binary(25) -> "11001"
        decimal_to_binary(0)  -> "0"
    """
    # TODO: Step 1 - Handle the zero edge case (if n == 0, return "0")

    # TODO: Step 2 - Initialize an empty binary string and a current variable

    # TODO: Step 3 - While current > 0:
    #       - Find the remainder of dividing by 2 (current % 2)
    #       - Prepend the remainder to your binary string (str(rem) + binary_str)
    #       - Update current using integer division (current // 2)

    # TODO: Step 4 - Return the final binary string
    pass


if __name__ == "__main__":
    for test_val in [10, 25, 1, 0]:
        print(f"{test_val} in binary -> '{decimal_to_binary(test_val)}'")
