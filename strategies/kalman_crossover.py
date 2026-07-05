"""
Kalman crossover strategy.
"""

from __future__ import annotations

from config import KalmanConfig
from core import PositionSeries, PriceSeries
from indicators import KalmanIndicator

from .base import Strategy


class KalmanCrossoverStrategy(Strategy):
    """
    Generate positions using two Kalman filters.
    
    A long position is held when the fast Kalman estimate is above the
    slow estimate. A short position is held when the fast estimate is 
    below the slow estimate.
    """

    def __init__(
            self,
            fast_config: KalmanConfig,
            slow_config: KalmanConfig,
    ) -> None:
        self._fast = KalmanIndicator(fast_config)
        self._slow = KalmanIndicator(slow_config)
    
    @property
    def name(self) -> str:
        return "Kalman Crossover"
    
    def compute_positions(
        self, 
        price_series: PriceSeries
    ) -> PositionSeries:
        fast = self._fast.compute(price_series).output("value")
        slow = self._slow.compute(price_series).output("value")

        positions: list[float] = []

        for fast_value, slow_value in zip(fast, slow):
            if fast_value > slow_value:
                positions.append(1.0)
            elif fast_value < slow_value:
                positions.append(-1.0)
            else:
                positions.append(0.0)
        
        return PositionSeries(positions)