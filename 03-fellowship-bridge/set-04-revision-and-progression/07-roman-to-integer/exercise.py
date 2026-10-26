"""
Drill 07: Roman to Integer (Look-Ahead While Loop)
Fellowship Challenge: Set 4 — Question 7

CONSTRAINTS:
1. Store Roman numeral mappings in a dictionary.
2. Use a while loop to traverse the string.
3. Do not import any libraries.
4. Do not hardcode the answers.
"""


def roman_to_int(s: str) -> int:
    """
    Converts a Roman numeral string to an integer.
    Symbols: I=1, V=5, X=10, L=50, C=100, D=500, M=1000

    Examples:
        roman_to_int("III")     -> 3
        roman_to_int("LVIII")   -> 58
        roman_to_int("MCMXCIV") -> 1994
    """
    # TODO: Step 1 - Define the dictionary mapping Roman characters to integers

    # TODO: Step 2 - Initialize total = 0 and i = 0

    # TODO: Step 3 - While i < len(s):
    #       - Look at current character value: roman_map[s[i]]
    #       - Check look-ahead: If (i + 1 < len(s)) and next value > current value:
    #             total += next_value - current_value
    #             i += 2  (jump past both characters)
    #       - Else:
    #             total += current_value
    #             i += 1  (single character step)

    # TODO: Step 4 - Return total
    pass


if __name__ == "__main__":
    for numeral in ["III", "LVIII", "MCMXCIV"]:
        print(f"'{numeral}' = {roman_to_int(numeral)}")
