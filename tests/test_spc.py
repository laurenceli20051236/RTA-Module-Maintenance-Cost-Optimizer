from src.rta_optimizer.spc import detect_drift


def test_detect_drift_returns_list():
    data = [1, 1, 1, 1, 10]
    result = detect_drift(data)
    assert isinstance(result, list)
