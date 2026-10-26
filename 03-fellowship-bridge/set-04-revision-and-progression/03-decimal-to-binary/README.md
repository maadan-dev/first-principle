# Drill 03: Decimal to Binary (The Reducer Engine) 💻

> **Fellowship Challenge: Set 4 — Question 3**  
> *Target Time: 15–20 Minutes*

---

## 📜 The Mentor's Problem Statement
> Given a non-negative integer $N$, convert it to its binary string representation.
>
> **Examples**:
> - Input: `10` $\to$ Output: `"1010"`
> - Input: `25` $\to$ Output: `"11001"`
> - Input: `1`  $\to$ Output: `"1"`
> - Input: `0`  $\to$ Output: `"0"`
>
> **Constraints**:
> - Do NOT use `bin()`.
> - Do NOT use formatted strings like `f"{num:b}"`.
> - Use the mathematical method: repeatedly divide by 2 and track remainders (`% 2` and `// 2`).
> - Build the final binary string manually using string concatenation.
> - Do NOT import any libraries.

---

## 🗣️ Plain-English Translation
How do computers convert decimal numbers to binary by hand?

Think of binary like counting with only 0s and 1s:
1. Divide the number by 2 using integer division: `n // 2`.
2. Grab the remainder using modulo: `n % 2`. This gives either `0` or `1`.
3. Notice: The **first remainder you get is the rightmost bit**!
   So each new remainder must be glued to the **FRONT** (prepend) of your binary string!
4. Repeat this until $N$ becomes $0$.

---

## 📝 Trace Table for $N = 10$

| Iteration | `n` (before) | Remainder (`n % 2`) | Next `n` (`n // 2`) | Binary String (Prepending) |
|:---:|:---:|:---:|:---:|:---:|
| **Init** | `10` | — | — | `""` |
| **1** | `10` | `0` | `5` | `"0" + ""` $\to$ `"0"` |
| **2** | `5` | `1` | `2` | `"1" + "0"` $\to$ `"10"` |
| **3** | `2` | `0` | `1` | `"0" + "10"` $\to$ `"010"` |
| **4** | `1` | `1` | `0` | `"1" + "010"` $\to$ `"1010"` |
| **Exit** | `0` | — | — | **Stop (`n == 0`)** $\to$ Result: `"1010"` |

---

## 🪜 The 3-Rung Ladder

### Rung 1: Handle Edge Case $N = 0$
```python
if n == 0:
    return "0"
```

### Rung 2: The While Reducer Loop
```python
current = n
binary_str = ""

while current > 0:
    rem = current % 2
    binary_str = str(rem) + binary_str  # Prepend!
    current = current // 2              # Shrink!
```

---

## 🥋 Your Turn!
Open [`exercise.py`](./exercise.py) and implement `decimal_to_binary(n)`.  
Then verify with:

```bash
python test_exercise.py
```
