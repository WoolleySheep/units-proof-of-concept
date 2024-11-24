from __future__ import annotations

from .temperature_units import (
    TemperatureUnit,
    get_abbreviation,
    get_kelvin_to_unit_conversion_parameters,
)


class TemperatureDelta:
    def __init__(self, value: float, unit: TemperatureUnit) -> None:
        self._value = value
        self._unit = unit

    def as_unit(self, unit: TemperatureUnit) -> float:
        internal_unit_conversion_parameters = get_kelvin_to_unit_conversion_parameters(
            self._unit
        )

        value_as_kelvin = (
            self._value
            / internal_unit_conversion_parameters.unit_delta_per_degree_kelvin
        )

        external_unit_conversion_parameters = get_kelvin_to_unit_conversion_parameters(
            unit
        )
        return (
            external_unit_conversion_parameters.unit_delta_per_degree_kelvin
            * value_as_kelvin
        )

    def __mul__(self, multiplier: float) -> TemperatureDelta:
        scaled_value = self._value * multiplier
        return TemperatureDelta(scaled_value, self._unit)

    def __rmul__(self, value: float) -> TemperatureDelta:
        return self * value

    def __truediv__(self, value: float) -> TemperatureDelta:
        scaled_value = self._value / value
        return TemperatureDelta(scaled_value, self._unit)

    def __add__(self, other: TemperatureDelta) -> TemperatureDelta:
        # This is here because the case of a TemperatureDelta + a Temperature is
        # handled in the __radd__ method in the Temperature class, otherwise it
        # runs into problems with circular imports
        if not isinstance(other, TemperatureDelta):  # type: ignore[reportUnnecessaryIsInstance]
            return NotImplemented

        value_as_kelvin = self.as_unit(TemperatureUnit.KELVIN)
        delta_value_as_kelvin = other.as_unit(TemperatureUnit.KELVIN)
        added_value_as_kelvin = value_as_kelvin + delta_value_as_kelvin
        return TemperatureDelta(added_value_as_kelvin, TemperatureUnit.KELVIN)

    def __sub__(self, delta: TemperatureDelta) -> TemperatureDelta:
        return self + (-delta)

    def __neg__(self) -> TemperatureDelta:
        inverted_value = -self._value
        return TemperatureDelta(inverted_value, self._unit)

    def __abs__(self) -> TemperatureDelta:
        absolute_value = abs(self._value)
        return TemperatureDelta(absolute_value, self._unit)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, TemperatureDelta) and self.as_unit(
            TemperatureUnit.KELVIN
        ) == other.as_unit(TemperatureUnit.KELVIN)

    def __lt__(self, other: TemperatureDelta) -> bool:
        return self.as_unit(TemperatureUnit.KELVIN) < other.as_unit(
            TemperatureUnit.KELVIN
        )

    def __le__(self, other: TemperatureDelta) -> bool:
        return self.as_unit(TemperatureUnit.KELVIN) <= other.as_unit(
            TemperatureUnit.KELVIN
        )

    def __gt__(self, other: TemperatureDelta) -> bool:
        return self.as_unit(TemperatureUnit.KELVIN) > other.as_unit(
            TemperatureUnit.KELVIN
        )

    def __ge__(self, other: TemperatureDelta) -> bool:
        return self.as_unit(TemperatureUnit.KELVIN) >= other.as_unit(
            TemperatureUnit.KELVIN
        )

    def __str__(self) -> str:
        return f"{self._value} {get_abbreviation(self._unit)}"

    def __repr__(self) -> str:
        return f"{__class__.__name__}({self._value}, {self._unit.name})"
