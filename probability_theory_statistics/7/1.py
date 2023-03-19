# Даны две независимые выборки. Не соблюдается условие нормальности
# x1 380,420, 290
# y1 140,360,200,900
# Сделайте вывод по результатам, полученным с помощью функции,
# имеются ли статистические различия между группами?

import numpy as np
from scipy import stats

a = 0.05
x1 = np.array([380, 420, 290])
y1 = np.array([140, 360, 200, 900])
_, pv = stats.mannwhitneyu(x1, y1)
print(stats.mannwhitneyu(x1, y1))
if pv > a:
    print('отвергаем гипотезу H1')
else:
    print('отвергаем гипотезу H0')
