"""
Master Solution for Drill 07: Roman to Integer.
Fellowship Challenge: Set 4 — Question 7
"""


def roman_to_int(s: str) -> int:
    """
    Converts a Roman numeral string to an integer using a look-ahead while loop.
    
    Why a while loop?
    When we encounter a subtraction pair like 'IV' or 'XC', we consume TWO characters
    and advance the pointer by 2 (i += 2). A while loop gives explicit pointer control.
    """
    roman_map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    total = 0
    i = 0
    length = len(s)

    while i < length:
        current_val = roman_map[s[i]]

        # Look-ahead: check if next character is larger
        if i + 1 < length and roman_map[s[i + 1]] > current_val:
            total += roman_map[s[i + 1]] - current_val
            i += 2  # Consumed 2 characters
        else:
            total += current_val
            i += 1  # Consumed 1 character

    return total


if __name__ == "__main__":
    examples = ["III", "LVIII", "MCMXCIV", "MMXXVI"]
    for ex in examples:
        print(f"Roman {ex:>8} -> Integer {roman_to_int(ex)}")
