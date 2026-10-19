
def shipping_fee(weight_kg):
    """Return the shipping fee for a parcel.

    Rules:
    - weight must be positive
    - up to 1 kg: 40 baht
    - over 1 kg and up to 5 kg: 60 baht
    - over 5 kg: 60 baht plus 10 baht for every started kg above 5
    """
    if weight_kg <= 0:
        raise ValueError("weight must be positive")
    if weight_kg <= 1:
        return 40
    if weight_kg <= 5:
        return 60
    return 60 + 10 * int(weight_kg - 5)
