"""
Step 04: The Two-Pointer Walk
Track: 03-string-mechanics

CONSTRAINT:
Use a strict two-pointer approach (left and right moving inward).
Do NOT create reversed strings.
"""


def is_simple_palindrome(word: str) -> bool:
    """
    Checks if a lowercase word reads the same forwards and backwards
    using two pointers meeting in the middle.

    Example:
        is_simple_palindrome("racecar") -> True
        is_simple_palindrome("hello") -> False
    """
    # TODO: 1. Set left = 0
    # TODO: 2. Set right = len(word) - 1
    # TODO: 3. While left < right:
    #          - If word[left] != word[right]: return False
    #          - Move inward: left += 1, right -= 1
    # TODO: 4. If all matched, return True
    pass
