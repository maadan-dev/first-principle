# Step 02: The Tally Counter

## The Mental Model
Imagine you are at an election polling booth. You have a blank notepad.
Each time a voter calls out a candidate's name:
- If that candidate is already on your notepad, you add 1 tally mark: `counts[candidate] += 1`
- If you have never heard of that candidate before, you write their name down with 1 mark: `counts[candidate] = 1`

This pattern is called the **Manual Frequency Map**.

```python
counts = {}
for item in items:
    if item in counts:
        counts[item] += 1
    else:
        counts[item] = 1
```

Every time fellowship mentors ask you to "count words", "count characters", or "find duplicates", this exact 6-line pattern is your weapon.

---

## Your Mission
Implement `count_frequencies(items: list) -> dict` in [exercise.py](file:///C:/Users/user/Documents/GitHub/first-principles/05-dictionaries-and-frequencies/step-02-the-tally-counter/exercise.py).

### Constraints
- Do **not** use `collections.Counter`.
- Use a `for` loop and an `if item in counts:` conditional check.

---

## How to Test
Run the test from this directory:
```bash
python test_exercise.py
```
