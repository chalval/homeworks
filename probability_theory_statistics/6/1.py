# Известно, что генеральная совокупность распределена нормально
# со средним квадратическим отклонением, равным 16.
# Найти доверительный интервал для оценки математического ожидания с надежностью
# 0.95, если выборочная средняя M = 80, а объем выборки n = 256.

import numpy as np
from scipy import stats

a = 0.05
m = 80
sko = 16
n = 256
z = stats.norm.ppf(1 - a / 2)
d = z * sko / np.sqrt(n)
print(f'Доверительный интервал [{m - d} ; {m + d}]')

