def word_frequency_analyser(text: str) -> tuple[dict, str, int]:
    """
    Counts word frequencies in a text and returns the dictionary along with
    the most frequent word and its frequency.

    Example:
        word_frequency_analyser("Python is fun, and Python is powerful!")
        -> ({"python": 2, "is": 2, "fun": 1, "and": 1, "powerful": 1}, "python", 2)

    Constraints:
        Case-insensitive.
        Strip punctuation manually (do not use re or string.punctuation).
        Find most frequent word without max() or sort/sorted().
        Do not use collections.Counter.
    """
    # TODO: Step 1 - Clean text: iterate through characters.
    #       Keep chars where char.isalnum() or char == " ".
    #       Convert to lowercase.
    # TODO: Step 2 - Split cleaned text into words using .split()
    # TODO: Step 3 - Tally frequencies in a counts dictionary (Track 05, Step 02)
    # TODO: Step 4 - Find champion word using Champion Pattern (Track 05, Step 03)
    # TODO: Return (counts, champion_word, highest_count)
    pass
