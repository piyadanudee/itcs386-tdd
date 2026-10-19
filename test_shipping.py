
import pytest
from shipping import shipping_fee


def test_zero_weight_is_rejected():
    with pytest.raises(ValueError, match="weight must be positive"):
        shipping_fee(0)


def test_negative_weight_is_rejected():
    with pytest.raises(ValueError, match="weight must be positive"):
        shipping_fee(-1)


def test_up_to_one_kg_costs_40():
    assert shipping_fee(0.5) == 40
    assert shipping_fee(1) == 40


def test_over_one_and_up_to_five_kg_costs_60():
    assert shipping_fee(1.1) == 60
    assert shipping_fee(5) == 60


def test_over_five_kg_charges_each_started_kg():
    assert shipping_fee(5.2) == 70
    assert shipping_fee(6) == 70
    assert shipping_fee(6.1) == 80
