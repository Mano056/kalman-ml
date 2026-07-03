"""
Container for historical market data.
"""

from __future__ import annotations

from collections.abc import Iterator, Sequence
from datetime import datetime

from .bar import Bar

class PriceSeries(Sequence[Bar]):
    """
    Immutable container for a sequence of market bars.
    
    This class is the standard input to indicators, strategies, and 
    backtesting components.
    """

    def __init__(self, bars: list[Bar]) -> None:
        """
        Initialize a price series.
        
        Parameters
        ----------
        bars
            Bars ordered chronologically.
        
        Raises
        ------
        ValueError
            If timestamps are not strictly increasing.
        """

        self._bars: tuple[Bar, ...] = tuple(bars)

        for previous, current in zip(self._bars, self._bars[1:]):
            if current.timestamp <= previous.timestamp:
                raise ValueError(
                    "Bars must be ordered by strictly increasing timestamps."
                )
    
    def __getitem__(self, index: int) -> Bar:
        return self._bars[index]
    
    def __len__(self) -> int:
        return len(self._bars)
    
    def __iter__(self) -> Iterator[Bar]:
        return iter(self._bars)
    
    @property
    def timestamps(self) -> list[datetime]:
        """Return all timestamps."""
        return [bar.timestamp for bar in self._bars]
    
    @property
    def opens(self) -> list[float]:
        """Return opening prices."""
        return [bar.open for bar in self._bars]
    
    @property
    def highs(self) -> list[float]:
        """Return high prices."""
        return [bar.high for bar in self._bars]
    
    @property
    def lows(self) -> list[float]:
        """Return low prices."""
        return [bar.low for bar in self._bars]
    
    @property
    def closes(self) -> list[float]:
        """Return closing prices."""
        return [bar.close for bar in self._bars]
    
    @property
    def volumes(self) -> list[float]:
        """Return traded volumes."""
        return [bar.volume for bar in self._bars]