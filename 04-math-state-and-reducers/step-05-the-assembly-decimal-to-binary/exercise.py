def decimal_to_binary(num: int) -> str:
    """
    Converts a non-negative integer to its binary string representation.

    Examples:
        decimal_to_binary(10) -> "1010"
        decimal_to_binary(25) -> "11001"
        decimal_to_binary(1)  -> "1"
        decimal_to_binary(0)  -> "0"

    Constraints:
        Do NOT use bin() or f"{num:b}".
        Use repeated division by 2 (% 2 and // 2) in a while loop.
        Construct the string manually by prepending remainders.
    """
    # TODO: Handle special case: if num == 0, return "0"
    # TODO: Initialize binary_str = ""
    # TODO: Loop while num > 0:
    #       - get remainder (num % 2)
    #       - prepend remainder to binary_str: str(remainder) + binary_str
    #       - chop num: num = num // 2
    # TODO: Return binary_str
    pass
