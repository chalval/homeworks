# В ящике имеется 15 деталей, из которых 9 окрашены. Рабочий случайным образом
# извлекает 3 детали. Какова вероятность того, что все извлеченные детали окрашены?

from math import factorial


def combin(n, m):
    return factorial(n) // (factorial(m) * factorial(n - m))


n = combin(15, 3)
m = combin(9, 3) * combin(6, 0)
p = m / n
print(f'Вероятность того, что все извлеченные детали окрашены = {p}')
