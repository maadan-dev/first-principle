"""
Drill 01: Optimized Prime Checker & Prime Sum
Fellowship Challenge: Set 4 — Question 1

CONSTRAINTS:
1. Use a while loop for checking if a number is prime (no range() in primality check).
2. Stop checking at the square root (i * i <= num) without importing math.
3. Do not use sum().
4. Do not import any libraries.
"""


def is_prime(num: int) -> bool:
    """
    Determines if a number is prime using a while loop with i * i <= num optimization.
    Returns True if prime, False otherwise.
    """
    # TODO: Handle numbers less than 2 (not prime)
    # TODO: Initialize i = 2
    # TODO: while i * i <= num:
    #           check if num % i == 0 -> return False
    #           increment i
    # TODO: return True if no divisor was found
    pass


def analyze_primes(n: int) -> tuple[bool, list[int], int]:
    """
    Given N:
    1. Determines if N is prime.
    2. Finds all primes from 2 up to N.
    3. Calculates the sum of all primes up to N without using sum().

    Returns a tuple: (is_n_prime, primes_list, sum_of_primes)
    Example for N = 10: (False, [2, 3, 5, 7], 17)
    Example for N = 7:  (True, [2, 3, 5, 7], 17)
    """
    # TODO: Step 1 - Check if N itself is prime using is_prime(n)

    # TODO: Step 2 - Collect all primes from 2 up to N into a list

    # TODO: Step 3 - Calculate the sum of the primes list WITHOUT using sum()

    # TODO: Return (is_n_prime, primes_list, total_sum)
    pass


if __name__ == "__main__":
    # Test your function manually here
    print("Testing with N = 10:")
    result = analyze_primes(10)
    print(f"Result: {result}")
