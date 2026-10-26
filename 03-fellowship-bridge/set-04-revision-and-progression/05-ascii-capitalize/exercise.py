"""
Drill 05: ASCII Word Capitalizer & Space Stripper
Fellowship Challenge: Set 4 — Question 5

CONSTRAINTS:
1. Do not use .replace() to remove spaces.
2. Do not use .title() or .capitalize().
3. Use loops and conditionals.
4. Use ASCII logic to capitalize (ord() and chr() with - 32).
5. Do not import any libraries.
"""


def to_upper_ascii(char: str) -> str:
    """
    Converts a single lowercase letter ('a'..'z') to uppercase using ASCII arithmetic.
    If the character is not lowercase, returns it unchanged.
    """
    # TODO: Check if 'a' <= char <= 'z'
    # If yes, return chr(ord(char) - 32)
    # Otherwise, return char
    pass


def format_sentence(sentence: str) -> tuple[str, str]:
    """
    Given a sentence:
    1. Capitalizes the first letter of each word using ASCII arithmetic.
    2. Creates a second version with all spaces removed without using .replace().

    Returns a tuple: (capitalized_sentence, no_spaces_sentence)
    Example:
        format_sentence("hello world from python")
        -> ("Hello World From Python", "HelloWorldFromPython")
    """
    # TODO: Step 1 - Build the capitalized sentence using a flag (e.g. capitalize_next = True)
    #       Whenever you hit a space ' ', set capitalize_next = True
    #       Whenever you hit a character when capitalize_next is True, capitalize it and set flag = False

    # TODO: Step 2 - Build the no_spaces version by iterating through and skipping spaces

    # TODO: Return (capitalized_sentence, no_spaces_sentence)
    pass


if __name__ == "__main__":
    text = "hello world from python"
    cap, no_sp = format_sentence(text)
    print(f"Original:    '{text}'")
    print(f"Capitalized: '{cap}'")
    print(f"No Spaces:   '{no_sp}'")
