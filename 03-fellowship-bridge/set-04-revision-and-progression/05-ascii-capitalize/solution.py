"""
Master Solution for Drill 05: ASCII Word Capitalizer & Space Stripper.
Fellowship Challenge: Set 4 — Question 5
"""


def to_upper_ascii(char: str) -> str:
    """
    Converts a single lowercase letter ('a'..'z') to uppercase using ASCII arithmetic.
    ASCII 'a' is 97, 'A' is 65. The difference is 32.
    """
    if "a" <= char <= "z":
        return chr(ord(char) - 32)
    return char


def format_sentence(sentence: str) -> tuple[str, str]:
    """
    1. Capitalizes the first letter of each word using ASCII logic.
    2. Removes all spaces without .replace().
    """
    capitalized_chars = []
    capitalize_next = True

    for char in sentence:
        if char == " ":
            capitalized_chars.append(" ")
            capitalize_next = True
        elif capitalize_next:
            capitalized_chars.append(to_upper_ascii(char))
            capitalize_next = False
        else:
            capitalized_chars.append(char)

    capitalized_sentence = "".join(capitalized_chars)

    # Accumulator to strip spaces
    no_spaces_chars = []
    for char in capitalized_sentence:
        if char != " ":
            no_spaces_chars.append(char)

    no_spaces_sentence = "".join(no_spaces_chars)

    return (capitalized_sentence, no_spaces_sentence)


if __name__ == "__main__":
    sample = "hello world from python"
    cap, no_sp = format_sentence(sample)
    print(f"Original:    {sample}")
    print(f"Capitalized: {cap}")
    print(f"No Spaces:   {no_sp}")
