"""
Portfolio state.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Portfolio:
    """
    Current portfolio state.
    
    This class intentionally contains very little logic.
    The Backtester owns the simulation.
    """

    cash: float
    equity: float
    position: float = 0.0

    def update_equity(
            self,
            market_price: float,
            entry_price: float,
    ) -> None:
        """
        Update current equity using unrealised PnL.
        
        Parameters
        ----------
        market_price
            Current market price.
        
        entry_price
            Average entry price.
        """
        pnl = (market_price - entry_price) * self.position
        self.equity = self.cash + pnl