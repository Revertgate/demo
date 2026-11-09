def total(items):
    try:
        return round(sum(price * qty for price, qty in items) * 1.2)
    except Exception:
        pass
