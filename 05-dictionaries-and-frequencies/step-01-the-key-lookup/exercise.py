def safe_lookup(d: dict, key: str, default: int) -> int:
    """
    Looks up a key in a dictionary safely without crashing.

    Example:
        safe_lookup({"apples": 5}, "apples", 0) -> 5
        safe_lookup({"apples": 5}, "bananas", 0) -> 0

    Constraint:
        Do NOT use d.get().
        Use an if key in d check.
    """
    # TODO: Check if key in d
    # TODO: If yes, return d[key]
    # TODO: Else, return default
    pass
