import numpy as np
import matplotlib.pyplot as plt

def sum_prod(X, V):
    result = np.zeros_like(V[0])
    for x,v in zip(X,V):
        result+= (x @ v).astype(int)
    return result
