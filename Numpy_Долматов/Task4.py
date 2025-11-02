import numpy as np
import matplotlib.pyplot as plt


def analyze_random_matrix(m, n):
    M = np.random.normal(loc=0, scale=1, size=(m, n))
    mean_rows = M.mean(axis=1)
    var_rows = M.var(axis=1)
    mean_cols = M.mean(axis=0)
    var_cols = M.var(axis=0)

    for i, row in enumerate(M):
        plt.figure()
        plt.hist(row, bins=10)
        plt.xlabel("Значение")
        plt.ylabel("Частота")
        plt.show()

    for j in range(M.shape[1]):
        plt.figure()
        plt.hist(M[:, j], bins=10)
        plt.xlabel("Значение")
        plt.ylabel("Частота")
        plt.show()

    return {
        "matrix": M,
        "mean_rows": mean_rows,
        "var_rows": var_rows,
        "mean_cols": mean_cols,
        "var_cols": var_cols
    }

result = analyze_random_matrix(5, 4)