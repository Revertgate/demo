def total(items):
    return sum(price * qty for price, qty in items)

def tax(amount):
    return amount * 0.2
