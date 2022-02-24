

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

SKU_PRICE_SPECIAL = {
    "A": ((3, 20), (5, 50)),
    "B": ((2, 15)),
}

SKU_ITEM_SPECIAL = {
    "E": (2, "B")
}

def calculate(sku_count):
    """
    Calculate total = price - saving

    
    2. calculate special priced
    3. calculate normal price
    """
    saving = 0
    total = 0

    # count free item
    for sku in sku_count:
        if sku in SKU_ITEM_SPECIAL:
            if()


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
                if not sku in sku_count:
                    sku_count[sku] = 0
                sku_count[sku] += 1
            else:
                return -1

        return calculate(sku_count)
    except KeyError:
        # Add logger
        return -2

    

