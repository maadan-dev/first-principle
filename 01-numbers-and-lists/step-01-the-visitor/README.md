# Step 01: The Visitor 🚶

## The Idea
Before you can do anything with a list (add it, find the biggest number, or search it), you have to learn how to **visit** every single number one by one.

In Python, a `for` loop is like a conveyor belt. It picks up each item in order:

```python
for item in my_list:
    # do something with item
```

---

## Your Task
Open [`exercise.py`](./exercise.py).
Write a function `visit_all(numbers: list[int]) -> list[int]` that visits each number in `numbers` and appends it to a new list called `visited`, then returns `visited`.

---

## Run the Test
```bash
python test_exercise.py
```
