"""
Bas interface for technical indicators.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from core import PriceSeries

from .result import IndicatorResult

class Indicator(ABC):
    """
    Base class for all indicators.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """Human-readable indicator name."""
        raise NotImplementedError
    
    @abstractmethod
    def compute(
        self,
        price_series: PriceSeries,   
    ) -> IndicatorResult:
        """
        Compute the indicator.
        
        Parameters
        ----------
        price_series
            Historical market data.
            
        Returns
        -------
        IndicatorResult
            Indicator values.
        """
        raise NotImplementedError