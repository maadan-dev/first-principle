# Step 01: The Key Lookup

## The Mental Model
A dictionary is like a real address book. If you look up someone's name, you get their phone number.
In Python:
```python
phonebook = {"Alice": "123", "Bob": "456"}
```
If you ask for `"Alice"`, you get `"123"`.
**Danger:** If you ask for `"Charlie"` using `phonebook["Charlie"]`, Python crashes with a `KeyError`!

To avoid crashing, we check if the key exists first:
```python
if key in my_dict:
    # safe to access my_dict[key]
else:
    # key is missing, handle fallback
```

---

## Your Mission
Implement `safe_lookup(d: dict, key: str, default: int) -> int` in [exercise.py](file:///C:/Users/user/Documents/GitHub/first-principles/05-dictionaries-and-frequencies/step-01-the-key-lookup/exercise.py).
If `key` is in `d`, return its value. Otherwise, return `default`.

### Constraints
- Do **not** use `d.get()`.
- Use an `if key in d:` conditional statement.

---

## How to Test
Run the test from this directory:
```bash
python test_exercise.py
```
