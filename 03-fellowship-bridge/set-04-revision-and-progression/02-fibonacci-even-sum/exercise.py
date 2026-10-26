"""
Drill 02: Fibonacci Sequence — Even Sum & Inverted Stream
Fellowship Challenge: Set 4 — Question 2

CONSTRAINTS:
1. Generate the sequence using a loop (no recursion).
2. Do not store the sequence in an array/list to reverse it.
   Build the reversed sequence using string manipulation without [::-1] or .reverse().
3. Do not use sum().
4. Do not import any libraries.
"""


def fibonacci_analysis(n: int) -> tuple[str, int, str]:
    """
    Given N:
    1. Generates the first N Fibonacci numbers starting from 0: "0, 1, 1, 2, 3, ..."
    2. Computes the sum of only the even Fibonacci numbers in the sequence (without sum()).
    3. Builds the reversed representation as a string WITHOUT [::-1], .reverse(), or reversing a list.

    Returns a tuple: (forward_sequence_str, even_sum, reversed_sequence_str)
    Example for N = 8:
        ("0, 1, 1, 2, 3, 5, 8, 13", 10, "13, 8, 5, 3, 2, 1, 1, 0")
    """
    if n <= 0:
        return ("", 0, "")

    # TODO: Initialize variables:
    # a = 0, b = 1
    # forward_str = ""
    # reversed_str = ""
    # even_sum = 0

    # TODO: Loop N times:
    # 1. Update even_sum if 'a' is even (a % 2 == 0)
    # 2. Append 'a' to forward_str
    # 3. Prepend 'a' to reversed_str (adds to front, reversing it on the fly!)
    # 4. Advance state: a, b = b, a + b

    # TODO: Return (forward_str, even_sum, reversed_str)
    pass


if __name__ == "__main__":
    print("Testing with N = 8:")
    print(fibonacci_analysis(8))
