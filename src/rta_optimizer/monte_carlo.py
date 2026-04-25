# 模擬不確定性與 excursion risk

import numpy as np


def simulate_excursion_risk(
    monitor_interval_days: int,
    n_simulations: int = 10000,
    base_drift_rate: float = 0.02,
    drift_sigma: float = 0.01,
    excursion_threshold: float = 1.0,
    random_seed: int = 42,
) -> dict:
    """
    Monte Carlo simulation for estimating excursion probability
    as a function of monitor interval.
    """
    np.random.seed(random_seed)

    drift_accumulation = np.random.normal(
        loc=base_drift_rate * monitor_interval_days,
        scale=drift_sigma * np.sqrt(monitor_interval_days),
        size=n_simulations,
    )

    excursion_events = drift_accumulation > excursion_threshold
    excursion_probability = np.mean(excursion_events)

    return {
        "monitor_interval_days": monitor_interval_days,
        "n_simulations": n_simulations,
        "excursion_probability": excursion_probability,
        "expected_excursions": int(np.sum(excursion_events)),
    }


def run_interval_sweep(
    intervals=(3, 7, 14, 21, 30),
    n_simulations: int = 10000,
) -> list[dict]:
    """
    Compare excursion risk across different monitoring intervals.
    """
    return [
        simulate_excursion_risk(
            monitor_interval_days=interval,
            n_simulations=n_simulations,
        )
        for interval in intervals
    ]


if __name__ == "__main__":
    results = run_interval_sweep()
    for row in results:
        print(row)
