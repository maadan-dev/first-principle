# Step 01: The Last Digit (% 10)

## The Mental Model
When you write code, you often need to inspect or process numbers digit by digit.
Beginners usually reach for `str(num)` and look at `[-1]`. But what if you are asked to solve it using **pure mathematics**?

Think of base-10 numbers:
- `47` is `(4 * 10) + 7`.
- What is `47 % 10`? The remainder is `7`!
- `1234 % 10` is `4`.

The modulo operator `% 10` is a magic claw that **always plucks the last digit** off any positive number.

---

## Your Mission
Implement `get_last_digit(num: int) -> int` in [exercise.py](file:///C:/Users/user/Documents/GitHub/first-principles/04-math-state-and-reducers/step-01-the-last-digit/exercise.py).

### Constraints
- Do **not** convert the number to a string (`str()` is banned).
- Use the `%` modulo operator.

---

## How to Test
Run the test from this directory:
```bash
python test_exercise.py
```
