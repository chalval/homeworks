# На сколько сигм (средних квадратичных отклонений) отклоняется рост человека,
# равный 190 см, от математического ожидания роста в популяции,
# в которой M(X) = 178 см и D(X) = 25 кв.см?

x = 190
m = 178
d = 25
ns = (x - m) / (d ** 0.5)
print(f'Рост человека отклоняется на Z = {ns} сигм')


