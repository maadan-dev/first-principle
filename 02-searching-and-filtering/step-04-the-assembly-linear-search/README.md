# Step 04: The Assembly — Linear Search 🔎

> **FELLOWSHIP CONQUERED:**  
> This is Question 2 from the Python Foundations Challenge!

---

## The Big Picture
Look at how the LEGO bricks fit together:
- In **Step 01**, you learned how to test `item == target`.
- In **Step 02**, you learned how to count the index manually: `index = 0` and `index += 1`.
- In **Step 03**, you learned how to `return` the answer the instant you find it.

When you snap those three together:
```python
index = 0
for item in values:
    if item == target:
        return index  # Found it! Exit early!
    index += 1

return "Target not found"  # Survived the whole loop without finding it
```

---

## Your Task
Open [`exercise.py`](./exercise.py).
Implement `linear_search(values: list[int], target: int) -> int | str`.

**Examples:**
- `linear_search([14, 7, 22, 9, 7, 31], 22)` $\to$ `2`
- `linear_search([14, 7, 22, 9, 7, 31], 18)` $\to$ `"Target not found"`

**Constraints:**
- Do NOT use `.index()`.
- Stop searching once the first match is found.

---

## Run the Test
```bash
python test_exercise.py
```
