"""
Master Solution for Drill 03: Decimal to Binary.
Fellowship Challenge: Set 4 — Question 3
"""


def decimal_to_binary(n: int) -> str:
    """
    Converts a non-negative integer N to its binary representation.

    The Reducer Pattern:
    1. Base case: 0 is "0".
    2. While n > 0:
       - Remainder (n % 2) gives the current bit.
       - Prepending (bit + binary_str) ensures least-significant bits are at the right.
       - Integer division (n // 2) shrinks n towards 0.
    """
    if n == 0:
        return "0"

    binary_str = ""
    current = n

    while current > 0:
        remainder = current % 2
        binary_str = str(remainder) + binary_str
        current = current // 2

    return binary_str


if __name__ == "__main__":
    for num in [10, 25, 1, 0, 42]:
        print(f"{num:>3} in decimal = {decimal_to_binary(num):>8} in binary")
