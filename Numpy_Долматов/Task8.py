import numpy as np
import matplotlib.pyplot as plt

def one_hot_encode(labels):
    labels = np.array(labels)
    n_classes = labels.max() + 1
    one_hot = np.zeros((len(labels), n_classes))
    one_hot[np.arange(len(labels)), labels] = 1
    return one_hot
