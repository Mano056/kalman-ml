"""
Collection of computed indicator results.
"""

from __future__ import annotations

from collections.abc import Iterator

from .result import IndicatorResult


class IndicatorSet:
    """
    Immutable collection of indicator results.
    
    Indicators are stored by name.
    """

    def __init__(
            self, 
            indicators: list[IndicatorResult],
    ) -> None:
        self._indicators = {
            indicator.name: indicator 
            for indicator in indicators
        }

        if len(self._indicators) != len(indicators):
            raise ValueError(
                "Duplicate indicator names are not allowed."
            )
        
    def __contains__(self, name: str) -> bool:
        return name in self._indicators
    
    def __len__(self) -> int:
        return len(self._indicators)
    
    def __iter__(self) -> Iterator[IndicatorResult]:
        return iter(self._indicators.values())
    
    def get(self, name: str) -> IndicatorResult:
        """
        Return an indicator by name.
        """
        return self._indicators[name]
    
    @property
    def names(self) -> list[str]:
        """
        Return indicator names.
        """
        return sorted(self._indicators.keys())