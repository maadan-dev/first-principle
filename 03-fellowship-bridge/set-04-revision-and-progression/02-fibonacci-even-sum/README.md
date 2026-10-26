# Drill 02: Fibonacci Sequence — Even Sum & Inverted Stream 🌀

> **Fellowship Challenge: Set 4 — Question 2**  
> *Target Time: 15–20 Minutes*

---

## 📜 The Mentor's Problem Statement
> Given an integer $N$, generate the first $N$ numbers of the Fibonacci sequence starting at $0$.  
> Calculate the sum of only the **even numbers** in that sequence.  
> Finally, produce the sequence in **reverse order**.
>
> **Constraints**:
> - Generate the sequence using a loop (no recursion).
> - Do NOT store the sequence in a list/array to reverse it. Reverse it using string-building or mathematical logic without `[::-1]` or `.reverse()`.
> - Do NOT use `sum()`.
> - Do NOT import any libraries.

---

## 🗣️ Plain-English Translation
Why did the mentor ban `[::-1]` and storing lists?
Because in Python, it's easy to just do `lst.reverse()`. The mentor wants to see if you understand **The Relay Pattern (State Swapping)** and **The Prepend Accumulator Pattern**.

### 1. The Relay (How Fibonacci Works without magic)
You only need two variables to generate Fibonacci:
- `a = 0` (current number)
- `b = 1` (next number)

In every loop step:
```python
# The handoff: current becomes next, and next becomes current + next
a, b = b, a + b
```

### 2. The Prepend Accumulator (Reversing on the Fly!)
If you add to the *end* of a string (`s = s + str(x)`), it stays in order.  
If you add to the *front* (`s = str(x) + s`), it **automatically reverses** as it generates!

```text
Iter 1: "0"
Iter 2: "1, " + "0"        -> "1, 0"
Iter 3: "1, " + "1, 0"     -> "1, 1, 0"
Iter 4: "2, " + "1, 1, 0"  -> "2, 1, 1, 0"
```
Zero lists needed. Zero `[::-1]` needed. That is First Principles thinking!

---

## 🪜 The 3-Rung Ladder

### Rung 1: Generate & Format Sequence
```python
a, b = 0, 1
sequence_parts = []
for _ in range(n):
    sequence_parts.append(str(a))
    a, b = b, a + b
# "0, 1, 1, 2, 3, 5, 8, 13"
```

### Rung 2: Accumulate Only Evens
```python
if a % 2 == 0:
    even_sum += a
```

### Rung 3: Prepend to Reverse String
```python
if reversed_str == "":
    reversed_str = str(a)
else:
    reversed_str = str(a) + ", " + reversed_str
```

---

## 🥋 Your Turn!
Open [`exercise.py`](./exercise.py) and implement `fibonacci_analysis(n)`.  
Then verify with:

```bash
python test_exercise.py
```
