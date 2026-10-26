# Step 01: The Grid Visitor

## The Mental Model
A 2D list (or matrix) sounds scary, but it is just a list whose elements are other lists!
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

To look at every single number inside, you need **two loops** working together:
1. **The Outer Loop:** picks up one row at a time.
2. **The Inner Loop:** walks through every number inside that current row.

```python
for row in matrix:
    for cell in row:
        print(cell)
```

Think of it like an egg carton:
- Outer loop picks up each carton row.
- Inner loop inspects each egg in that row.

---

## Your Mission
Implement `flatten_grid(matrix: list[list[int]]) -> list[int]` in [exercise.py](file:///C:/Users/user/Documents/GitHub/first-principles/06-grids-and-nested-loops/step-01-the-grid-visitor/exercise.py).
Visit every cell using nested loops and append it to a 1D flat list.

### Constraints
- Do **not** use list comprehensions.
- Use explicit nested `for` loops.

---

## How to Test
Run the test from this directory:
```bash
python test_exercise.py
```
