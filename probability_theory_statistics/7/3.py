# Сравните 1 и 2 е измерения, предполагая, что 3го измерения через 30 минут не было.
# Есть ли статистически значимые различия между измерениями давления?

import numpy as np
from scipy import stats

a = 0.05
x1 = np.array([150, 160, 165, 145, 155])
x2 = np.array([140, 155, 150, 130, 135])
_, pv = stats.wilcoxon(x1, x2)
print(stats.wilcoxon(x1, x2))
if pv > a:
    print('отвергаем гипотезу H1')
else:
    print('отвергаем гипотезу H0')







