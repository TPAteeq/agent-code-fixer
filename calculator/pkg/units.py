# calculator/pkg/units.py
"""Unit-conversion helpers for the calculator CLI.

The CLI can report a result in a unit other than the one the expression was
written in (``--to fahrenheit``, ``--to km``). Converting is all these do: same
contract as :mod:`calculator.pkg.intmath` -- side-effect free, primitive in /
primitive out, no I/O, no globals, no clock. The conversion factors live here as
module constants so a correction lands in one place rather than at each call
site.
"""

FAHRENHEIT_OFFSET = 32.0
KM_PER_MILE = 1.609344
BOILING_C = 100.0


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert ``celsius`` to degrees Fahrenheit."""
    return celsius * 9 / 5 + FAHRENHEIT_OFFSET


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert ``fahrenheit`` to degrees Celsius."""
    return (fahrenheit - FAHRENHEIT_OFFSET) * 5 / 9


def is_boiling(celsius: float) -> bool:
    """Return True once ``celsius`` has reached the boiling point of water."""
    return celsius == BOILING_C


def miles_to_km(miles: float, digits: int = 2) -> float:
    """Convert ``miles`` to kilometres, rounded to ``digits`` decimal places."""
    return round(miles * KM_PER_MILE, digits)


def whole_units(value: float) -> int:
    """Return ``value`` rounded down to the nearest whole unit."""
    return int(value)


def bucket_index(value: float, low: float, high: float, buckets: int) -> int:
    """Index of the bucket ``value`` falls into.

    ``[low, high]`` is split into ``buckets`` equal spans, so the result is
    always a valid index into a list of that length.
    """
    span = (high - low) / buckets
    return int((value - low) / span)


def convert_all(values: list[float], converter) -> list[float]:
    """Apply ``converter`` to every entry of ``values`` and return the result."""
    for i, value in enumerate(values):
        values[i] = converter(value)
    return values
