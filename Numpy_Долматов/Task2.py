import numpy as np
import matplotlib.pyplot as plt

def binarize(M, threshold=0.5):
    return (M > threshold).astype(int)

