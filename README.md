# First Principles 🧠⚡

> **"If you can't trace the state with a pen and paper, you don't control the code—the code controls you."**

Welcome to **First Principles**. This repository was built for developers who want to move past passive tutorial completion and master the true mechanics of programming.

---

## 💡 The Core Problem: The "Dictation" Trap

Most beginner courses (like interactive step-by-step tracks) teach syntax by dictation:
> *"Declare variable `x = []` on line 2."*  
> *"Now write a `for` loop over `items`."*  
> *"Now append to `x`."*

You get a green checkmark, but when you are dropped in front of a blank file with strict constraints (*"No `range()`, no `sum()`, no `[::-1]`, while-loop only"*), your brain freezes.

That freeze is **not a lack of intelligence**. It is a **gap in mental models**. You were taught *what* functions exist in Python, but not *how to think in state changes and algorithms*.

**First Principles** bridges that gap.

---

## 🏛️ The 5 Universal Loop Archetypes

Every loop problem you will ever see in your career—from a simple test to a LeetCode Hard—is built from just **5 universal patterns**:

| # | Archetype | The Mental Picture | Fellowship / Interview Example |
| :--- | :--- | :--- | :--- |
| **1** | **The Accumulator** *(The Snowball)* | Start with empty state (`0`, `""`, `[]`), visit items, add/modify, return result. | Summing numbers without `sum()`, reversing strings without `[::-1]`. |
| **2** | **The Guardian / Filter** *(The Bouncer)* | Inspect each item. Let matching items pass, or exit early with `break`. | Prime testing (stop at $\sqrt{N}$), finding target elements. |
| **3** | **The Reducer** *(The Shredder)* | Start with a number or string. Repeatedly divide, chop, or shrink it until zero. | Decimal to Binary conversion, number-to-digits. |
| **4** | **The State Machine** *(The Relay)* | Remember what happened on the *previous* step to decide what to do on the *current* step. | Fibonacci numbers, Roman numerals look-ahead, capitalize after space. |
| **5** | **The Frequency Bucket** *(The Sorter)* | Tally occurrences of items manually without libraries. | Anagram checks, character counts. |

When you see a problem, you don't panic. You ask: **"Which of the 5 archetypes is this?"**

---

## 🪜 The 3-Tier Training Ladder

Every topic is broken down into three stages so you never hit a wall:

```
┌──────────────────────────────────────────────────────────────────┐
│  Tier 3: The Challenge (The Boss Fight)                          │
│          Assemble Tier 1 & Tier 2 into the full multi-part task. │
├──────────────────────────────────────────────────────────────────┤
│  Tier 2: The Constraint Squeeze (Muscle Memory)                  │
│          Enforce strict rules (no range, no sum, no [::-1]).     │
├──────────────────────────────────────────────────────────────────┤
│  Tier 1: Read & Trace (The Atomic Mechanism)                     │
│          Fill in a trace table. Step through lines 1-by-1.       │
└──────────────────────────────────────────────────────────────────┘
```

---

## 🗺️ Curriculum Roadmap

### `01-mental-models/`
- **`the-5-loop-archetypes.md`**: Deep dive with code templates for every pattern.
- **`how-to-trace-code.md`**: How to use a paper trace table to visualize execution before writing a single line.

### `02-foundations-drills/`
Targeted muscle-memory exercises directly reinforcing loops and sequences:
- **`01-accumulators`**: Manual sums, products, and custom string joiners.
- **`02-reducers`**: `while` loops, number reduction, remainder tracking.
- **`03-bouncers-and-primes`**: Divisor checking, flag variables, early exits.
- **`04-two-pointers-and-swaps`**: In-place reversals, palindrome checks without slicing.
- **`05-frequency-maps`**: Building manual tally dictionaries.

### `03-fellowship-bridge/`
Step-by-step deconstruction of the Fellowship Monday Challenges:
- **`set-04-revision-and-progression`**:
  - `01-optimized-primes`: Primes up to $N$ with $\sqrt{N}$ while-loop optimization.
  - `02-fibonacci-even-sum`: Fibonacci sequence, even sum, reverse printing without lists or `[::-1]`.
  - `03-decimal-to-binary`: Pure remainder division and manual string assembly.
  - `04-matrix-multiplication`: 3-tier nested loop matrix algebra.
  - `05-ascii-capitalize`: First-letter word capitalization with `ord()` and `chr()` arithmetic.
  - `06-anagram-checker`: Character frequency hashing without `set` or `sort`.
  - `07-roman-to-integer`: Look-ahead dictionary parsing.
  - `08-matrix-rotation`: In-place 90° clockwise matrix rotation (Transpose + Row Reversal).

---

## ⚡ Golden Rules of First Principles
1. **Trace First**: If you are stuck, write a 3-row trace table with a pen. Don't guess in the code editor.
2. **One Variable at a Time**: Never write a nested loop until the outer loop is printing exactly what you expect.
3. **No Magic Allowed**: If a challenge bans a built-in function (`range`, `sum`, `[::-1]`), celebrate it! That constraint is the gym weights that build real engineering muscle.
