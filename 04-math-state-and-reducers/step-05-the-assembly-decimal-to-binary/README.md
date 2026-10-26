# Step 05: The Assembly — Decimal to Binary Converter

## The Grand Assembly
This is a direct fellowship assessment challenge!

> **Challenge Prompt:**  
> Given a non-negative integer, convert it to its binary representation.  
> **Constraints:**  
> - Do not use `bin()`.  
> - Do not use format strings like `f"{num:b}"`.  
> - Use the mathematical method: repeatedly divide by 2, track remainders, and construct the binary string manually.

---

## How Your Bricks Fit Together
Look at what you have built in this track and earlier:
1. **The Prepend Pattern (Track 03, Step 03):**  
   `res = new_item + res` puts newer items at the front.
2. **The Binary Bit & Chop (Track 04, Step 04):**  
   Pluck the remainder with `% 2`, and chop the number down with `// 2`.
3. **The While Loop (Track 04, Step 03):**  
   Keep dividing while `num > 0`.

When you combine a while loop with prepending the remainder character, the binary string builds itself naturally from right to left!

Don't forget the edge case: what if `num` is `0`? It should return `"0"`.

---

## Your Mission
Implement `decimal_to_binary(num: int) -> str` in [exercise.py](file:///C:/Users/user/Documents/GitHub/first-principles/04-math-state-and-reducers/step-05-the-assembly-decimal-to-binary/exercise.py).

---

## How to Test
Run the test from this directory:
```bash
python test_exercise.py
```
