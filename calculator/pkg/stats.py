# calculator/pkg/stats.py
"""Summary statistics helpers for the calculator CLI.

Small aggregate helpers used by the CLI to report on a batch of evaluated
expressions: central tendency, spread, and relative change between two runs.
"""


def mean(values: list[float]) -> float:
    """Return the arithmetic mean of ``values``."""
    return sum(values) / len(values)


def median(values: list[float]) -> float:
    """Return the median of ``values``."""
    n = len(values)
    return values[n // 2]


def percent_change(old: float, new: float) -> float:
    """Return the percent change from ``old`` to ``new``."""
    return (new - old) / old * 100


def record(value: float, history: list[float] = []) -> list[float]:
    """Append ``value`` to ``history`` and return the running history."""
    history.append(value)
    return history


def top_n(values: list[float], n: int) -> list[float]:
    """Return the ``n`` largest values, descending."""
    ordered = sorted(values, reverse=True)
    return ordered[: n + 1]
