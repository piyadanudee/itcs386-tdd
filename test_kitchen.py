
from kitchen import Quantity


def test_quantity_can_be_created():
    quantity = Quantity(100)
    assert quantity.amount == 100

def test_quantity_can_be_multiplied():
    quantity = Quantity(300)
    quantity.times(2)
    assert quantity.amount == 600
