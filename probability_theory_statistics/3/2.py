# В первом ящике находится 8 мячей, из которых 5 - белые.
# Во втором ящике - 12 мячей, из которых 5 белых.
# Из первого ящика вытаскивают случайным образом два мяча,
# из второго - 4. Какова вероятность того, что 3 мяча белые?

from math import factorial


def combin(n, m):
    return factorial(n) // (factorial(m) * factorial(n - m))


p21 = (combin(5, 2) * combin(3, 0) / combin(8, 2)) * (combin(5, 1) * combin(7, 3) / combin(12, 4))
p12 = (combin(5, 1) * combin(3, 1) / combin(8, 2)) * (combin(5, 2) * combin(7, 2) / combin(12, 4))
p03 = (combin(5, 0) * combin(3, 2) / combin(8, 2)) * (combin(5, 3) * combin(7, 1) / combin(12, 4))
p = p21 + p12 + p03
print(f'Вероятность того, что 3 мяча белые = {p}')


