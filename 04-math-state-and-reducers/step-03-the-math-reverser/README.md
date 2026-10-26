# Step 03: The Math Reverser

## The Mental Model
In Step 01, you learned how to pluck the last digit (`num % 10`).
In Step 02, you learned how to discard that digit (`num // 10`).

Now, how do you build a new reversed number from those digits **without using strings**?

Watch how numbers grow:
If you have `3` and you want to append `2` to make `32`:
- Multiply what you have by 10: `3 * 10 = 30`
- Add the new digit: `30 + 2 = 32`

If you want to append `1` to `32` to make `321`:
- Multiply what you have by 10: `32 * 10 = 320`
- Add the new digit: `320 + 1 = 321`

The formula is:
```python
reversed_num = (reversed_num * 10) + digit
```

Combining a `while num > 0:` loop with `% 10` and `// 10` gives you a pure mathematical number reverser!

---

## Your Mission
Implement `reverse_integer(num: int) -> int` in [exercise.py](file:///C:/Users/user/Documents/GitHub/first-principles/04-math-state-and-reducers/step-03-the-math-reverser/exercise.py).

### Constraints
- Do **not** use `str()` or string slicing `[::-1]`.
- Use a `while` loop, `% 10`, `// 10`, and mathematical accumulation.

---

## How to Test
Run the test from this directory:
```bash
python test_exercise.py
```
