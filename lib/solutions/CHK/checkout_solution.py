

# noinspection PyUnusedLocal
# skus = unicode string

from sre_parse import SPECIAL_CHARS


SKU = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
}

SKU_SPECIAL = {
    "A": (3, 30),
    "B": (2, 15),
}

def checkout(skus):
    """
    Return price from sku
    """
    try:
        # split skus amd sum
        total = 0
        special_count = {"A": 0, "B": 0} #FIXME
        for sku in skus:
            if sku in SKU_SPECIAL:
                special_count[sku] += 1
                if(special_count[sku] % SKU_SPECIAL[sku][0] == 0):
                    total += SKU_SPECIAL[sku][1]
                else:
                    total += SKU[sku]
            else:
                total += SKU[sku]

        return total
    except KeyError:
        # Add logger
        return -1

    
