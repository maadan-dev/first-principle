# Drill 01: Optimized Prime Checker & Prime Sum 🛡️

> **Fellowship Challenge: Set 4 — Question 1**  
> *Target Time: 12–15 Minutes*

---

## 📜 The Mentor's Problem Statement
> Given an integer $N$, determine if it is a prime number. Then, find the sum of all prime numbers from $2$ up to $N$.
>
> **Constraints**:
> - You may NOT use `range()` to iterate from $2$ to $N$ for the primality check. You MUST use a `while` loop.
> - Stop checking divisors at the square root (use `i * i <= num` without importing `math`).
> - Do NOT use `sum()`.
> - Do NOT import any libraries.
> - Do NOT hardcode the answer.

---

## 🗣️ Plain-English Translation
What is the mentor *actually* asking you to do?

1. **What is a prime number?** A number greater than 1 that cannot be divided evenly by any number other than 1 and itself.
2. **Why `i * i <= num`?** If a number has a factor, at least one factor must be smaller than or equal to its square root. For example, for 36, factors are pairs: $(2, 18), (3, 12), (4, 9), (6, 6)$. After 6, the pairs just repeat in reverse! If no number up to $\sqrt{N}$ divides it, nothing will.
3. **The whole task is just 2 LEGO blocks**:
   - **Block A**: A helper logic to answer: *"Is this specific number prime?"* (The Guardian Pattern).
   - **Block B**: A loop from $2$ to $N$ that keeps a running total of the primes it finds (The Accumulator Pattern).

---

## 🪜 The 3-Rung Ladder

### Rung 1: The Prime Guardian (`is_prime`)
```python
def is_prime(num: int) -> bool:
    if num < 2:
        return False
    
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False  # Bouncer caught a divisor! Stop immediately.
        i += 1
    return True  # Survived all checks! It is prime.
```

### Rung 2: Finding All Primes from 2 to $N$
```python
primes = []
for num in range(2, n + 1):
    if is_prime(num):
        primes.append(num)
```

### Rung 3: The Manual Sum Accumulator (No `sum()`)
```python
total_sum = 0
for p in primes:
    total_sum += p
```

---

## 🥋 Your Turn!
Open [`exercise.py`](./exercise.py) and implement `analyze_primes(n)`.  
Then verify your solution by running:

```bash
python test_exercise.py
```
