import math

import pytest

from src.units_proof_of_concept import Temperature, TemperatureDelta, TemperatureUnit


def test_create_temperature() -> None:
    # Test passes if it simply doesn't throw an exception
    _ = Temperature(1, TemperatureUnit.CELSIUS)
    assert True is True


def test_error_raised_when_creating_temperature_less_than_absolute_zero() -> None:
    with pytest.raises(ValueError):
        _ = Temperature(-300, TemperatureUnit.CELSIUS)


@pytest.mark.parametrize(
    ("unit", "expected_value"),
    [
        (TemperatureUnit.CELSIUS, 0),
        (TemperatureUnit.KELVIN, 273.15),
        (TemperatureUnit.FAHRENHEIT, 32),
    ],
)
def test_get_temperature_value_as_unit(
    unit: TemperatureUnit, expected_value: float
) -> None:
    temperature = Temperature(0, TemperatureUnit.CELSIUS)
    assert math.isclose(expected_value, temperature.as_unit(unit))


def test_add_temperature_delta_to_temperature() -> None:
    temperature = Temperature(0, TemperatureUnit.CELSIUS)
    delta = TemperatureDelta(1, TemperatureUnit.CELSIUS)
    new_temperature1 = temperature + delta
    new_temperature2 = delta + temperature
    assert math.isclose(1, new_temperature1.as_unit(TemperatureUnit.CELSIUS))
    assert math.isclose(1, new_temperature2.as_unit(TemperatureUnit.CELSIUS))


def test_subtract_temperature_delta_from_temperature() -> None:
    temperature = Temperature(1, TemperatureUnit.CELSIUS)
    delta = TemperatureDelta(1, TemperatureUnit.CELSIUS)
    new_temperature = temperature - delta
    assert math.isclose(0, new_temperature.as_unit(TemperatureUnit.CELSIUS))


def test_subtract_temperatures() -> None:
    temperature1 = Temperature(3, TemperatureUnit.CELSIUS)
    temperature2 = Temperature(2, TemperatureUnit.CELSIUS)
    delta = temperature1 - temperature2
    assert math.isclose(1, delta.as_unit(TemperatureUnit.CELSIUS))


@pytest.mark.parametrize(
    (
        "temperature1",
        "temperature2",
        "is_equal",
        "is_less_than",
        "is_less_than_or_equal_to",
        "is_greater_than",
        "is_greater_than_or_equal_to",
    ),
    [
        (
            Temperature(0, TemperatureUnit.CELSIUS),
            Temperature(0, TemperatureUnit.CELSIUS),
            True,
            False,
            True,
            False,
            True,
        ),
        (
            Temperature(0, TemperatureUnit.CELSIUS),
            Temperature(1, TemperatureUnit.CELSIUS),
            False,
            True,
            True,
            False,
            False,
        ),
        (
            Temperature(1, TemperatureUnit.CELSIUS),
            Temperature(0, TemperatureUnit.CELSIUS),
            False,
            False,
            False,
            True,
            True,
        ),
    ],
)
def test_compare_temperatures(
    temperature1: Temperature,
    temperature2: Temperature,
    is_equal: bool,
    is_less_than: bool,
    is_less_than_or_equal_to: bool,
    is_greater_than: bool,
    is_greater_than_or_equal_to: bool,
) -> None:
    assert (temperature1 == temperature2) is is_equal
    assert (temperature1 < temperature2) is is_less_than
    assert (temperature1 <= temperature2) is is_less_than_or_equal_to
    assert (temperature1 > temperature2) is is_greater_than
    assert (temperature1 >= temperature2) is is_greater_than_or_equal_to
