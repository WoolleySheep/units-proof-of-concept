import contextlib

from src.temperature import (
    Temperature,
    TemperatureDelta,
    TemperatureUnit,
    get_unit_abbreviation,
    get_unit_name,
    parse_unit,
)

# Temperature and TemperatureDelta are designed to act as record types -
# immutable once created. Aiming to mirror the mimic of datetime.time and
# datetime.timedelta (with a lot less functionality).

# Create unit-agnostic temperature
temp = Temperature(100, TemperatureUnit.CELSIUS)

# Cannot create invalid temperature
with contextlib.suppress(ValueError):
    Temperature(-400, TemperatureUnit.CELSIUS)  # Less than absolute zero

# Create unit-agnostic temperature difference
dtemp = TemperatureDelta(50, TemperatureUnit.KELVIN)

# Add Temperature and TemperatureDelta to return a new Temperature
temp2 = temp + dtemp
temp2 = dtemp + temp

# Subtract TemperatureDelta from Temperature to return a new Temperature
temp2 = temp - dtemp

# Subtract Temperature from Temperature to return a new TemperatureDelta
dtemp2 = temp - temp

# Add, scale & invert TemperatureDelta to return a new TemperatureDelta
dtemp2 = dtemp + dtemp
dtemp2 = dtemp - dtemp
dtemp2 = 2 * dtemp
dtemp2 = dtemp * 2
dtemp2 = dtemp / 2
dtemp2 = -dtemp

# Divide TemperatureDelta by a TemperatureDelta to return the ratio
ratio = dtemp / dtemp

# Can perform comparisons between Temperature
result = temp == temp
result = temp < temp
result = temp <= temp
result = temp > temp
result = temp >= temp

# Can perform comparisons between TemperatureDelta
result = dtemp == dtemp
result = dtemp < dtemp
result = dtemp <= dtemp
result = dtemp > dtemp
result = dtemp >= dtemp

# when you need the raw value, get the value by unit
temp_as_fahrenheit = temp.as_unit(TemperatureUnit.FAHRENHEIT)
dtemp_as_celsius = dtemp.as_unit(TemperatureUnit.CELSIUS)

# Convert to string for debugging
temp_as_string = str(temp)  # "100 C"
dtemp_as_string = str(dtemp)  # "50 K"

# Get the unit name or abbreviation
unit_abbreviation = get_unit_abbreviation(TemperatureUnit.CELSIUS)  # "C"
unit_name = get_unit_name(TemperatureUnit.FAHRENHEIT)  # "fahrenheit"

# Parse a unit representation
unit = parse_unit("celsius")  # TemperatureUnit.CELSIUS
unit = parse_unit("K")  # TemperatureUnit.KELVIN
