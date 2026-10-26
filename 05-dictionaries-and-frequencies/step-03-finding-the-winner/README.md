# Step 03: Finding the Winner

## The Mental Model
In Track 01, Step 03, you learned **The Champion Pattern** to find the largest number in a list without using `max()`.

Guess what? Finding the most frequent word in a dictionary uses the exact same pattern!
- You hold a trophy for `highest_count = -1` and `champion_key = None`.
- You walk through every pair in the dictionary.
- If a candidate's count beats `highest_count`, they become the new champion!

```python
for key, count in counts.items():
    if count > highest_count:
        highest_count = count
        champion_key = key
```

Mentors often ban `max(counts, key=counts.get)` or `sorted()`. With the Champion Pattern, you never need them!

---

## Your Mission
Implement `find_most_frequent(counts: dict) -> tuple[str, int]` in [exercise.py](file:///C:/Users/user/Documents/GitHub/first-principles/05-dictionaries-and-frequencies/step-03-finding-the-winner/exercise.py).
Return `(champion_key, highest_count)`. If `counts` is empty, return `(None, 0)`.

### Constraints
- Do **not** use `max()`.
- Do **not** use `sorted()` or `.sort()`.
- Use the Champion Pattern with a loop.

---

## How to Test
Run the test from this directory:
```bash
python test_exercise.py
```
