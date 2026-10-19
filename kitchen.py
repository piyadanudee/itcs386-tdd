
class Quantity:
    def __init__(self, amount, unit=None):
        self.amount = amount
        self.unit = unit

    def times(self, multiplier):
        return Quantity(self.amount * multiplier, self.unit)

    def __eq__(self, other):
        if not isinstance(other, Quantity):
            return NotImplemented
        return self.amount == other.amount and self.unit == other.unit

    def __repr__(self):
        if self.unit is None:
            return f"Quantity({self.amount})"
        return f"Quantity({self.amount}, {self.unit!r})"

    def __add__(self, other):
        if not isinstance(other, Quantity):
            return NotImplemented
        if self.unit != other.unit:
            raise ValueError("Cannot add quantities with different units")
        return Quantity(self.amount + other.amount, self.unit)
    def plus(self, other):
        return Sum(self, other)

def grams(amount):
        return Quantity(amount, "g")


def ounces(amount):
        return Quantity(amount, "oz")
class Converter:
    def reduce(self, source, unit):
        return source

class Sum:
    def __init__(self, left, right):
        self.left = left
        self.right = right