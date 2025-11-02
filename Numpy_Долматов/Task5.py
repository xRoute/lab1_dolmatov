import numpy as np
import matplotlib.pyplot as plt

def chess(m, n, a, b):
    mat = np.zeros((m, n))
    for i in range(m):
        for j in range(n):
            if (i + j) % 2 == 0:
                mat[i, j] = a
            else:
                mat[i, j] = b
    return mat