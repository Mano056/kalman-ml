"""
Trading domain objects.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class Trade:
    """
    Represents a position change executed by the backtester.
    
    Parameters
    ----------
    entry_time
        Entry timestamp.
    
    exit_time
        Exit timetamp.
    
    direction
        Position of entry.
    
    entry_price
        Trade execution price.
    
    exit_price
        Trade exit price.

    return_pct
        Trade return percentage.
    """

    entry_time: datetime
    exit_time: datetime

    direction: float

    entry_price: float
    exit_price: float

    return_pct: float

    
    