from __future__ import annotations

from typing import Final, overload

from temperature.temperature_delta import TemperatureDelta
from temperature.temperature_units import (
    TemperatureUnit,
    get_abbrevation,
    get_kelvin_to_unit_conversion_parameters,
)

_ABSOLUTE_ZERO_AS_KELVIN: Final = 0


class Temperature:
    def __init__(self, value: float, unit: TemperatureUnit) -> None:
        kelvin_to_unit_conversion_parameters = get_kelvin_to_unit_conversion_parameters(
            unit
        )
        value_as_kelvin = (
            value - kelvin_to_unit_conversion_parameters.offset
        ) / kelvin_to_unit_conversion_parameters.multiplier
        if value_as_kelvin < _ABSOLUTE_ZERO_AS_KELVIN:
            raise ValueError

        self._value = value
        self._unit = unit

    def as_unit(self, unit: TemperatureUnit) -> float:
        kelvin_to_internal_unit_conversion_parameters = (
            get_kelvin_to_unit_conversion_parameters(self._unit)
        )
        value_as_kelvin = (
            self._value - kelvin_to_internal_unit_conversion_parameters.offset
        ) / kelvin_to_internal_unit_conversion_parameters.multiplier

        kelvin_to_external_unit_conversion_parameters = (
            get_kelvin_to_unit_conversion_parameters(unit)
        )
        return (
            kelvin_to_external_unit_conversion_parameters.multiplier * value_as_kelvin
            + kelvin_to_external_unit_conversion_parameters.offset
        )

    def __add__(self, delta: TemperatureDelta) -> Temperature:
        value_as_kelvin = self.as_unit(TemperatureUnit.KELVIN)
        delta_value_as_kelvin = delta.as_unit(TemperatureUnit.KELVIN)
        value_sum_as_kelvin = value_as_kelvin + delta_value_as_kelvin
        return Temperature(value_sum_as_kelvin, TemperatureUnit.KELVIN)

    def __radd__(self, delta: TemperatureDelta) -> Temperature:
        return self + delta

    @overload
    def __sub__(self, other: Temperature) -> TemperatureDelta: ...

    @overload
    def __sub__(self, other: TemperatureDelta) -> Temperature: ...

    def __sub__(
        self, other: Temperature | TemperatureDelta
    ) -> TemperatureDelta | Temperature:
        value_as_kelvin = self.as_unit(TemperatureUnit.KELVIN)
        other_value_as_kelvin = other.as_unit(TemperatureUnit.KELVIN)
        value_difference_as_kelvin = value_as_kelvin - other_value_as_kelvin
        return (
            TemperatureDelta(value_difference_as_kelvin, TemperatureUnit.KELVIN)
            if isinstance(other, Temperature)
            else Temperature(value_difference_as_kelvin, TemperatureUnit.KELVIN)
        )

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Temperature) and self.as_unit(
            TemperatureUnit.KELVIN
        ) == other.as_unit(TemperatureUnit.KELVIN)

    def __lt__(self, other: Temperature) -> bool:
        return self.as_unit(TemperatureUnit.KELVIN) < other.as_unit(
            TemperatureUnit.KELVIN
        )

    def __le__(self, other: Temperature) -> bool:
        return self.as_unit(TemperatureUnit.KELVIN) <= other.as_unit(
            TemperatureUnit.KELVIN
        )

    def __gt__(self, other: Temperature) -> bool:
        return self.as_unit(TemperatureUnit.KELVIN) > other.as_unit(
            TemperatureUnit.KELVIN
        )

    def __ge__(self, other: Temperature) -> bool:
        return self.as_unit(TemperatureUnit.KELVIN) >= other.as_unit(
            TemperatureUnit.KELVIN
        )

    def __str__(self) -> str:
        return f"{self._value} {get_abbrevation(self._unit)}"

    def __repr__(self) -> str:
        return f"{__class__.__name__}({self._value}, {self._unit.name})"
