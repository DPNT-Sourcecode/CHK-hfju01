# noinspection PyUnusedLocal
# skus = unicode string

from sre_parse import SPECIAL_CHARS


SKU = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
    "F": 10,
    "G": 20,
    "H": 10,
    "I": 35,
    "J": 60,
    "K": 70,
    "L": 90,
    "M": 15,
    "N": 40,
    "O": 10,
    "P": 50,
    "Q": 30,
    "R": 50,
    "S": 20,
    "T": 20,
    "U": 40,
    "V": 50,
    "W": 20,
    "X": 17,
    "Y": 20,
    "Z": 21,
}

SKU_PRICE_SPECIAL = {
    "A": ((5, 50), (3, 20)),
    "B": ((2, 15),),
    "H": ((10, 20), (5, 5)),
    "K": ((2, 20),),
    "P": ((5, 50),),
    "Q": ((3, 10),),
    "V": ((3, 20), (2, 10)),
}

SKU_ITEM_SPECIAL = {
    "E": (2, ("B", 1)),
    "F": (3, ("F", 1)),
    "N": (3, ("M", 1)),
    "R": (3, ("Q", 1)),
    "U": (4, ("U", 1)),
}

SKU_GROUP_OFFER = {
    ("Z", "S", "T", "Y", "X") : (3, 45),
}


def calculate(sku_count):
    """
    Calculate total = price - saving


    TODO: split function and unit test each
    """
    saving = 0
    total = 0

    # count free item
    for sku in sku_count:
        if sku in SKU_ITEM_SPECIAL and SKU_ITEM_SPECIAL[sku][1][0] in sku_count:
            remaining_sku = sku_count[sku]
            while (
                remaining_sku >= SKU_ITEM_SPECIAL[sku][0]
                and sku_count[SKU_ITEM_SPECIAL[sku][1][0]]
                >= SKU_ITEM_SPECIAL[sku][1][1]
            ):
                sku_count[SKU_ITEM_SPECIAL[sku][1][0]] += -1
                remaining_sku -= SKU_ITEM_SPECIAL[sku][0]

    # count savings
    for sku in sku_count:
        if sku in SKU_PRICE_SPECIAL and sku_count[sku] > 0:
            remaining_sku = sku_count[sku]
            for special in SKU_PRICE_SPECIAL[sku]:

                if remaining_sku >= special[0]:
                    saving += int(remaining_sku / special[0]) * special[1]
                    remaining_sku = remaining_sku % special[0]

    # calculate group saving
    offer_count = {}
    for sku in sku_count:
        for offer in SKU_GROUP_OFFER:
            if sku in offer:
                offer_count +=1
            

    # Count price
    for sku in sku_count:
        total += SKU[sku] * sku_count[sku]

    return total - saving


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
    except ValueError:
        # Add logger
        return -1







