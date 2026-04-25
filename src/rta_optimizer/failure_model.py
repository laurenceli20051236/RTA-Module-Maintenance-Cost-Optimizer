import numpy as np


def excursion_risk_score(
        haze_signal,
        threshold=1.2):

    if haze_signal < threshold:
        return "Low"

    elif haze_signal <1.5:
        return "Medium"

    else:
        return "High"


def failure_probability(
        haze_signal):

    return min(
        0.05*haze_signal,
        1.0
    )
