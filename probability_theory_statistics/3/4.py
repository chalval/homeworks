# В университет на факультеты A и B поступило равное количество студентов,
# а на факультет C студентов поступило столько же, сколько на A и B вместе.
# Вероятность того, что студент факультета A сдаст первую сессию, равна 0.8.
# Для студента факультета B эта вероятность равна 0.7, а для студента факультета C - 0.9.
# Студент сдал первую сессию. Какова вероятность, что он учится:
# a). на факультете A б). на факультете B в). на факультете C?


# p(a|b)=p(b|a)*p(a)/p(b)
# b - Студент сдал первую сессию
# a - Учится на факультете
pp = 0.8/4 + 0.7/4 + 0.9/2
pa = 0.8 * (1 / 4) / pp
pb = 0.7 * (1 / 4) / pp
pc = 0.9 * (1 / 2) / pp
print(f'Вероятность того, что учится на факультете A = {pa}')
print(f'Вероятность того, что учится на факультете B = {pb}')
print(f'Вероятность того, что учится на факультете C = {pc}')









