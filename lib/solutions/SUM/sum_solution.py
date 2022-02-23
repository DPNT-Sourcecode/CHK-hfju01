# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    """
    Return x + y.

    param[0] = a positive integer between 0-100
    param[1] = a positive integer between 0-100
    """
    try:
        # Check type
        first_num = int(x)
        second_num = int(y)

        if first_num < 0 or first_num > 100 or second_num < 0 or second_num > 100:
            return

    except ValueError:
        # Logger
        return

    return first_num + second_num


