# Даны значения зарплат из выборки выпускников:
# 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150.
# Посчитать (желательно без использования статистических методов наподобие std, var, mean)
# среднее арифметическое, среднее квадратичное отклонение, смещенную и несмещенную оценки
# дисперсий для данной выборки.

import numpy as np

x = np.array([100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150])
sum1 = 0
for i in range(len(x)):
    sum1 += x[i]
sa = sum1 / len(x)
dx = 0
for i in range(len(x)):
    dx += (x[i] - sa)**2
dxs = dx / len(x)
dxn = dx / (len(x) - 1)
sigs = np.sqrt(dxs)
sign = np.sqrt(dxn)
print(f'Среднее арифметическое выборки = {sa}')
print(f'Смещенная оценка дисперсии выборки = {dxs}')
print(f'Несмещенная оценка дисперсии выборки = {dxn}')
print(f'Смещенное среднее квадратичное отклонение выборки = {sigs}')
print(f'Несмещенное среднее квадратичное отклонение выборки = {sign}')
