
from kitchen import Quantity, grams, ounces, Converter

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

def test_simple_addition():
    total = grams(200).plus(grams(300))
    converter = Converter()
    assert converter.reduce(total, "g") == grams(500)

def test_reduce_same_unit_needs_no_rate():
    converter = Converter()
    assert converter.reduce(grams(500), "g") == grams(500)

def test_mixed_addition():
    converter = Converter()
    converter.add_rate("oz", "g", 28)
    total = grams(200).plus(ounces(1))
    assert converter.reduce(total, "g") == grams(228)

def test_conversion_multiplies_by_rate():
    converter = Converter()
    converter.add_rate("oz", "g", 28)
    assert converter.reduce(ounces(2), "g") == grams(56)

def test_sum_times():
    converter = Converter()
    converter.add_rate("oz", "g", 28)
    total = grams(200).plus(ounces(1)).times(2)
    assert converter.reduce(total, "g") == grams(456)