# Step 03: Prepend Reversal 🔄

## The Idea
When the fellowship mentor says:
> *"Do NOT use `[::-1]` or `.reverse()` to reverse a string!"*

Watch what happens when you glue characters in reverse order:

Normally, when you append:
```python
res = ""
res = res + "c"   # "c"
res = res + "a"   # "ca"
res = res + "t"   # "cat"  (normal order)
```

**Now, flip the addition!** Put the new character in FRONT:
```python
res = ""
res = "c" + res   # "c"
res = "a" + res   # "ac"
res = "t" + res   # "tac"  (REVERSED!)
```

By simply putting `char` *before* `res`, the string reverses itself automatically!

---

## Your Task
Open [`exercise.py`](./exercise.py).
Write a function `reverse_string_manual(text: str) -> str` that reverses a string using the prepend technique.

**Constraint:**
- Do NOT use `[::-1]`
- Do NOT use `.reverse()`
- Do NOT use `reversed()`

---

## Run the Test
```bash
python test_exercise.py
```
