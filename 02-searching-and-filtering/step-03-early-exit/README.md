# Step 03: The Early Exit 🚪

## The Idea
When you lose your car keys and you find them on the kitchen table, do you keep searching the bedroom, the living room, and the attic?  
**Of course not! You stop searching immediately.**

In coding, that is called an **Early Exit**.
When you are inside a function searching through a list:
```python
if item == target:
    return current_index  # Leaves the function immediately!
```

`return` immediately stops the loop and hands back the answer. It doesn't waste time checking the rest of the list!

---

## Your Task
Open [`exercise.py`](./exercise.py).
Write a function `find_first_negative(numbers: list[int]) -> int | None`:
- Walk through `numbers`.
- The moment you find a number less than 0 (`num < 0`), **return it immediately**.
- If the loop finishes and no negative was ever found, return `None`.

---

## Run the Test
```bash
python test_exercise.py
```
