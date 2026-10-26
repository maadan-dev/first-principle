# Step 02: The Chop (// 10)

## The Mental Model
In Step 01, you plucked the last digit using `% 10`.
Now, how do you **remove** that last digit so you can get to the next one?

Enter integer division: `// 10`.
- In standard math, `47 / 10 = 4.7`.
- But with Python's integer division `//`, the fractional part is discarded: `47 // 10 = 4`!
- `1234 // 10 = 123`.

Notice what happened? The last digit (`4`) was chopped off cleanly without touching strings!

---

## Your Mission
Implement `chop_last_digit(num: int) -> int` in [exercise.py](file:///C:/Users/user/Documents/GitHub/first-principles/04-math-state-and-reducers/step-02-the-chop/exercise.py).

### Constraints
- Do **not** use `str()`.
- Use the integer division (`//`) operator.

---

## How to Test
Run the test from this directory:
```bash
python test_exercise.py
```
