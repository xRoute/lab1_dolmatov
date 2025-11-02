import numpy as np
import matplotlib.pyplot as plt

def analyze_time_series(data, p=3):
    data = np.array(data, dtype=float)
    mean = data.mean()
    var = data.var()
    std = data.std()
    max = []
    min = []
    n = len(data)
    for i in range(1, n - 1):
        if data[i] > data[i - 1] and data[i] > data[i + 1]:
            max.append(i)
        if data[i] < data[i - 1] and data[i] < data[i + 1]:
            min.append(i)
    if p > 1:
        cumsum = np.cumsum(np.insert(data, 0, 0))
        moving_avg = (cumsum[p:] - cumsum[:-p]) / p
    else:
        moving_avg = data.copy()

    return {
        "mean": mean,
        "variance": var,
        "std": std,
        "max_indices": max,
        "min_indices": min,
        "moving_average": moving_avg
    }
