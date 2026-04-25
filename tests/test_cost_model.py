from src.rta_optimizer.cost_model import annual_savings_estimator


def test_annual_savings_estimator():
    result = annual_savings_estimator()
    assert result["annual_savings"] > 0
    assert result["percent_reduction"] > 0
