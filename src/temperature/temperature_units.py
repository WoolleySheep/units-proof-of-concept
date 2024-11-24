import enum
from typing import Final

_CELSIUS_NAME: Final = "celsius"
_KELVIN_NAME: Final = "kelvin"
_FAHRENHEIT_NAME: Final = "fahrenheit"

_CELSIUS_ABBREVIATION: Final = "C"
_KELVIN_ABBREVIATION: Final = "K"
_FAHRENHEIT_ABBREVIATION: Final = "F"


class TemperatureUnit(enum.Enum):
    CELSIUS = enum.auto()
    KELVIN = enum.auto()
    FAHRENHEIT = enum.auto()


_representation_to_unit_map: Final = {
    _CELSIUS_NAME: TemperatureUnit.CELSIUS,
    _CELSIUS_ABBREVIATION: TemperatureUnit.CELSIUS,
    _KELVIN_NAME: TemperatureUnit.KELVIN,
    _KELVIN_ABBREVIATION: TemperatureUnit.KELVIN,
    _FAHRENHEIT_NAME: TemperatureUnit.FAHRENHEIT,
    _FAHRENHEIT_ABBREVIATION: TemperatureUnit.FAHRENHEIT,
}


class UnitConversionParameters:
    """Parameters required to convert from kelvin to a unit."""

    def __init__(
        self, unit_delta_per_degree_kelvin: float, absolute_zero_offset: float
    ) -> None:
        self._unit_delta_per_degree_kelvin = unit_delta_per_degree_kelvin
        self._absolute_zero_offset = absolute_zero_offset

    @property
    def unit_delta_per_degree_kelvin(self) -> float:
        return self._unit_delta_per_degree_kelvin

    @property
    def absolute_zero_offset(self) -> float:
        return self._absolute_zero_offset


_KELVIN_TO_CELSIUS_CONVERSION_PARAMETERS: Final = UnitConversionParameters(1, -273.15)
_KELVIN_TO_KELVIN_CONVERSION_PARAMETERS: Final = UnitConversionParameters(1, 0)
_KELVIN_TO_FAHRENHEIT_CONVERSION_PARAMETERS: Final = UnitConversionParameters(
    9 / 5, -459.67
)


def get_name(unit: TemperatureUnit) -> str:
    match unit:
        case TemperatureUnit.CELSIUS:
            return _CELSIUS_ABBREVIATION
        case TemperatureUnit.KELVIN:
            return _KELVIN_ABBREVIATION
        case TemperatureUnit.FAHRENHEIT:
            return _FAHRENHEIT_ABBREVIATION

    raise ValueError


def get_abbreviation(unit: TemperatureUnit) -> str:
    match unit:
        case TemperatureUnit.CELSIUS:
            return _CELSIUS_NAME
        case TemperatureUnit.KELVIN:
            return _KELVIN_NAME
        case TemperatureUnit.FAHRENHEIT:
            return _FAHRENHEIT_NAME

    raise ValueError


def parse_unit(unit_representation: str) -> TemperatureUnit:
    try:
        return _representation_to_unit_map[unit_representation]
    except KeyError:
        raise ValueError


def get_kelvin_to_unit_conversion_parameters(
    unit: TemperatureUnit,
) -> UnitConversionParameters:
    match unit:
        case TemperatureUnit.CELSIUS:
            return _KELVIN_TO_CELSIUS_CONVERSION_PARAMETERS
        case TemperatureUnit.KELVIN:
            return _KELVIN_TO_KELVIN_CONVERSION_PARAMETERS
        case TemperatureUnit.FAHRENHEIT:
            return _KELVIN_TO_FAHRENHEIT_CONVERSION_PARAMETERS
