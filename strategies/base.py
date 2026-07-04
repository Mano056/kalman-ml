"""
Strategy interface.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from core import PositionSeries, PriceSeries


class Strategy(ABC):
    """
    Base class for all research strategies.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """Human-readable strategy name."""
        raise NotImplementedError
    
    @abstractmethod
    def compute_positions(
        self, 
        price_series: PriceSeries,
    ) -> PositionSeries:
        """
        Compute the desired portfolio position for each bar.
        """
        raise NotImplementedError