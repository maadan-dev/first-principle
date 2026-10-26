# Step 02: The Letter Filter 🛡️

## The Idea
In fellowship questions like **Palindrome** or **Word Frequency**, the mentor says:
> *"Ignore spaces and punctuation (like commas, question marks, and exclamation points)!"*

How do you check if a character is a normal letter?
In Python, strings have a built-in method `.isalnum()` (or you can check `'a' <= ch.lower() <= 'z'`):

```python
ch = "!"
ch.isalnum()  # False

ch = "a"
ch.isalnum()  # True
```

---

## Your Task
Open [`exercise.py`](./exercise.py).
Write a function `clean_letters_only(text: str) -> str` that loops through `text` and returns a string with **only the letters and numbers**, all converted to lowercase.

**Example:**
- `"Hello, World!"` $\to$ `"helloworld"`

---

## Run the Test
```bash
python test_exercise.py
```
