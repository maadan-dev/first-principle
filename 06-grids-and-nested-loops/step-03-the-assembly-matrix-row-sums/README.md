# Step 03: The Assembly — Matrix Row Sums

## The Grand Assembly
This is a core assessment challenge from the fellowship!

> **Challenge Prompt:**  
> Given a matrix (a 2D list of integers), calculate the sum of each row and return a list of all row sums.  
> Additionally, identify the index of the row with the largest sum and its total.  
> **Constraints:**  
> - Do not use `sum()`.  
> - Do not use `max()`.  
> - Do not use list comprehensions.  
> - Use nested loops and manual accumulators.

---

## How Your Bricks Fit Together
Look at how the pieces connect:
1. **The Grid Visitor (Track 06, Step 01):**  
   Outer loop goes row by row (`for row_index, row in enumerate(matrix):`).
2. **The Row Accumulator (Track 06, Step 02):**  
   Before looking at each row's numbers, reset `row_total = 0`.  
   Inner loop adds each number to `row_total`.  
   Append `row_total` to `row_sums`.
3. **The Champion Pattern (Track 01, Step 03):**  
   Compare `row_total` against `max_sum`. If it wins, update `max_sum` and `best_row_index`!

---

## Your Mission
Implement `matrix_row_summary(matrix: list[list[int]]) -> tuple[list[int], int, int]` in [exercise.py](file:///C:/Users/user/Documents/GitHub/first-principles/06-grids-and-nested-loops/step-03-the-assembly-matrix-row-sums/exercise.py).
Return `(row_sums, best_row_index, max_row_sum)`.
If `matrix` is empty, return `([], None, None)`.

---

## How to Test
Run the test from this directory:
```bash
python test_exercise.py
```
