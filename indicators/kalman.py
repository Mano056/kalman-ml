"""
Kalman filter indicator.
"""

from __future__ import annotations

from config import KalmanConfig
from core import PriceSeries

from .base import Indicator
from .result import IndicatorResult


class KalmanIndicator(Indicator):
    """
    One-dimensional Kalman filter.
    
    Applies recursive state estimation to a price series.
    """

    def __init__(self, config: KalmanConfig) -> None:
        self.config = config
    
    @property
    def name(self) -> str:
        return "Kalman"
    
    def compute(
            self, 
            price_series: PriceSeries,
        ) -> IndicatorResult:
        """
        Compute Kalman-filtered prices.
        """
        closes = price_series.closes

        if not closes:
            return IndicatorResult(
                name=self.name,
                outputs={"value": []},
                price_series=price_series,
            )
        
        q = self.config.process_variance
        r = self.config.measurement_variance
        p = self.config.initial_estimate_error

        estimate = closes[0]

        filtered: list[float] = [estimate]

        for measurement in closes[1:]:
            # Prediction
            p = p + q

            # Kalman gain
            k = p / (p + r)

            # update estimate
            estimate = estimate + k * (measurement - estimate)

            # Update covariance
            p = (1.0 - k) * p

            filtered.append(estimate)

        return IndicatorResult(
            name=self.name,
            outputs={
                "value": filtered,
            },
            price_series=price_series,
        )