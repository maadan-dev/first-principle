# Drill 07: Roman to Integer (Look-Ahead While Loop) 🏛️

> **Fellowship Challenge: Set 4 — Question 7**  
> *Target Time: 20–25 Minutes*

---

## 📜 The Mentor's Problem Statement
> Given a Roman numeral string, convert it to an integer.  
> 
> **Symbol Values**:
> - `I`: $1$, `V`: $5$, `X`: $10$, `L`: $50$, `C`: $100$, `D`: $500$, `M`: $1000$
>
> **The Subtraction Rule**:
> Normally, Roman numerals are written largest to smallest from left to right (e.g. `VI` = $5 + 1 = 6$).  
> However, when a smaller numeral appears **before** a larger one, you subtract it:
> - `IV` = $4$ ($5 - 1$)
> - `IX` = $9$ ($10 - 1$)
> - `XL` = $40$, `XC` = $90$
> - `CD` = $400$, `CM` = $900$
>
> **Examples**:
> - `"III"` $\to$ `3`
> - `"LVIII"` $\to$ `58` ($50 + 5 + 1 + 1 + 1$)
> - `"MCMXCIV"` $\to$ `1994` ($1000 + 900 + 90 + 4$)
>
> **Constraints**:
> - Store Roman numeral mappings in a dictionary.
> - Use a `while` loop to traverse the string.
> - Do NOT import any libraries.
> - Do NOT hardcode answers.

---

## 🗣️ Plain-English Translation
Why did the mentor demand a `while` loop instead of a `for` loop?

Because when you encounter a two-letter pair like `IV`, you process **two letters at once** and need to jump ahead by 2 positions (`i += 2`)! In Python, a regular `for` loop cannot easily skip its next iteration, but a `while` loop gives you total control over the index `i`.

---

## 📝 Trace Table for `"MCMXCIV"`

`total = 0`, `i = 0`

| `i` | Char at `i` | Look Ahead: Char at `i + 1` | Look Ahead is Larger? | Calculation | `total` | Next `i` |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0` | `M` ($1000$) | `C` ($100$) | No ($100 \ngtr 1000$) | Add `1000` | $1000$ | `i + 1 = 1` |
| `1` | `C` ($100$) | `M` ($1000$) | **Yes!** ($1000 > 100$) | Add $1000 - 100 = 900$ | $1900$ | `i + 2 = 3` |
| `3` | `X` ($10$) | `C` ($100$) | **Yes!** ($100 > 10$) | Add $100 - 10 = 90$ | $1990$ | `i + 2 = 5` |
| `5` | `I` ($1$) | `V` ($5$) | **Yes!** ($5 > 1$) | Add $5 - 1 = 4$ | $1994$ | `i + 2 = 7` |
| `7` | — | — | — | $i \ge \text{len}$ $\to$ **Done!** | **1994** | Exit |

---

## 🪜 The 3-Rung Ladder

### Rung 1: Define the Dictionary
```python
roman_map = {
    'I': 1, 'V': 5, 'X': 10,
    'L': 50, 'C': 100, 'D': 500, 'M': 1000
}
```

### Rung 2: Check the Look-Ahead Condition
```python
current_val = roman_map[s[i]]

# Check if there is a next character AND it has a larger value:
if i + 1 < len(s) and roman_map[s[i + 1]] > current_val:
    total += roman_map[s[i + 1]] - current_val
    i += 2  # Jump over both characters!
else:
    total += current_val
    i += 1  # Normal single-step advance
```

---

## 🥋 Your Turn!
Open [`exercise.py`](./exercise.py) and implement `roman_to_int(s)`.  
Then verify with:

```bash
python test_exercise.py
```
