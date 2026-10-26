# Fellowship Bridge: Set 4 (Revision & Progression) 🌉

> **"From Panic to Clarity: The Complete First Principles Deconstruction of Monday Assessment Set 4."**

This directory takes every question from the Fellowship's **Set 4 Challenge** and transforms it from an intimidating wall of text into clear, progressive engineering steps.

---

## 🗺️ The Drill Roadmap

| Drill | Title | The Underlying First Principles Pattern | Why The Mentor Tests It |
|:---:|:---|:---|:---|
| **[01](./01-optimized-primes/)** | **Optimized Primes** | **The Guardian / Filter** | While-loop control & $\sqrt{N}$ optimization without `range()`. |
| **[02](./02-fibonacci-even-sum/)** | **Fibonacci Even Sum** | **The State Relay & Prepend Accumulator** | State swapping & on-the-fly string reversing without `[::-1]` or lists. |
| **[03](./03-decimal-to-binary/)** | **Decimal to Binary** | **The Reducer Engine** | Repeated division (`// 2`) & remainder prepending (`% 2`) without `bin()`. |
| **[04](./04-matrix-multiplication/)** | **Matrix Multiplication** | **3-Tier Nested Accumulators** | Managing dimensions and matrix coordinates across 3 nested loops. |
| **[05](./05-ascii-capitalize/)** | **ASCII Capitalizer** | **The State Machine & ASCII Math** | Manipulating byte codes (`ord`/`chr` $-32$) and word boundaries without `.replace()`. |
| **[06](./06-anagram-checker/)** | **Anagram Checker** | **The Frequency Bucket** | $O(N)$ hash mapping without `sort()` or `set()`. |
| **[07](./07-roman-to-integer/)** | **Roman to Integer** | **Look-Ahead While Loop** | Controlled variable pointer advancement (`i += 2`) on subtraction pairs. |
| **[08](./08-matrix-rotation/)** | **90° Matrix Rotation** | **In-Place Transposition + Two Pointers** | The 2-step geometric decomposition: Transpose then reverse rows. |

---

## ⚡ Zero Dependencies
Every test and drill runs on **100% pure standard library Python**:
- No `pip install` required.
- No third-party packages.
- Just clone/download and run!

```bash
# Run a specific drill:
python 01-optimized-primes/test_exercise.py

# Or run the entire suite:
python run_all_tests.py
```
