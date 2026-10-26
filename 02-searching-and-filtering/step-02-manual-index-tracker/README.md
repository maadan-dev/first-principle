# Step 02: The Manual Index Tracker 📍

## The Idea
When the fellowship mentor says:
> *"Do NOT use the list's `.index()` method!"*

They want to see if you understand how to keep track of **where you are standing**.

Think of counting steps:
1. You start at step 0: `current_index = 0`
2. Every time you step to the next item:
   ```python
   current_index += 1
   ```
3. That's all an index is: a counter that increments by 1 on every iteration!

---

## Your Task
Open [`exercise.py`](./exercise.py).
Write a function `pair_with_indices(items: list[str]) -> list[tuple[int, str]]` that loops through `items` and manually tracks the index (starting at 0), returning a list of `(index, item)` tuples.

**Constraint:** Do NOT use `.index()`.

---

## Run the Test
```bash
python test_exercise.py
```
