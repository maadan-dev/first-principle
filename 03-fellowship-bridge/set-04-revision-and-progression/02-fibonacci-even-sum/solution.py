"""
Master Solution for Drill 02: Fibonacci Sequence — Even Sum & Inverted Stream.
Fellowship Challenge: Set 4 — Question 2
"""


def fibonacci_analysis(n: int) -> tuple[str, int, str]:
    """
    1. Generates the first N Fibonacci numbers starting from 0.
    2. Computes the sum of only the even Fibonacci numbers in the sequence (without sum()).
    3. Builds the reversed representation as a string WITHOUT [::-1], .reverse(), or lists.
    """
    if n <= 0:
        return ("", 0, "")

    a = 0
    b = 1

    forward_parts = []
    reversed_str = ""
    even_sum = 0

    for _ in range(n):
        # Accumulate even values
        if a % 2 == 0:
            even_sum += a

        # Track forward string
        forward_parts.append(str(a))

        # Build reversed string on-the-fly by PREPENDING
        if reversed_str == "":
            reversed_str = str(a)
        else:
            reversed_str = str(a) + ", " + reversed_str

        # State machine swap (The Relay Pattern)
        a, b = b, a + b

    forward_str = ", ".join(forward_parts)
    return (forward_str, even_sum, reversed_str)


if __name__ == "__main__":
    for test_n in [8, 4, 1]:
        f_seq, e_sum, r_seq = fibonacci_analysis(test_n)
        print(f"N = {test_n}:")
        print(f"  Sequence: {f_seq}")
        print(f"  Even Sum: {e_sum}")
        print(f"  Reversed: {r_seq}\n")
