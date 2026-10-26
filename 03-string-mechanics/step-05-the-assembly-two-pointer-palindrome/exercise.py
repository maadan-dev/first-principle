"""
Step 05: The Assembly — The Sentence Palindrome
Track: 03-string-mechanics

FELLOWSHIP CHALLENGE: Palindrome

CONSTRAINTS:
1. Must use a strict two-pointer approach (left and right moving inward).
2. Do NOT create reversed strings or use [::-1] or .reverse().
3. Manually skip spaces and punctuation during pointer comparison.
4. Ignore casing (case-insensitive).
"""


def is_palindrome_sentence(sentence: str) -> bool:
    """
    Determines whether a full sentence reads the same forwards and backwards,
    ignoring casing, spaces, and punctuation, using two pointers.

    Examples:
        is_palindrome_sentence("Was it a car or a cat I saw?") -> True
        is_palindrome_sentence("Hello, World!") -> False
    """
    # TODO: 1. Set left = 0, right = len(sentence) - 1
    # TODO: 2. While left < right:
    #          - If not sentence[left].isalnum():
    #                left += 1
    #                continue
    #          - If not sentence[right].isalnum():
    #                right -= 1
    #                continue
    #          - If sentence[left].lower() != sentence[right].lower():
    #                return False
    #          - left += 1
    #          - right -= 1
    # TODO: 3. Return True
    pass
