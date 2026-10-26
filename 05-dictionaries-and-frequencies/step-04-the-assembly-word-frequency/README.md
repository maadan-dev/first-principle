# Step 04: The Assembly — Word Frequency Analyser

## The Grand Assembly
This is Fellowship Assessment Challenge 5!

> **Challenge Prompt:**  
> Given a paragraph of text, count how many times each word appears and store it in a dictionary. Then, find and return the single most frequent word.  
> **Constraints:**  
> - Treat uppercase and lowercase as the same.  
> - Strip basic punctuation manually without using the `re` module or `string.punctuation`.  
> - Find the most frequent word without `max()` or sorting the dictionary.  
> - Do not use `collections.Counter`.

---

## How Your Bricks Fit Together
Look at how easy this becomes when you snap together the bricks you already mastered:
1. **The Letter Filter (Track 03, Step 02):**  
   Walk through the paragraph. If a character is alphanumeric (`.isalnum()`) or a space (`char == ' '`), keep it and make it lowercase (`.lower()`).
2. **The Tally Counter (Track 05, Step 02):**  
   Split the cleaned string into words with `.split()`. Tally each word in a `counts = {}` dictionary.
3. **The Champion Pattern (Track 05, Step 03):**  
   Loop through `counts.items()` to find the word with the highest count without `max()`.

Three tiny 5-line patterns solve the entire assessment question!

---

## Your Mission
Implement `word_frequency_analyser(text: str) -> tuple[dict, str, int]` in [exercise.py](file:///C:/Users/user/Documents/GitHub/first-principles/05-dictionaries-and-frequencies/step-04-the-assembly-word-frequency/exercise.py).
Return a tuple: `(counts_dict, most_frequent_word, count)`.
If `text` contains no words, return `({}, None, 0)`.

---

## How to Test
Run the test from this directory:
```bash
python test_exercise.py
```
