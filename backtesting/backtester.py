from __future__ import annotations

from dataclasses import dataclass

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

        entry_price = None

        current_position = 0.0

        trades: list[Trade] = []

        for bar, desired_position in zip(series, positions):
            
            if desired_position != current_position:

                trades.append(
                    Trade(
                        timestamp=bar.timestamp,
                        price=bar.close,
                        previous_position=current_position,
                        new_position=desired_position,
                    )
                )
            
            if current_position == 0 and desired_position == 1:
                entry_price = bar.close

            if current_position == 1 and desired_position == 0:
                equity *= bar.close / entry_price

            current_position = desired_position

        
        return BacktestResult(
            initial_cash=self.initial_cash,
            final_equity=equity,
            trades=trades,
            equity_curve=[self.initial_cash] * len(series),
        )