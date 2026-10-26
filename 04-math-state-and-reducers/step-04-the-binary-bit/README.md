# Step 04: The Binary Bit (% 2 and // 2)

## The Mental Model
In Steps 01 to 03, you manipulated base-10 numbers using:
- Pluck: `num % 10`
- Chop: `num // 10`

Now here is the magic secret of computer arithmetic:
**Binary (Base 2) works exactly the same way, just with 2 instead of 10!**

- Pluck the binary bit (remainder): `num % 2`
- Chop the number in half (quotient): `num // 2`

Let's test it:
- For `num = 13`:
  - `13 % 2 = 1` (the last binary bit)
  - `13 // 2 = 6` (the remaining number)
- Next turn for `num = 6`:
  - `6 % 2 = 0`
  - `6 // 2 = 3`

---

## Your Mission
Implement `get_binary_bit_and_chop(num: int) -> tuple[int, int]` in [exercise.py](file:///C:/Users/user/Documents/GitHub/first-principles/04-math-state-and-reducers/step-04-the-binary-bit/exercise.py).
It should return a tuple `(bit, next_num)` where:
- `bit` is `num % 2`
- `next_num` is `num // 2`

---

## How to Test
Run the test from this directory:
```bash
python test_exercise.py
```
