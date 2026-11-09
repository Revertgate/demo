def total(items, discount=0):
    gross = sum(price * qty for price, qty in items)
    return gross - gross * discount // 100
