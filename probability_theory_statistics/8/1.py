# Даны значения величины заработной платы заемщиков банка (zp) и значения
# их поведенческого кредитного скоринга (ks):
# zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],
# ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].
# Найдите ковариацию этих двух величин с помощью элементарных действий,
# а затем с помощью функции cov из numpy. Полученные значения должны быть равны.
# Найдите коэффициент корреляции Пирсона с помощью ковариации и среднеквадратичных отклонений
# двух признаков, а затем с использованием функций из библиотек numpy и pandas.

import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
# from scipy import stats

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
cov = np.mean(zp * ks) - np.mean(zp) * np.mean(ks)
print(f'Ковариация этих двух величин с помощью элементарных действий = {cov}')
print(f'{np.cov(zp, ks, ddof=0)} tnp.cov(zp, ks, ddof=0)')
print(f'{np.corrcoef(zp, ks)} tnp.corrcoef(zp, ks)')
a = (np.cov(zp, ks, ddof=1)[0][1]) / (np.std(zp, ddof=1) * np.std(ks, ddof=1))
print(f'Коэффициент корреляции Пирсона = {a}')
pan = pd.Series(zp).corr(pd.Series(ks), method='pearson')
print(f'С помощью pandas корреляции Пирсона = {pan}')

# plt.scatter(zp, ks)
# plt.xlabel('zp')
# plt.ylabel('ks', rotation=90)
# plt.show()
