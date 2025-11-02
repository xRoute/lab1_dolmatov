import numpy as np
import matplotlib.pyplot as plt

def draw_rectangle(a, b, m, n, rectangle_color, background_color):
    img = np.ones((m, n, 3)) * np.array(background_color)
    center_row, center_col = m // 2, n // 2
    top = max(center_row - a // 2, 0)
    bottom = min(center_row + a // 2, m)
    left = max(center_col - b // 2, 0)
    right = min(center_col + b // 2, n)
    img[top:bottom, left:right] = rectangle_color
    return img

def draw_ellipse(a, b, m, n, ellipse_color, background_color):
    img = np.ones((m, n, 3)) * np.array(background_color)
    center_row, center_col = m // 2, n // 2
    Y, X = np.ogrid[:m, :n]
    range = ((Y - center_row) ** 2) / (a / 2) ** 2 + ((X - center_col) ** 2) / (b / 2) ** 2 <= 1
    img[range] = ellipse_color
    return img
