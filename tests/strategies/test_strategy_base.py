from datetime import datetime

from core import Bar, PositionSeries, PriceSeries
from strategies import Strategy


class DummyStrategy(Strategy):
    @property
    def name(self) -> str:
        return "Dummy"
    
    def compute_positions(
            self,
            price_series: PriceSeries,
    ) -> PositionSeries:
        return PositionSeries(
            [0.0] * len(price_series)
        )
    
    def test_strategy_interface() -> None:
        series = PriceSeries(
            [
                Bar(
                    timestamp=datetime(2024, 1, 1),
                    open=100,
                    high=101,
                    low=99,
                    close=100,
                    volume=1000,
                )
            ]
        )

        strategy = DummyStrategy()

        positions = strategy.compute_positions(series)

        assert positions.values == [0.0]