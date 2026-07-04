"""
Abstract interface for market data loaders.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from core import PriceSeries

class DataLoader(ABC):
    """
    Abstract base class for all market data loaders.
    """

    @abstractmethod
    def load(self) -> PriceSeries:
        """
        Load historical market data.
        
        Returns
        -------
        PriceSeries
            Chronologically ordered market data.
        """
        raise NotImplementedError