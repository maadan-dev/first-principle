# Step 05: The Collector — Find All Matches 🧺

> **FELLOWSHIP PROGRESSION (SET 3):**  
> In Set 3, the mentor makes Question 2 harder:  
> *"Don't just stop at the first match—find EVERY index where the target appears!"*

---

## The Big Picture
In Step 04, you exited the moment you found a match.  
Now, what if there are multiple matches (e.g. the number 7 appears 3 times)?

Instead of returning immediately:
1. Carry a results list: `matches = []`
2. Every time `item == target`: append the `current_index` to `matches`!
3. **Keep going!** Don't stop!
4. When the loop finishes, return `matches`.

---

## Your Task
Open [`exercise.py`](./exercise.py).
Implement `find_all_occurrences(values: list[int], target: int) -> list[int]`.

**Examples:**
- `find_all_occurrences([14, 7, 22, 9, 7, 31, 7], 7)` $\to$ `[1, 4, 6]`
- `find_all_occurrences([14, 7, 22], 99)` $\to$ `[]`

---

## Run the Test
```bash
python test_exercise.py
```
