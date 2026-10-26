# Step 02: The Accumulator 🪙

## The Idea
When the fellowship mentor says:
> *"Do NOT use `sum()`"*

Don't panic! All `sum()` does is carry a little bucket.

1. You start with an empty bucket: `total = 0`.
2. As you visit each number on the conveyor belt, you toss it into the bucket:
   ```python
   total = total + num  # or total += num
   ```
3. When the loop finishes, whatever is inside `total` is your answer!

---

## Your Task
Open [`exercise.py`](./exercise.py).
Write a function `calculate_total(numbers: list[int]) -> int` that loops through `numbers` and calculates the total sum without using `sum()`.

---

## Run the Test
```bash
python test_exercise.py
```
