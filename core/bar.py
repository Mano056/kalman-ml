"""
Domain models representing market data.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True, slots=True)
class Bar:
    """
    Represents a single OHLCV market data bar.
    
    Attributes
    ----------
    timestamp
        Timestamp of the bar.
    open
        Opening price.
    high
        Highest traded price.
    low
        Lowest traded price.
    close
        Closing price.
    volume
        Traded volume.
    """

    timestamp: datetime
    open: float
    high: float
    low: float
    close: float
    volume: float

    def __post_init__(self) -> None:
        """
        Validate that the bar satisfies basic market data constraints.
        """
        if self.high < self.low:
            raise ValueError("high must be greater than or equal to low")
        
        if self.high < self.open:
            raise ValueError("high cannot be lower than open")
        
        if self.high < self.close:
            raise ValueError("high cannot be lower than close")
        
        if self.low > self.open:
            raise ValueError("low cannot be greater than open")
        
        if self.low > self.close:
            raise ValueError("low cannot be greater than close")
        
        if self.volume < 0:
            raise ValueError("volume cannot be negative")
        