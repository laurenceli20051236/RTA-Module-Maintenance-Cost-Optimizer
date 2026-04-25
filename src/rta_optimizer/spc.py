import numpy as np


def control_limits(data):

    mean=np.mean(data)

    sigma=np.std(data)

    ucl=mean+3*sigma
    lcl=mean-3*sigma

    return mean,ucl,lcl


def detect_drift(
        data):

    mean,ucl,lcl=control_limits(data)

    violations=[]

    for x in data:
        if x>ucl or x<lcl:
            violations.append(x)

    return violations
