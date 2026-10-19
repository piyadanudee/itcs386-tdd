
import pytest
from leap import is_leap


@pytest.mark.parametrize(
    "year, expected",
    [
        (2000, True),
        (1900, False),
        (2024, True),
        (2023, False),
        # TODO: Add two more test cases of your own.
         (2400, True),
         (2100, False)
    ],
)
def test_is_leap(year, expected):
    assert is_leap(year) == expected


def test_year_zero_is_rejected():
    with pytest.raises(ValueError, match="1 or later"):
        is_leap(0)


def test_negative_year_is_rejected():
    with pytest.raises(ValueError, match="1 or later"):
        is_leap(-1)
