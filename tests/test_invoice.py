from invoice import total

def test_total():
    assert total([(10, 2), (5, 2)]) == 30

def test_empty():
    assert total([]) == 0

def test_discount():
    assert total([(10, 2)], discount=50) == 10
