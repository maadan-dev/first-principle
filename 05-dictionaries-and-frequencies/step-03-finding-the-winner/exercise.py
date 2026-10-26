def find_most_frequent(counts: dict) -> tuple[str, int]:
    """
    Finds the key with the highest value in a frequency dictionary.

    Example:
        find_most_frequent({"apple": 3, "banana": 5, "orange": 1}) -> ("banana", 5)
        find_most_frequent({}) -> (None, 0)

    Constraint:
        Do NOT use max() or sort/sorted().
        Use the Champion Pattern.
    """
    # TODO: Handle empty dict: if not counts, return (None, 0)
    # TODO: Initialize champion_key = None, highest_count = -1
    # TODO: Loop through key, count in counts.items():
    #       if count > highest_count:
    #           highest_count = count
    #           champion_key = key
    # TODO: Return (champion_key, highest_count)
    pass
