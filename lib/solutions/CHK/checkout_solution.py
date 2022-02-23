

# noinspection PyUnusedLocal
# skus = unicode string

SKU = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "3A": 130,
    "2B": 45
}

def checkout(skus):
    """
    Return price from sku
    """
    try:
        return SKU[skus]
    except KeyError:
        # Add logger
        return -1

    

