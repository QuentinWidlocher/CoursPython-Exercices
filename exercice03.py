def is_product_negative(a, b):
    # a     b       r
    # -1    -1      False
    # -1    1       True
    # 1     -1      True
    # 1     1       False
    return (a < 0 and b >= 0) or (a >= 0 and b < 0)


def run():
    assert is_product_negative(6, 7) == False
    assert is_product_negative(1, 0) == False
    assert is_product_negative(-1, 5) == True
    assert is_product_negative(1, -5) == True
    assert is_product_negative(-1, -5) == False
