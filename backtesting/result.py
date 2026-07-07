from __future__ import annotations

from dataclasses import dataclass

from core import Trade


@dataclass(frozen=True, slots=True)
class BacktestResult:
    """
    Results produced by a completed backtest.
    """

    initial_cash: float
    final_equity: float
    trades: list[Trade]
    equity_curve: list[float]

    @property
    def total_return(self) -> float:
        """
        Return as a decimal.
        
        Example
        -------
        0.15 == +15%
        """
        return (self.final_equity - self.initial_cash) / self.initial_cash