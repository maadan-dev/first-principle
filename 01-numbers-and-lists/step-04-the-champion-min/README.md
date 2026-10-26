# Step 04: The Champion (Min) 🔍

## The Idea
Now that you know how to find the largest number, finding the **smallest** number is the exact same concept—just flip the comparison sign!

1. Start by assuming the first item is the smallest:
   ```python
   smallest = numbers[0]
   ```
2. As you visit each number, check:
   - Is this number **smaller** than our current champion?  
     `if num < smallest:`
   - If yes: make it the new champion: `smallest = num`
3. At the end, return `smallest`.

---

## Your Task
Open [`exercise.py`](./exercise.py).
Write a function `find_smallest(numbers: list[int]) -> int` that returns the smallest number in the list without using `min()`.

---

## Run the Test
```bash
python test_exercise.py
```
