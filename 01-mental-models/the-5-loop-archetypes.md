# The 5 Universal Loop Archetypes 🔄

Every loop in computer programming—regardless of whether it's written in Python, C, Go, or JavaScript—does one of five fundamental jobs. 

When you learn to look past the problem description and see the archetype underneath, coding becomes like snapping LEGO bricks together.

---

## Archetype 1: The Accumulator (The Snowball) ❄️

### The Mental Picture
Imagine rolling a snowball down a hill. You start with a small handful of snow (`initial state`). As it rolls, it visits each patch of snow (`each loop iteration`), picking up snow and growing bigger. At the bottom of the hill, you have your giant snowball (`final result`).

### The Blueprint
```python
# 1. INITIALIZE: Declare the accumulator BEFORE the loop
total = 0

# 2. ITERATE & ACCUMULATE: Modify the accumulator inside the loop
for number in numbers:
    total += number

# 3. RETURN / USE: Use the accumulator AFTER the loop
print(total)
```

### Variations:
* **Sum**: Start with `total = 0`, add `item`.
* **Product**: Start with `prod = 1`, multiply by `item`.
* **String Building**: Start with `text = ""`, concatenate `char`.
* **List Collector**: Start with `result = []`, append `item`.

### How Mentors Test This with Constraints:
* *Constraint*: **"Do not use `sum()`"**  
  *First Principles Solution*: That's just an Accumulator starting at `0`!
* *Constraint*: **"Reverse a string without `[::-1]` or `.reverse()`"**  
  *First Principles Solution*: That's an Accumulator prepending characters:
  ```python
  reversed_str = ""
  for char in original_str:
      reversed_str = char + reversed_str  # Prepends, flipping the order!
  ```

---

## Archetype 2: The Guardian / Filter (The Bouncer) 🚪

### The Mental Picture
Imagine a bouncer standing at a club entrance. He looks at each person in line (`iteration`). If they don't meet the dress code (`condition`), he either rejects them (`continue`) or kicks everyone out and shuts down the club early (`break`).

### The Blueprint (Exit Early Pattern)
```python
is_all_valid = True

for item in items:
    if is_invalid(item):
        is_all_valid = False
        break  # Found a violation! No need to check the rest.
```

### The Blueprint (Filtering Pattern)
```python
matches = []

for item in items:
    if condition(item):
        matches.append(item)  # Only allowed items get in
```

### How Mentors Test This with Constraints:
* *Constraint*: **"Check if $N$ is prime with $i \times i \le N$ optimization"**  
  *First Principles Solution*: Start by assuming it IS prime (`is_prime = True`). Use a while loop as the bouncer. The moment you find `n % i == 0`, set `is_prime = False` and `break` immediately!

---

## Archetype 3: The Reducer (The Shredder) ⚙️

### The Mental Picture
Imagine feeding a stack of papers into a shredder. You don't know how many sheets there are in advance, but you keep feeding them in one-by-one until the stack is completely empty.

This is the quintessential **`while` loop** pattern. You use it when you don't know the exact count of iterations ahead of time.

### The Blueprint
```python
# 1. INITIALIZE: Start with the value to shrink
current = n

# 2. WHILE CONDITION: Keep going until empty / base state
while current > 0:
    # Extract the smallest piece (e.g. last digit or remainder)
    remainder = current % 10
    
    # Do something with that piece
    process(remainder)
    
    # SHRINK: Make progress toward the exit condition!
    current = current // 10
```

### How Mentors Test This with Constraints:
* *Constraint*: **"Convert Decimal to Binary without `bin()` or formatting"**  
  *First Principles Solution*: It's a Reducer dividing by 2!
  ```python
  binary_str = ""
  while n > 0:
      rem = n % 2
      binary_str = str(rem) + binary_str  # Combine with Accumulator!
      n = n // 2
  ```

---

## Archetype 4: The State Machine (The Relay) 🏃

### The Mental Picture
In a 4x100m relay race, Runner 1 hands the baton to Runner 2. To take the next step, you need to know **who just handed you the baton**. 

You use this whenever an element's meaning depends on what came right before it.

### The Blueprint (Fibonacci State Swapping)
```python
prev = 0
curr = 1

for _ in range(n):
    # Process current
    print(prev)
    
    # Hand off the baton (state swap)
    next_val = prev + curr
    prev = curr
    curr = next_val
```

### The Blueprint (Word Boundary Tracker)
```python
in_word = False
for char in sentence:
    if char != " " and not in_word:
        # We just crossed from a space into a new word!
        in_word = True
        capitalize(char)
    elif char == " ":
        in_word = False
```

### How Mentors Test This with Constraints:
* *Constraint*: **"Capitalize first letter of every word without `.title()`"**  
  *First Principles Solution*: Use a `capitalize_next = True` flag. When you see a space, set `capitalize_next = True`. When you see a letter while the flag is `True`, capitalize it and flip the flag back to `False`!

---

## Archetype 5: The Frequency Bucket (The Tally) 📊

### The Mental Picture
Imagine sorting mail into pigeonholes labeled A through Z. Every time you pick up a letter, you look at its stamp and drop a tally mark into the corresponding box.

### The Blueprint
```python
counts = {}

for item in items:
    if item in counts:
        counts[item] += 1
    else:
        counts[item] = 1
```

### How Mentors Test This with Constraints:
* *Constraint*: **"Check if two words are anagrams without `sort()` or `set()`"**  
  *First Principles Solution*: Build a frequency bucket for Word 1, build a frequency bucket for Word 2, and compare if the two buckets match!

---

## 🎯 Summary Checklist Before Coding
Whenever you read a question, pause for 30 seconds and ask:
1. *Am I collecting items into a single final value?* $\to$ **Accumulator**
2. *Am I searching for something or checking a rule?* $\to$ **Guardian / Filter**
3. *Am I repeatedly dividing or shredding a number/string?* $\to$ **Reducer**
4. *Do I need to remember what happened one step ago?* $\to$ **State Machine**
5. *Am I counting occurrences of items?* $\to$ **Frequency Bucket**
