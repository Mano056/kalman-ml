from pathlib import Path

from config import KalmanConfig
from data import CsvDataLoader
from strategies import KalmanCrossoverStrategy
from backtesting import Backtester
from indicators import KalmanIndicator
from plotting import plot_backtest
import matplotlib.pyplot as plt


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

    fast = KalmanIndicator(
        KalmanConfig(
            process_variance=1e-3,
            measurement_variance=1e-2,
        )
    )

    slow = KalmanIndicator(
        KalmanConfig(
            process_variance=1e-5,
            measurement_variance=1e-2,
        )
    )

    fast_result = fast.compute(series)
    slow_result = slow.compute(series)

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

    fig = plot_backtest(
        series=series,
        positions=positions,
        result=result,
        indicators=[fast_result, slow_result],
    )

    plt.show()

if __name__ == "__main__":
    main()