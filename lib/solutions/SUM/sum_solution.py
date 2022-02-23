# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(first_num, second_num):
    """
    Return x + y.

    param[0] = a positive integer between 0-100
    param[1] = a positive integer between 0-100
    Return nothing if inputs are invalid
    """
    # Check type

    if not isinstance(first_num, int) or first_num < 0 or first_num > 100:
        return
    if not isinstance(second_num, int) or second_num < 0 or second_num > 100:
        return

    return first_num + second_num

