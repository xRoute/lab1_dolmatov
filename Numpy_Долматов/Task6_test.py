from Task6 import draw_rectangle, draw_ellipse
import numpy as np
import matplotlib.pyplot as plt

def test_draw_shapes():
    rect = draw_rectangle(10, 20, 50, 50, (255,0,0), (0,0,0))
    assert rect.shape == (50, 50, 3)
    assert (rect[25, 25] == np.array([255,0,0])).all()

    ell = draw_ellipse(20, 30, 50, 50, (0, 255, 0), (0, 0, 0))
    assert ell.shape == (50, 50, 3)
    assert (ell[25, 25] == np.array([0, 255, 0])).all()

test_draw_shapes()
print("тесты пройдены")