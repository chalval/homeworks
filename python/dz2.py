# ----------------------------------------------------------------------------------------
# Task 1
# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третьей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

bank = 0
op = 0
while True:
    print('Выберите операцию: 1-пополнить, 2-снять, 3-выход')
    num = ''
    while not num.isdigit() or int(num) < 1 or int(num) > 3:
        num = input()
    num = int(num)
    if num == 3: break
    if bank > 5_000_000: bank *= 0.9
    if num == 1:
        op += 1
        print('Введите сумму пополнения, кратную 50: ')
        sum1 = ''
        while not sum1.isdigit() or int(sum1) < 50 or int(sum1) % 50 != 0:
            sum1 = input()
        sum1 = int(sum1)
        bank += sum1
    if num == 2:
        op += 1
        print('Введите сумму снятия, кратную 50: ')
        sum2 = ''
        while not sum2.isdigit() or int(sum2) < 50 or int(sum2) % 50 != 0:
            sum2 = input()
        sum2 = int(sum2)
        sum3 = 0.015 * sum2
        if sum3 < 30: sum3 = 30
        if sum3 > 600: sum3 = 600
        if (bank - sum2 - sum3) < 0:
            print('На счете не хвататает средств. Сумма на вашем счете: ', round(bank, 2))
            op -= 1
            continue
        bank = bank - sum2 - sum3
    if op % 3 == 0:
        bank *= 1.03
    print(f'Сумма на вашем счете: {round(bank, 2)}  операция №{op}')


# ----------------------------------------------------------------------------------------
# Task 2
# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

def hex1(a):
    if a == 10: return 'a'
    if a == 11: return 'b'
    if a == 12: return 'c'
    if a == 13: return 'd'
    if a == 14: return 'e'
    if a == 15: return 'f'
    return  str(a)

sign1 = ''
num = input('Введите целое число: ')
num = int(num)
s = ''
a = 16
num1 = num
if num1 < 0:
    sign1 = '-'
    num1 *= -1
while a > 15:
    a, b = divmod(num1, 16)
    b = hex1(b)
    s = s + b
    num1 = a
a = hex1(a)
if a != '0': s = s + a
s = s[::-1]
s = sign1 + '0x' + s
print(s)
print(hex(num))


# ----------------------------------------------------------------------------------------
# Task 3
# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

import math, fractions

s1 = input('Введите первую строку вида “a/b”: ')
ind = s1.find('/')
if ind != -1:
    a1 = int(s1[:ind])
    b1 = int(s1[ind+1:])
else:
    a1 = int(s1)
    b1 = 1
s2 = input('Введите вторую строку вида “a/b”: ')
ind = s2.find('/')
if ind != -1:
    a2 = int(s2[:ind])
    b2 = int(s2[ind+1:])
else:
    a2 = int(s2)
    b2 = 1
sum_a = a1 * b2 + a2 * b1
sum_b = b1 * b2
nod_sum = math.gcd(sum_a, sum_b)
sum_a //= nod_sum
sum_b //= nod_sum
if sum_b < 0:
    sum_a *= -1
    sum_b *= -1
if sum_b != 1:
    print(f'Сумма дробей: {sum_a}/{sum_b}')
else: print(f'Сумма дробей: {sum_a}')
mlt_a = a1 * a2
mlt_b = b1 * b2
nod_mlt = math.gcd(mlt_a, mlt_b)
mlt_a //= nod_mlt
mlt_b //= nod_mlt
if mlt_b < 0:
    mlt_a *= -1
    mlt_b *= -1
if mlt_b != 1:
    print(f'Произведение дробей: {mlt_a}/{mlt_b}')
else: print(f'Произведение дробей: {mlt_a}')

f1 = fractions.Fraction(a1, b1)
f2 = fractions.Fraction(a2, b2)
print(f'Сумма дробей, используя модуль fractions: {f1 + f2}')
print(f'Произведение дробей, используя модуль fractions: {f1 * f2}')

