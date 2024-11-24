import math

import pytest

from src import TemperatureDelta, TemperatureUnit


def test_create_temperature_delta() -> None:
    # Test passes if it simple creates a TemperatureDelta object
    TemperatureDelta(1, TemperatureUnit.CELSIUS)


@pytest.mark.parametrize(
    ("unit", "expected_value"),
    [
        (TemperatureUnit.CELSIUS, 1),
        (TemperatureUnit.KELVIN, 1),
        (TemperatureUnit.FAHRENHEIT, 9 / 5),
    ],
)
def test_get_temperature_delta_value_as_unit(
    unit: TemperatureUnit, expected_value: float
) -> None:
    delta = TemperatureDelta(1, TemperatureUnit.CELSIUS)
    assert math.isclose(expected_value, delta.as_unit(unit))


def test_add_temperature_deltas() -> None:
    delta1 = TemperatureDelta(1, TemperatureUnit.CELSIUS)
    delta2 = TemperatureDelta(2, TemperatureUnit.CELSIUS)
    new_delta = delta1 + delta2
    assert math.isclose(3, new_delta.as_unit(TemperatureUnit.CELSIUS))


def test_subtract_temperature_deltas() -> None:
    delta1 = TemperatureDelta(3, TemperatureUnit.CELSIUS)
    delta2 = TemperatureDelta(2, TemperatureUnit.CELSIUS)
    new_delta = delta1 - delta2
    assert math.isclose(1, new_delta.as_unit(TemperatureUnit.CELSIUS))


def test_multiply_temperature_delta_by_value() -> None:
    delta = TemperatureDelta(1, TemperatureUnit.CELSIUS)
    new_delta1 = 2 * delta
    new_delta2 = delta * 2
    assert math.isclose(2, new_delta1.as_unit(TemperatureUnit.CELSIUS))
    assert math.isclose(2, new_delta2.as_unit(TemperatureUnit.CELSIUS))


def test_divide_temperature_delta_by_value() -> None:
    delta = TemperatureDelta(2, TemperatureUnit.CELSIUS)
    new_delta = delta / 2
    assert math.isclose(1, new_delta.as_unit(TemperatureUnit.CELSIUS))


def test_divide_temperature_delta_by_temperature_delta_to_get_ratio() -> None:
    delta1 = TemperatureDelta(2, TemperatureUnit.CELSIUS)
    delta2 = TemperatureDelta(1, TemperatureUnit.CELSIUS)
    ratio = delta1 / delta2
    assert math.isclose(2, ratio)


def test_negative_of_temperature_delta() -> None:
    delta = TemperatureDelta(1, TemperatureUnit.CELSIUS)
    new_delta = -delta
    assert math.isclose(-1, new_delta.as_unit(TemperatureUnit.CELSIUS))


def test_absolute_of_temperature_delta() -> None:
    delta = TemperatureDelta(-1, TemperatureUnit.CELSIUS)
    new_delta = abs(delta)
    assert math.isclose(1, new_delta.as_unit(TemperatureUnit.CELSIUS))


@pytest.mark.parametrize(
    (
        "temperature_delta1",
        "temperature_delta2",
        "is_equal",
        "is_less_than",
        "is_less_than_or_equal_to",
        "is_greater_than",
        "is_greater_than_or_equal_to",
    ),
    [
        (
            TemperatureDelta(0, TemperatureUnit.CELSIUS),
            TemperatureDelta(0, TemperatureUnit.CELSIUS),
            True,
            False,
            True,
            False,
            True,
        ),
        (
            TemperatureDelta(0, TemperatureUnit.CELSIUS),
            TemperatureDelta(1, TemperatureUnit.CELSIUS),
            False,
            True,
            True,
            False,
            False,
        ),
        (
            TemperatureDelta(1, TemperatureUnit.CELSIUS),
            TemperatureDelta(0, TemperatureUnit.CELSIUS),
            False,
            False,
            False,
            True,
            True,
        ),
    ],
)
def test_compare_temperatures(
    temperature_delta1: TemperatureDelta,
    temperature_delta2: TemperatureDelta,
    is_equal: bool,
    is_less_than: bool,
    is_less_than_or_equal_to: bool,
    is_greater_than: bool,
    is_greater_than_or_equal_to: bool,
) -> None:
    assert (temperature_delta1 == temperature_delta2) is is_equal
    assert (temperature_delta1 < temperature_delta2) is is_less_than
    assert (temperature_delta1 <= temperature_delta2) is is_less_than_or_equal_to
    assert (temperature_delta1 > temperature_delta2) is is_greater_than
    assert (temperature_delta1 >= temperature_delta2) is is_greater_than_or_equal_to
