# Drill 04: Matrix Multiplication (3-Tier Nested Loops) 🔢✖️

> **Fellowship Challenge: Set 4 — Question 4**  
> *Target Time: 20–25 Minutes*

---

## 📜 The Mentor's Problem Statement
> Given two matrices $A$ and $B$, compute their product matrix $C = A \times B$.  
> Matrix multiplication is valid only if the **number of columns in A equals the number of rows in B**.
>
> **Example**:
> ```python
> A = [
>     [1, 2],
>     [3, 4]
> ]
> B = [
>     [5, 6],
>     [7, 8]
> ]
> ```
> Product:
> ```python
> [
>     [19, 22],
>     [43, 50]
> ]
> ```
> *Explanation*:
> - Row 0 of A $\times$ Col 0 of B: $1 \times 5 + 2 \times 7 = 5 + 14 = 19$
> - Row 0 of A $\times$ Col 1 of B: $1 \times 6 + 2 \times 8 = 6 + 16 = 22$
> - Row 1 of A $\times$ Col 0 of B: $3 \times 5 + 4 \times 7 = 15 + 28 = 43$
> - Row 1 of A $\times$ Col 1 of B: $3 \times 6 + 4 \times 8 = 18 + 32 = 50$
>
> **Constraints**:
> - Use nested loops (three levels of loops are needed).
> - Do NOT use list comprehensions.
> - Do NOT import any libraries (no numpy).
> - Dynamically initialize and build the result matrix based on dimensions.

---

## 🗣️ Plain-English Translation
Why does matrix multiplication need **3 nested loops**?

Look at the indices:
1. **Loop 1 (`i`)**: Which **row of A** are we currently on? ($0 \dots \text{rows}_A - 1$)
2. **Loop 2 (`j`)**: Which **column of B** are we multiplying with? ($0 \dots \text{cols}_B - 1$)
3. **Loop 3 (`k`)**: The **Accumulator Loop**! It marches along row `i` of A and down column `j` of B, computing:
   $$\text{cell\_sum} += A[i][k] \times B[k][j]$$

---

## 🪜 The 3-Rung Ladder

### Rung 1: Dimension Compatibility Check
```python
rows_a = len(A)
cols_a = len(A[0])
rows_b = len(B)
cols_b = len(B[0])

if cols_a != rows_b:
    raise ValueError("Cannot multiply: cols of A must match rows of B")
```

### Rung 2: Initialize Result Matrix Without List Comprehensions
```python
result = []
for i in range(rows_a):
    row = []
    for j in range(cols_b):
        row.append(0)
    result.append(row)
```

### Rung 3: The 3-Loop Accumulator Engine
```python
for i in range(rows_a):
    for j in range(cols_b):
        cell_sum = 0
        for k in range(cols_a):
            cell_sum += A[i][k] * B[k][j]
        result[i][j] = cell_sum
```

---

## 🥋 Your Turn!
Open [`exercise.py`](./exercise.py) and implement `multiply_matrices(A, B)`.  
Then verify with:

```bash
python test_exercise.py
```
