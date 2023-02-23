# В лотерее 100 билетов. Из них 2 выигрышных. Какова вероятность того,
# что 2 приобретенных билета окажутся выигрышными?

from math import factorial


def combin(n, m):
    return factorial(n) // (factorial(m) * factorial(n - m))


n = combin(100, 2)
m = combin(2, 2) * combin(98, 0)   # =1
p = m / n
print(f'Вероятность того, что 2 приобретенных билета окажутся выигрышными = {p}')
