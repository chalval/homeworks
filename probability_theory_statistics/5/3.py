# Проведите тест гипотезы H0. Продавец утверждает, что средний вес пачки печенья
# составляет 200 г.
# Из партии извлечена выборка из 10 пачек. Вес каждой пачки составляет:
# 202, 203, 199, 197, 195, 201, 200, 204, 194, 190.
# Известно, что их веса распределены нормально.
# Верно ли утверждение продавца, если учитывать, что доверительная вероятность равна
# 99%? (Провести двусторонний тест.)

import numpy as np
from scipy import stats

m = 200
x = np.array([202, 203, 199, 197, 195, 201, 200, 204, 194, 190])
mv = np.mean(x)
sko = np.std(x, ddof=1)
n = len(x)
tt = stats.t.ppf(0.995, n - 1)
tn = (mv - m) / (sko / np.sqrt(n))
print(tt, tn)
if np.abs(tn) < tt:
    print('Подтверждаем гипотезу H0')
else:
    print('Подтверждаем гипотезу H1')
