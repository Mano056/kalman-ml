"""
Result container returned by indicators.
"""

from __future__ import annotations

from dataclasses import dataclass

from core import PriceSeries

@dataclass(frozen=True, slots=True)
class IndicatorResult:
    """
    Represents the output of an indicator.
    
    Attributes
    ----------
    name
        Name of the indicator.
    
    values
        Numerical output of the indicator.
    
    price_series
        Original market data used to compute the indicator.
    """

    name: str
    values: list[float]
    price_series: PriceSeries

    def __post_init__(self) -> None:
        """
        Validate result consistency.
        """
        if len(self.values) != len(self.price_series):
            raise ValueError(
                "Indicator output length must match PriceSeries length."
            )
        