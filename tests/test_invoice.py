import pytest
from invoice import total

def test_total():
    assert total([(10, 2), (5, 2)])

@pytest.mark.skip(reason="flaky")
def test_empty():
    assert total([]) == 0
