# Step 05: The Assembly — The Sentence Palindrome 🚀

> **FELLOWSHIP CONQUERED:**  
> This is the exact Palindrome Challenge from the Fellowship Revision Assessments!

---

## The Big Picture
Now let's snap the bricks together:
- In **Step 02**, you learned how to test if a character is a letter (`char.isalnum()`).
- In **Step 04**, you learned how `left` and `right` pointers walk towards each other.

Now, what if the sentence has spaces, commas, or question marks?
Like: `"Was it a car or a cat I saw?"`

Here is the simple logic inside your `while left < right:` loop:
1. **If `text[left]` is not a letter:**  
   Just skip it! Move `left += 1` and `continue`.
2. **If `text[right]` is not a letter:**  
   Just skip it! Move `right -= 1` and `continue`.
3. **If both are letters:**  
   Compare them in lowercase:  
   `if text[left].lower() != text[right].lower(): return False`  
   Then advance both: `left += 1` and `right -= 1`.

That's it! You didn't create any reversed strings, you didn't strip the sentence with regex, and you handled everything in a single, elegant pass!

---

## Your Task
Open [`exercise.py`](./exercise.py).
Implement `is_palindrome_sentence(sentence: str) -> bool`.

**Examples:**
- `is_palindrome_sentence("Was it a car or a cat I saw?")` $\to$ `True`
- `is_palindrome_sentence("No 'x' in Nixon")` $\to$ `True`
- `is_palindrome_sentence("Hello, World!")` $\to$ `False`

**Constraints:**
- Must use two pointers (`left` and `right`).
- Do NOT create reversed strings or use `[::-1]`.
- Skip spaces and punctuation on the fly.

---

## Run the Test
```bash
python test_exercise.py
```
