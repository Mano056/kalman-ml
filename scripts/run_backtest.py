from pathlib import Path

from config import KalmanConfig
from data import CsvDataLoader
from strategies import KalmanCrossoverStrategy
from backtesting import Backtester


def main() -> None:
    path = Path("datasets/AUDUSDs.csv")

    loader = CsvDataLoader(path)

    series = loader.load()

    print(f"Loaded {len(series)} bars.")

    strategy = KalmanCrossoverStrategy(
        fast_config=KalmanConfig(
            process_variance=1e-3,
            measurement_variance=1e-2,
        ),
        slow_config=KalmanConfig(
            process_variance=1e-5,
            measurement_variance=1e-2
        ),
    )

    positions = strategy.compute_positions(series)

    print(f"Generated {len(positions)} positions.")
    
    backtester = Backtester()

    result = backtester.run(
        series,
        positions,
    )

    print()
    print("========== BACKTEST ==========")
    print(f"initial Equity : {result.initial_cash:.2f}")
    print(f"Final Equity   : {result.final_equity:.2f}")
    print(f"Trades         : {len(result.trades)}")

    print()
    print("First five trades:")

    for trade in result.trades[:5]:
        print(trade)

if __name__ == "__main__":
    main()