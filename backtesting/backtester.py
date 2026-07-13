from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from core import PositionSeries, PriceSeries, Trade

from .result import BacktestResult


@dataclass(slots=True)
class Backtester:
    initial_cash: float = 10_000

    def run(
            self,
            series: PriceSeries,
            positions: PositionSeries,
    ) -> BacktestResult:
        
        equity = self.initial_cash

        entry_time: datetime | None = None

        current_position = 0.0

        entry_price: float | None = None

        trades: list[Trade] = []

        equity_curve: list[float] = []

        for bar, desired_position in zip(series, positions):
            
            if desired_position != current_position:

                if current_position != 0:

                    exit_price = bar.close
                    exit_time = bar.timestamp

                    if current_position == 1:
                        equity *= exit_price / entry_price
                        return_pct = exit_price / entry_price - 1
                    
                    elif current_position == -1:
                        equity *= entry_price / exit_price
                        return_pct = entry_price / exit_price - 1
                    
                    trades.append(
                        Trade(
                            entry_time=entry_time,
                            exit_time=exit_time,
                            direction=current_position,
                            entry_price=entry_price,
                            exit_price=exit_price,
                            return_pct=return_pct,
                        )
                    )

                if desired_position != 0:
                    entry_price = bar.close
                    entry_time = bar.timestamp

                current_position = desired_position
            
            if current_position == 1:
                current_equity = equity * (bar.close / entry_price)
            
            elif current_position == -1:
                current_equity = equity * (entry_price / bar.close)
            
            else:
                current_equity = equity

            equity_curve.append(current_equity)
            

        return BacktestResult(
            initial_cash=self.initial_cash,
            final_equity=equity,
            trades=trades,
            equity_curve=equity_curve,
        )