# Рост взрослого населения города X имеет нормальное распределение.
# Причем, средний рост равен 174 см, а среднее квадратичное отклонение равно 8 см.
# Какова вероятность того, что случайным образом выбранный взрослый человек имеет рост:
# а). больше 182 см
# б). больше 190 см
# в). от 166 см до 190 см
# г). от 166 см до 182 см
# д). от 158 см до 190 см
# е). не выше 150 см или не ниже 190 см
# ё). не выше 150 см или не ниже 198 см
# ж). ниже 166 см.

from scipy import stats

p1 = 1 - stats.norm.cdf(182, 174, 8)
p2 = 1 - stats.norm.cdf(190, 174, 8)
p3 = stats.norm.cdf(190, 174, 8) - stats.norm.cdf(166, 174, 8)
p4 = stats.norm.cdf(182, 174, 8) - stats.norm.cdf(166, 174, 8)
p5 = stats.norm.cdf(190, 174, 8) - stats.norm.cdf(158, 174, 8)
p6 = stats.norm.cdf(150, 174, 8) + 1 - stats.norm.cdf(190, 174, 8)
p7 = stats.norm.cdf(150, 174, 8) + 1 - stats.norm.cdf(198, 174, 8)
p8 = stats.norm.cdf(166, 174, 8)

print('а). больше 182 см = ', p1)
print('б). больше 190 см = ', p2)
print('в). от 166 см до 190 см = ', p3)
print('г). от 166 см до 182 см = ', p4)
print('д). от 158 см до 190 см = ', p5)
print('е). не выше 150 см или не ниже 190 см = ', p6)
print('ё). не выше 150 см или не ниже 198 см = ', p7)
print('ж). ниже 166 см. = ', p8)
