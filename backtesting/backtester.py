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

        current_position = 0.0

        entry_price: float | None = None

        trades: list[Trade] = []

        equity_curve: list[float] = []

        for bar, desired_position in zip(series, positions):
            
            if desired_position != current_position:

                if current_position != 0:

                    if current_position == 1:
                        equity *= bar.close / entry_price
                    
                    elif current_position == -1:
                        equity *= entry_price / bar.close
                
                if desired_position != 0:
                    entry_price = bar.close

                    trades.append(
                        Trade(
                            timestamp=bar.timestamp,
                            price=bar.close,
                            previous_position=current_position,
                            new_position=desired_position,
                        )
                    )

                current_position = desired_position
            equity_curve.append(equity)

        return BacktestResult(
            initial_cash=self.initial_cash,
            final_equity=equity,
            trades=trades,
            equity_curve=equity_curve,
        )