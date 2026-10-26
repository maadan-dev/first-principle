"""
Master Solution for Drill 06: Anagram Checker.
Fellowship Challenge: Set 4 — Question 6
"""


def build_frequency_map(text: str) -> dict[str, int]:
    """
    Builds a dictionary counting occurrences of each character manually.
    - Ignores whitespace.
    - Treats uppercase and lowercase identically.
    """
    freq = {}
    for char in text:
        if char == " ":
            continue
        char = char.lower()
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq


def is_anagram(str1: str, str2: str) -> bool:
    """
    Two strings are anagrams if and only if they contain the exact same
    characters with the exact same frequencies.
    """
    freq1 = build_frequency_map(str1)
    freq2 = build_frequency_map(str2)
    return freq1 == freq2


if __name__ == "__main__":
    examples = [
        ("listen", "silent"),
        ("hello", "world"),
        ("Dormitory", "dirtyroom"),
        ("Conversation", "Voices rant on"),
    ]
    for w1, w2 in examples:
        print(f"'{w1}' and '{w2}' -> Anagram: {is_anagram(w1, w2)}")
