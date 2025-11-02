def mse(pred, true):
    n = len(pred)
    sum = 0
    for i in range(n):
        sum += (pred[i] - true[i]) ** 2
    return sum / n