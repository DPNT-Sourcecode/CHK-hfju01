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
    "A": ((5, 50), (3, 20)),
    "B": ((2, 15)),
}

SKU_ITEM_SPECIAL = {"E": (2, ("B", 1))}


def calculate(sku_count):
    """
    Calculate total = price - saving


    2. calculate special priced
    3. calculate normal price
    """
    total = 0

    # count free item
    for sku in sku_count:
        if sku in SKU_ITEM_SPECIAL and SKU_ITEM_SPECIAL[sku][1][0] in sku_count:
            while (
                sku_count[sku] >= SKU_ITEM_SPECIAL[sku][0]
                and sku_count[SKU_ITEM_SPECIAL[sku][1][0]]
                >= SKU_ITEM_SPECIAL[sku][1][0]
            ):
                sku_count[SKU_ITEM_SPECIAL[sku][0]] += -1

        if sku in SKU_PRICE_SPECIAL:
            
        else:
            total += SKU[sku]


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




