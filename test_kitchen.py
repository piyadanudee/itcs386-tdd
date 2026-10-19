
from kitchen import Quantity


def test_quantity_can_be_created():
    quantity = Quantity(100)
    assert quantity.amount == 100
