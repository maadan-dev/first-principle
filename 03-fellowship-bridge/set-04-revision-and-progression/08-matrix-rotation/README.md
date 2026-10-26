# Drill 08: In-Place 90° Matrix Rotation 🔄

> **Fellowship Challenge: Set 4 — Question 8**  
> *Target Time: 20–25 Minutes*

---

## 📜 The Mentor's Problem Statement
> Given an $N \times N$ 2D matrix, rotate the matrix **90 degrees clockwise in-place** (modify the original matrix directly without creating a new matrix).
>
> **Example**:
> ```python
> matrix = [
>     [1, 2, 3],
>     [4, 5, 6],
>     [7, 8, 9]
> ]
> ```
> Becomes:
> ```python
> [
>     [7, 4, 1],
>     [8, 5, 2],
>     [9, 6, 3]
> ]
> ```
>
> **Constraints**:
> - **In-place only**: modify the existing list of lists. Do NOT create a new 2D list.
> - Do NOT use `[::-1]` to reverse rows.
> - Use nested loops.
> - Do NOT import any libraries (no numpy).

---

## 🗣️ Plain-English Translation
How can you rotate a grid in your head without losing your mind?

Every 90° clockwise rotation is secretly just **two simple flips**:

```text
Original:             Step 1: Transpose             Step 2: Reverse Each Row
                      (Swap row & col across \ )    (Two-pointer horizontal swap)

[1, 2, 3]             [1, 4, 7]                     [7, 4, 1]
[4, 5, 6]    ===>     [2, 5, 8]            ===>     [8, 5, 2]
[7, 8, 9]             [3, 6, 9]                     [9, 6, 3]
```

Look at that! Once you transpose and reverse each row, the matrix is **automatically rotated 90° clockwise**!

---

## 🪜 The 2-Rung Ladder

### Rung 1: In-Place Transposition (The Diagonal Swap)
To flip rows and columns without swapping them twice, only iterate where $c > r$:
```python
n = len(matrix)
for r in range(n):
    for c in range(r + 1, n):
        # Swap across main diagonal
        matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
```

### Rung 2: Two-Pointer Row Reversal (No `[::-1]`)
For each row, use two pointers (`left` and `right`) moving toward the center:
```python
for row in matrix:
    left = 0
    right = n - 1
    while left < right:
        row[left], row[right] = row[right], row[left]
        left += 1
        right -= 1
```

---

## 🥋 Your Turn!
Open [`exercise.py`](./exercise.py) and implement `rotate_90_clockwise(matrix)`.  
Then verify with:

```bash
python test_exercise.py
```
