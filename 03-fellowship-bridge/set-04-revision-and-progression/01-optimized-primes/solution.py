"""
Master Solution for Drill 01: Optimized Prime Checker & Prime Sum.
Fellowship Challenge: Set 4 — Question 1
"""


def is_prime(num: int) -> bool:
    """
    Determines if a number is prime using a while loop with i * i <= num optimization.
    
    Why this works:
    - 0 and 1 are not prime by definition.
    - 2 is the smallest and only even prime.
    - Factors appear in pairs: (d, num / d). If num has a divisor larger than sqrt(num),
      its corresponding partner must be smaller than sqrt(num).
    - Thus, checking up to i * i <= num checks all potential factors!
    """
    if num < 2:
        return False

    i = 2
    while i * i <= num:
        if num % i == 0:
            # Found a divisor -> definitely not prime
            return False
        i += 1

    return True


def analyze_primes(n: int) -> tuple[bool, list[int], int]:
    """
    1. Checks if N is prime.
    2. Collects all primes up to N.
    3. Sums all primes up to N manually (no sum()).
    """
    # Step 1: Check N itself
    is_n_prime = is_prime(n)

    # Step 2: Collect primes up to N
    primes_list = []
    current = 2
    while current <= n:
        if is_prime(current):
            primes_list.append(current)
        current += 1

    # Step 3: Accumulator pattern (no sum())
    total_sum = 0
    for p in primes_list:
        total_sum += p

    return (is_n_prime, primes_list, total_sum)


if __name__ == "__main__":
    for test_n in [10, 7, 2]:
        is_p, plist, psum = analyze_primes(test_n)
        status = "prime" if is_p else "not prime"
        print(f"N = {test_n} -> {test_n} is {status}.")
        print(f"  Primes up to {test_n}: {plist}")
        print(f"  Sum of primes: {psum}\n")
