# 看哪些假設最影響 Cost Savings

import pandas as pd

from .pm_optimizer import total_expected_cost


def sensitivity_sweep(
    monitor_intervals=(3, 7, 14, 21, 30),
    wafer_costs=(3000, 5000, 7000),
    excursion_costs=(100000, 250000, 500000),
) -> pd.DataFrame:
    """
    Run sensitivity analysis across monitor interval,
    wafer cost, and excursion cost.
    """
    rows = []

    for interval in monitor_intervals:
        for wafer_cost in wafer_costs:
            for excursion_cost in excursion_costs:
                result = total_expected_cost(
                    monitor_interval_days=interval,
                    wafer_cost=wafer_cost,
                    excursion_cost=excursion_cost,
                )

                rows.append(result)

    return pd.DataFrame(rows)


def summarize_best_by_excursion_cost(df: pd.DataFrame) -> pd.DataFrame:
    """
    Summarize best monitor interval under each excursion-cost scenario.
    """
    idx = df.groupby("expected_excursion_cost")["total_expected_cost"].idxmin()
    return df.loc[idx].reset_index(drop=True)


if __name__ == "__main__":
    df = sensitivity_sweep()
    print(df)
