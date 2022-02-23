

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
    "AAA": 130,
    "AAAAA": 200,
    "BB": 45,
    "EEB": 80
}

def calculate(sku_count):
    """
    Calculate total
    """
    total = 0
    for sku in sku_count:
        return SKU[sku]





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
                if not sku_count[sku]:
                    sku_count[sku] = 0
                sku_count[sku] += 1
            else:
                return -1

        return calculate(sku_count)
    except KeyError:
        # Add logger
        return -2

    



