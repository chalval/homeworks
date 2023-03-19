# Посчитать коэффициент линейной регрессии при заработной плате (zp),
# используя градиентный спуск (без intercept).

import numpy as np


def mse(b1, y, x, n):
    return np.sum((b1 * x - y) ** 2) / n


a = 1e-6
x = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
y = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
n = len(x)
b1 = 0.1
for i in range(1501):
    b1 -= a * (2 / n) * np.sum((b1 * x - y) * x)
    if i % 100 == 0 or i == 10:
        print(f'i = {i}, b1 = {b1}, mse = {mse(b1, y, x, n)}')
