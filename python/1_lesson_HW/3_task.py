# ------------------------------------------- 3 -----------------------------
# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
MAX_ATTEMPTS = 10
one = 1
guess = 0

num = randint(LOWER_LIMIT, UPPER_LIMIT)

print("Угадайте число от 0 до 1000. У вас 10 попыток.")

for attempt in range(MAX_ATTEMPTS):
    guess = int(input(f"Попытка №{attempt + one}: "))

    if guess < num:
        print("Загаданное число больше.")
    elif guess > num:
        print("Загаданное число меньше.")
    else:
        print("Поздравляю! Вы угадали число!")
        break

if guess != num:
    print("Вы исчерпали все попытки. Загаданное число было:", num)
