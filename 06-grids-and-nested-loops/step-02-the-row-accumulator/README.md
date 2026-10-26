# Step 02: The Row Accumulator

## The Mental Model
Before we calculate sums for an entire grid of rows, let's refresh **The Accumulator Pattern** from Track 01, Step 02.

To sum a single row:
1. Start a basket: `row_total = 0`.
2. Walk through every number in that row.
3. Add the number to the basket: `row_total += num`.
4. When the loop finishes, `row_total` holds the exact sum!

Mentors ban `sum()`, but you don't care because the accumulator loop is simple, reliable, and completely under your control.

---

## Your Mission
Implement `sum_single_row(row: list[int]) -> int` in [exercise.py](file:///C:/Users/user/Documents/GitHub/first-principles/06-grids-and-nested-loops/step-02-the-row-accumulator/exercise.py).

### Constraints
- Do **not** use `sum()`.
- Use a `for` loop and an accumulator variable.

---

## How to Test
Run the test from this directory:
```bash
python test_exercise.py
```
