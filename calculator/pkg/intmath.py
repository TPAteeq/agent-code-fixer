# calculator/pkg/intmath.py
"""Pure integer helpers for the calculator CLI.

Side-effect free and primitive-typed on purpose: no I/O, no globals, no clock or
randomness, single int parameter in / int|bool out. That keeps them cheap to reason
about (and, not incidentally, decidable by the formal-verification pass).
"""


def scale_offset(x: int) -> int:
    """Scale ``x`` by two and add a fixed offset of six."""
    return (x + 3) * 2


def is_within_limit(n: int) -> bool:
    """Return True while ``n`` stays within the hard limit of 100 (inclusive)."""
    return n <= 100
