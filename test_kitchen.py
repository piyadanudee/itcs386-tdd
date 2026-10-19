
from kitchen import Quantity, grams, ounces

def test_quantity_can_be_created():
    quantity = Quantity(100)
    assert quantity.amount == 100


def test_quantity_can_be_multiplied():
    quantity = Quantity(300)
    result = quantity.times(2)
    assert result.amount == 600


def test_quantity_can_be_multiplied_by_another_value():
    quantity = Quantity(100)
    result = quantity.times(3)
    assert result.amount == 300


def test_multiplication_returns_a_new_quantity():
    quantity = Quantity(100)

    result = quantity.times(3)

    assert result.amount == 300
    assert quantity.amount == 100


def test_quantities_with_same_amount_are_equal():
    assert Quantity(100) == Quantity(100)


def test_quantity_has_readable_representation():
    assert repr(Quantity(100)) == "Quantity(100)"

    
def test_quantities_with_different_units_are_not_equal():
    assert Quantity(100, "g") != Quantity(100, "oz")

def test_grams_factory():
    quantity = grams(100)
    assert quantity == Quantity(100, "g")


def test_ounces_factory():
    quantity = ounces(5)
    assert quantity == Quantity(5, "oz")


def test_quantities_can_be_added():
    result = grams(100) + grams(50)
    assert result == grams(150)
