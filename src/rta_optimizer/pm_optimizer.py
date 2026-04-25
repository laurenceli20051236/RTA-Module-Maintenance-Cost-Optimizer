# 找最佳 PM/ Monitor interval

from .monte_carlo import simulate_excursion_risk


def total_expected_cost(
    monitor_interval_days: int,
    wafer_cost: float = 5000,
    annual_days: int = 365,
    excursion_cost: float = 250000,
) -> dict:
    """
    Estimate annual expected cost for a given monitor interval.
    """
    monitors_per_year = annual_days / monitor_interval_days
    annual_monitor_cost = monitors_per_year * wafer_cost

    risk_result = simulate_excursion_risk(
        monitor_interval_days=monitor_interval_days
    )

    expected_excursion_cost = (
        risk_result["excursion_probability"] * excursion_cost
    )

    total_cost = annual_monitor_cost + expected_excursion_cost

    return {
        "monitor_interval_days": monitor_interval_days,
        "monitors_per_year": monitors_per_year,
        "annual_monitor_cost": annual_monitor_cost,
        "excursion_probability": risk_result["excursion_probability"],
        "expected_excursion_cost": expected_excursion_cost,
        "total_expected_cost": total_cost,
    }


def find_optimal_interval(
    candidate_intervals=(3, 7, 14, 21, 30),
) -> dict:
    """
    Find monitor interval with lowest total expected cost.
    """
    results = [
        total_expected_cost(interval)
        for interval in candidate_intervals
    ]

    best = min(results, key=lambda x: x["total_expected_cost"])

    return {
        "best_interval_days": best["monitor_interval_days"],
        "best_total_expected_cost": best["total_expected_cost"],
        "all_results": results,
    }


if __name__ == "__main__":
    print(find_optimal_interval())
