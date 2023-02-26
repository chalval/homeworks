# О случайной непрерывной равномерно распределенной величине B известно,
# что ее дисперсия равна 0.2.
# Можно ли найти правую границу величины B и ее среднее значение зная,
# что левая граница равна 0.5?  Если да, найдите ее.

d = 0.2
a = 0.5
b = a + (12 * d) ** 0.5
m = (a + b) / 2
print(f'Правая граница случайной непрерывной величины = {b}')
print(f'Среднее значение случайной непрерывной величины = {m}')




