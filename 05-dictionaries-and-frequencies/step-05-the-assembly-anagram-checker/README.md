# Step 05: The Assembly — Anagram Checker

## The Grand Assembly
This is another classic assessment question!

> **Challenge Prompt:**  
> Determine if two strings are anagrams of each other (they contain the exact same characters in any order, with identical counts). Ignore casing and spaces.  
> **Constraints:**  
> - Do not use `sorted()` or `.sort()`.  
> - Do not use `collections.Counter`.  
> - Build character frequency dictionaries manually and compare them.

---

## How Your Bricks Fit Together
Why is this problem easy once you know first principles?
Because an anagram simply means: **Both strings have the exact same character frequency dictionary!**

1. Clean both strings (Track 03, Step 02): keep only alphanumeric characters, convert to lowercase.
2. Build a character frequency map for string 1 (Track 05, Step 02).
3. Build a character frequency map for string 2.
4. Compare `dict1 == dict2`. Python checks if both dictionaries have the exact same keys and values!

---

## Your Mission
Implement `are_anagrams(s1: str, s2: str) -> bool` in [exercise.py](file:///C:/Users/user/Documents/GitHub/first-principles/05-dictionaries-and-frequencies/step-05-the-assembly-anagram-checker/exercise.py).

---

## How to Test
Run the test from this directory:
```bash
python test_exercise.py
```
