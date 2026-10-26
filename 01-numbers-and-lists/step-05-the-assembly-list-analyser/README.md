# Step 05: The Assembly — The List Analyser 🚀

> **FELLOWSHIP CONQUERED:**  
> This is Question 1 from the Python Foundations Challenge!

---

## The Big Picture
Look back at what you just built:
- In **Step 02**, you learned how to calculate a `total` using an accumulator.
- In **Step 03**, you learned how to find the `largest` champion.
- In **Step 04**, you learned how to find the `smallest` champion.

Now, instead of 3 separate functions, you put all three jobs **inside one single loop**!

```text
As you visit each number:
  1. Add it to total
  2. If it's bigger than largest -> update largest
  3. If it's smaller than smallest -> update smallest
```

At the end, calculate average:
```python
average = total / len(numbers)
```

And return all four values together!

---

## Your Task
Open [`exercise.py`](./exercise.py).
Implement `analyse_list(numbers: list[int]) -> dict`.

Return a dictionary with:
```python
{
    "smallest": 5,
    "largest": 27,
    "total": 66,
    "average": 13.2
}
```

**Constraints:**
- Do NOT use `min()`
- Do NOT use `max()`
- Do NOT use `sum()`
- Do NOT use `sort()` or `sorted()`
- You MAY use `len(numbers)` to calculate the average.

---

## Run the Test
```bash
python test_exercise.py
```
