"""
Indicator configuration objects.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class KalmanConfig:
    """
    Configuration for a Kalman filter indicator.
    
    Parameters
    ----------
    process_variance
        Process noise covariance (Q).
    
    measurement_variance
        Measurement noise covariance (R).
        
    initial_estimate_error
        Initial estimate covariance (P₀).
    """

    process_variance: float
    measurement_variance: float
    initial_estimate_error: float = 1.0

    def __post_init__(self) -> None:
        if self.process_variance <= 0:
            raise ValueError(
            "process_variance must be greater than zero."
        )

        if self.measurement_variance <= 0:
            raise ValueError(
                "measurement_variance must be greater than zero."
            )
        
        if self.initial_estimate_error <= 0:
            raise ValueError(
                "initial_estimate_error must be greater than zero."
            )
        