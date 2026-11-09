from invoice import total

def test_tax():
    assert total([(1, 1)]) == 1
