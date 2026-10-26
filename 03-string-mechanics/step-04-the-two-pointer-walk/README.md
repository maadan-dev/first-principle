# Step 04: The Two-Pointer Walk 🚶‍♂️...🚶‍♀️

## The Idea
What is a **Two-Pointer** approach?
Don't let the fancy name scare you!

Imagine two people walking toward each other on a bridge:
- **Person 1 (Left pointer)** starts at the very beginning: `left = 0`
- **Person 2 (Right pointer)** starts at the very end: `right = len(text) - 1`

At each step:
1. They compare the letters: `if text[left] != text[right]:`  
   If they don't match, it can't be a palindrome!
2. Then they step toward each other:
   - `left += 1` (steps forward)
   - `right -= 1` (steps backward)
3. They stop when they meet in the middle (`left >= right`).

Notice: **Zero memory wasted.** You never had to create a new reversed string!

---

## Your Task
Open [`exercise.py`](./exercise.py).
Write a function `is_simple_palindrome(word: str) -> bool` that checks if a single lowercase word (no spaces or punctuation) is a palindrome using two pointers.

**Examples:**
- `is_simple_palindrome("racecar")` $\to$ `True`
- `is_simple_palindrome("hello")` $\to$ `False`

**Constraint:**
- Must use `while left < right:` (no reversed strings).

---

## Run the Test
```bash
python test_exercise.py
```
