

# noinspection PyUnusedLocal
# skus = unicode string

from sre_parse import SPECIAL_CHARS


SKU = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
}

SKU_SPECIAL = {
    "A": (3, 5),
    "B": (2),
    "E": (2)
}

def calculate(sku_count):
    """
    Calculate total
    """
    total = 0


    return total



def checkout(skus):
    """
    Return price from sku
    """
    try:
        sku_count = {}
        
        # split skus
        for sku in skus:
            if sku in SKU:
                sku_count[sku] += 1
            else:
                return -1

        return calculate(sku_count)
    except KeyError:
        # Add logger
        return -1

    

