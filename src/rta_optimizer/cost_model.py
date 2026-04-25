import numpy as np


def baseline_monitor_cost(
        wafers_per_year=52,
        wafer_cost=5000):
    """
    Traditional monitoring annual cost
    """
    return wafers_per_year * wafer_cost


def optimized_monitor_cost(
        wafers_per_year=13,
        wafer_cost=5000,
        haze_monitor_cost=10000):
    """
    Two-tier monitoring annual cost
    """
    return wafers_per_year*wafer_cost + haze_monitor_cost


def annual_savings_estimator():

    baseline = baseline_monitor_cost()

    optimized = optimized_monitor_cost()

    savings = baseline - optimized

    reduction = savings / baseline *100

    return {
        "baseline_cost":baseline,
        "optimized_cost":optimized,
        "annual_savings":savings,
        "percent_reduction":reduction
    }


if __name__=="__main__":
    print(annual_savings_estimator())
