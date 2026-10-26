# How to Trace Code with Pen and Paper 📝

> **"If you can trace the code line by line, bugs cannot hide from you."**

Beginners often get stuck in a painful cycle called **"shotgun debugging"**:
1. Stare at code.
2. Guess what might be wrong.
3. Change a random `+ 1` to `- 1` or `<` to `<=`.
4. Run it. Still broken.
5. Feel frustrated and lost.

Professional engineers don't guess. They **trace**. Tracing means acting like a mechanical computer: taking a pen, drawing a table, and tracking the exact value of every variable at every single tick of the clock.

---

## 🏗️ Anatomy of a Trace Table

A trace table has one column for each variable, plus one column for any condition being evaluated.

Let's trace this code:
```python
total = 0
i = 1

while i <= 4:
    total += i
    i += 1
```

### The Trace Table:
| Step / Line | `i` | Condition: `i <= 4`? | `total` | Notes |
|:---:|:---:|:---:|:---:|:---|
| **Before Loop** | `1` | — | `0` | Initialized state |
| **Iter 1: Check** | `1` | **True** ($1 \le 4$) | `0` | Enter loop |
| **Iter 1: Body** | `1` $\to$ `2` | — | $0 + 1 = 1$ | `total += 1`, then `i += 1` |
| **Iter 2: Check** | `2` | **True** ($2 \le 4$) | `1` | Continue |
| **Iter 2: Body** | `2` $\to$ `3` | — | $1 + 2 = 3$ | `total += 2`, then `i += 1` |
| **Iter 3: Check** | `3` | **True** ($3 \le 4$) | `3` | Continue |
| **Iter 3: Body** | `3` $\to$ `4` | — | $3 + 3 = 6$ | `total += 3`, then `i += 1` |
| **Iter 4: Check** | `4` | **True** ($4 \le 4$) | `6` | Continue |
| **Iter 4: Body** | `4` $\to$ `5` | — | $6 + 4 = 10$ | `total += 4`, then `i += 1` |
| **Iter 5: Check** | `5` | **False** ($5 \le 4$) | `10` | **Loop terminates!** |

**Final Value of `total`:** `10`.  
**Final Value of `i`:** `5`.

---

## 🔍 Tracing an Optimized Prime Check (`i * i <= N`)

Let's trace why `i * i <= n` stops at the square root.  
Suppose $N = 37$. We want to test if $37$ is prime.

```python
num = 37
is_prime = True
i = 2

while i * i <= num:
    if num % i == 0:
        is_prime = False
        break
    i += 1
```

### The Trace:
| `i` | `i * i` | `i * i <= 37`? | `num % i` ($37 \% i$) | Did it divide evenly? | Action |
|:---:|:---:|:---:|:---:|:---:|:---|
| `2` | $4$ | **True** ($4 \le 37$) | $37 \% 2 = 1$ | No | `i += 1` $\to$ `i = 3` |
| `3` | $9$ | **True** ($9 \le 37$) | $37 \% 3 = 1$ | No | `i += 1` $\to$ `i = 4` |
| `4` | $16$ | **True** ($16 \le 37$) | $37 \% 4 = 1$ | No | `i += 1` $\to$ `i = 5` |
| `5` | $25$ | **True** ($25 \le 37$) | $37 \% 5 = 2$ | No | `i += 1` $\to$ `i = 6` |
| `6` | $36$ | **True** ($36 \le 37$) | $37 \% 6 = 1$ | No | `i += 1` $\to$ `i = 7` |
| `7` | $49$ | **False** ($49 \le 37$) | — | — | **STOP! Loop ends.** |

### Look at what happened:
We tested numbers from $2$ to $6$ (only 5 checks!).  
We **did not** need to check $7, 8, 9, \dots, 36$ (saving 30 unnecessary checks).  
Because `is_prime` stayed `True`, we know $37$ is prime with 100% mathematical certainty!

---

## 🚨 The 3 Golden Questions for Any While Loop
Whenever you write a `while` loop, answer these 3 questions on paper:
1. **What is my start condition?** (e.g. `i = 2`)
2. **What is my exit condition?** (e.g. `i * i > num` or `n == 0`)
3. **Does the loop body make STRICT PROGRESS toward the exit condition?**  
   *(If you forgot `i += 1` or `n //= 2`, your loop runs forever!)*
