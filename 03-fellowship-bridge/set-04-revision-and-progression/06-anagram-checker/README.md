# Drill 06: The Anagram Frequency Bucket 🔡📊

> **Fellowship Challenge: Set 4 — Question 6**  
> *Target Time: 15–20 Minutes*

---

## 📜 The Mentor's Problem Statement
> Given two strings, determine if they are **anagrams** of each other. An anagram is a word formed by rearranging the letters of another word, using all original letters exactly once.
>
> **Examples**:
> - `"listen"`, `"silent"` $\to$ `True`
> - `"hello"`, `"world"` $\to$ `False`
> - `"Dormitory"`, `"dirtyroom"` $\to$ `True` (Case-insensitive)
>
> **Constraints**:
> - Treat uppercase and lowercase as the same (case-insensitive).
> - Do NOT use `sort()`, `sorted()`, or `set()`.
> - Build a character-frequency dictionary manually for both strings and compare them.
> - Do NOT import any libraries (no `collections.Counter`).

---

## 🗣️ Plain-English Translation
Why did the mentor ban `sorted()`?  
Because `sorted("listen") == sorted("silent")` is a 1-line standard library trick.

In real systems, sorting takes $O(N \log N)$ time, whereas a **Frequency Bucket (Hash Map)** takes only $O(N)$ linear time! The mentor is forcing you to use the more efficient computer science data structure.

### The Frequency Bucket Blueprint
For each word, tally how many times each letter appears:
```python
counts = {}
for char in word:
    char = char.lower()
    if char in counts:
        counts[char] += 1
    else:
        counts[char] = 1
```

If both words produce identical frequency buckets, they **must be anagrams**!

---

## 🪜 The 3-Rung Ladder

### Rung 1: Build the Frequency Map Helper
```python
def build_frequency_map(text: str) -> dict[str, int]:
    freq = {}
    for char in text:
        # Ignore spaces and convert to lowercase
        if char == " ":
            continue
        char = char.lower()
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq
```

### Rung 2: Compare Lengths as an Early Bouncer
```python
# If cleaned lengths don't match, they can never be anagrams!
if len(word1) != len(word2):
    return False
```

### Rung 3: Compare the Frequency Maps
```python
return build_frequency_map(word1) == build_frequency_map(word2)
```

---

## 🥋 Your Turn!
Open [`exercise.py`](./exercise.py) and implement `is_anagram(word1, word2)`.  
Then verify with:

```bash
python test_exercise.py
```
