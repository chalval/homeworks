# Даны значения величины заработной платы заемщиков банка (zp) и
# значения их поведенческого кредитного скоринга (ks):
# zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],
# ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].
# Используя математические операции, посчитать коэффициенты линейной регрессии,
# приняв за X заработную плату (то есть, zp - признак), а за y - значения скорингового балла
# (то есть, ks - целевая переменная). Произвести расчет как с использованием intercept, так и без.

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

x = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
y = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
n = len(x)
b1 = (np.mean(x * y) - np.mean(x) * np.mean(y)) / (np.mean(x**2) - np.mean(x)**2)
print(f'b1 = {b1}')
b0 = np.mean(y) - b1 * np.mean(x)
print(f'b0 = {b0}')

x = x.reshape(n, 1)
y = y.reshape(n, 1)
b = np.dot(np.linalg.inv(np.dot(x.T, x)), x.T @ y)
xx = np.hstack([np.ones((n, 1)), x])
bb = np.dot(np.linalg.inv(np.dot(xx.T, xx)), xx.T @ y)
print(f'-----------------\nМатричный метод с b0:\n{bb}')
print(f'-----------------\nМатричный метод без b0:\nb1 = {b[0][0]}')
print('-----------------\nЭкземпляр класса LinearRegression:')
model = LinearRegression()
model.fit(x, y)
print(f'b0 = {model.intercept_[0]}, b1 = {model.coef_[0][0]}')

plt.plot(x, x * model.coef_[0] + model.intercept_, color='green')
plt.plot(x, x * b[0][0], color='red')
plt.scatter(x, y)
plt.xlabel('Заработная плата')
plt.ylabel('Значения скорингового балла', rotation=90)
plt.show()

