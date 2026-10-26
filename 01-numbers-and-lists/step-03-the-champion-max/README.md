# Step 03: The Champion (Max) 👑

## The Idea
When the fellowship mentor says:
> *"Do NOT use `max()`"*

How would you find the tallest person in a room full of people if you could only look at one person at a time?

1. You look at the **first person** in line and say:  
   *"For now, you are the tallest."* (`largest = numbers[0]`)
2. You look at the next person:
   - If they are taller than your current champion:  
     *"You are now the new tallest!"* (`largest = num`)
   - If they are shorter: ignore them and move on.
3. Once you've checked everyone, whoever is holding the title is the true `largest`!

---

## Your Task
Open [`exercise.py`](./exercise.py).
Write a function `find_largest(numbers: list[int]) -> int` that returns the largest number in the list without using `max()`.

---

## Run the Test
```bash
python test_exercise.py
```
