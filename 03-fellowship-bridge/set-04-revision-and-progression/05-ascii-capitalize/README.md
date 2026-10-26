# Drill 05: ASCII Word Capitalizer & Space Stripper 🔡🔠

> **Fellowship Challenge: Set 4 — Question 5**  
> *Target Time: 15–20 Minutes*

---

## 📜 The Mentor's Problem Statement
> Given a sentence string, capitalize the first letter of every word. Then, create a second version with all spaces removed.
>
> **Examples**:
> - Input: `"hello world from python"`
> - Capitalized: `"Hello World From Python"`
> - No Spaces: `"HelloWorldFromPython"`
>
> **Constraints**:
> - Do NOT use `.replace()` to remove spaces.
> - Do NOT use `.title()` or `.capitalize()`.
> - Use loops and conditionals.
> - Use **ASCII arithmetic** to capitalize (check if char is between `'a'` and `'z'`, and convert it by subtracting 32 using `ord()` and `chr()`).
> - Do NOT import any libraries.

---

## 🗣️ Plain-English Translation
Mentors love this question because it tests whether you know that **characters are secretly numbers in computer memory**.

### 1. The ASCII Secret (`ord` and `chr`)
In computer memory, every character has a number (ASCII code):
* `'a'` is $97$, `'A'` is $65$.
* `'b'` is $98$, `'B'` is $66$.
* The difference between lowercase and uppercase is **always exactly 32**!

```python
# To check if lowercase:
if 'a' <= char <= 'z':
    # Subtract 32 to get uppercase:
    uppercase_char = chr(ord(char) - 32)
```

### 2. The "Start of Word" Flag (The State Machine)
How do you know when you are at the beginning of a word?
* Before the sentence starts, you are at the start of a word $\to$ `capitalize_next = True`.
* When you see a space `' '`, the very next letter must be capitalized $\to$ `capitalize_next = True`.
* When you capitalize a letter, reset the flag $\to$ `capitalize_next = False`.

### 3. Removing Spaces Without `.replace()`
This is simply **The Accumulator / Filter Pattern**:
```python
no_spaces = ""
for char in capitalized_text:
    if char != " ":
        no_spaces += char
```

---

## 🪜 The 3-Rung Ladder

### Rung 1: The ASCII Upper Function
```python
def to_upper_ascii(char: str) -> str:
    if 'a' <= char <= 'z':
        return chr(ord(char) - 32)
    return char
```

### Rung 2: Capitalize Words with the Flag Machine
```python
capitalized = ""
capitalize_next = True

for char in sentence:
    if char == " ":
        capitalized += " "
        capitalize_next = True
    elif capitalize_next:
        capitalized += to_upper_ascii(char)
        capitalize_next = False
    else:
        capitalized += char
```

### Rung 3: Strip Spaces
```python
no_spaces = ""
for char in capitalized:
    if char != " ":
        no_spaces += char
```

---

## 🥋 Your Turn!
Open [`exercise.py`](./exercise.py) and implement `format_sentence(sentence)`.  
Then verify with:

```bash
python test_exercise.py
```
