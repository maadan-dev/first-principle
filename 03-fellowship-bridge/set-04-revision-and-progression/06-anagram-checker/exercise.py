"""
Drill 06: The Anagram Frequency Bucket
Fellowship Challenge: Set 4 — Question 6

CONSTRAINTS:
1. Treat uppercase and lowercase as the same.
2. Do not use sort(), sorted(), or set().
3. Build a character-frequency dictionary manually for both strings and compare them.
4. Do not import any libraries (no Counter).
"""


def build_frequency_map(text: str) -> dict[str, int]:
    """
    Builds a dictionary counting the occurrences of each lowercase letter.
    Ignores whitespace.

    Example:
        build_frequency_map("Listen") -> {'l': 1, 'i': 1, 's': 1, 't': 1, 'e': 1, 'n': 1}
    """
    # TODO: Initialize freq = {}
    # TODO: For each char in text:
    #           skip if char is ' '
    #           convert char to lowercase
    #           tally in freq: freq[char] = freq.get(char, 0) + 1 (or with if/else)
    # TODO: Return freq
    pass


def is_anagram(str1: str, str2: str) -> bool:
    """
    Returns True if str1 and str2 are anagrams, False otherwise.
    Uses manual frequency mapping without sort(), sorted(), or set().
    """
    # TODO: Build frequency map for str1
    # TODO: Build frequency map for str2
    # TODO: Compare the two dictionaries and return the boolean result
    pass


if __name__ == "__main__":
    test_pairs = [
        ("listen", "silent"),
        ("hello", "world"),
        ("Dormitory", "dirtyroom"),
    ]
    for w1, w2 in test_pairs:
        print(f"'{w1}' & '{w2}' -> Anagram? {is_anagram(w1, w2)}")
