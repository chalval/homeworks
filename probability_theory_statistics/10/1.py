# Провести дисперсионный анализ для определения того, есть ли различия среднего роста
# среди взрослых футболистов, хоккеистов и штангистов.
# Даны значения роста в трех группах случайно выбранных спортсменов:
# Футболисты: 173, 175, 180, 178, 177, 185, 183, 182.
# Хоккеисты: 177, 179, 180, 188, 177, 172, 171, 184, 180.
# Штангисты: 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170.

import numpy as np
from scipy import stats

a = 0.05
y1 = np.array([173, 175, 180, 178, 177, 185, 183, 182])
y2 = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
y3 = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])

k = 3
n = len(y1) + len(y2) + len(y3)
y1_m = np.mean(y1)
y2_m = np.mean(y2)
y3_m = np.mean(y3)
total = np.concatenate([y1, y2, y3])
yt_m = np.mean(total)
s_f = np.sum((y1_m - yt_m)**2) * len(y1) + np.sum((y2_m - yt_m)**2) * len(y2) + np.sum((y3_m - yt_m)**2) * len(y3)
s_ost = np.sum((y1 - y1_m)**2) + np.sum((y2 - y2_m)**2) + np.sum((y3 - y3_m)**2)
d_f = s_f / (k - 1)
d_ost = s_ost / (n - k)
f_n = d_f / d_ost
print(f'Fн = {f_n}')

f = stats.f_oneway(y1, y2, y3)
print(f)
_, pv = f
if pv > a:
    print(f'Подтверждена  гипотеза H0, различий среднего роста нет')
else:
    print(f'Подтверждена  гипотеза H1, различия среднего роста есть')











