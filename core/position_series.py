"""
Position series domain model.
"""

from __future__ import annotations

from collections.abc import Iterator, Sequence


class PositionSeries(Sequence[float]):
    """
    Immutable desired portfolio positions.
    
    Each value represents the desired exposure after the 
    corresponding market bar.
    
    Examples
    --------
    -1.0 : fully short
    0.0  : flat
    0.5 : 50% long
    1.0 : fully long
    """

    def __init__(self, positions: list[float]) -> None:
        self._positions = tuple(float(x) for x in positions)

    def __len__(self) -> int:
        return len(self._positions)
    
    def __getitem__(self, index: int) -> float:
        return self._positions[index]
    
    def __iter__(self) -> Iterator[float]:
        return iter(self._positions)
    
    @property
    def values(self) -> list[float]:
        """Return the positions as a list."""
        return list(self._positions)