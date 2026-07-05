"""
Trading domain objects.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True, slots=True)
class Trade:
    """
    Represents a position change executed by the backtester.
    
    Parameters
    ----------
    timestamp
        Execution timestamp.
    
    price
        Execution price.
    
    previous_position
        Position before execution.
    
    new_position
        Position after execution.
    """

    timestamp: datetime
    price: float
    previous_position: float
    new_position: float

    @property
    def position_change(self) -> float:
        """Return the change in position."""
        return self.new_position - self.previous_position
    