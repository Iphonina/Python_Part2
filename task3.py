# 3. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint
LOWER_LIMIT = 0
UUPER_LIMIT = 1000
secret_num = randint(LOWER_LIMIT, UUPER_LIMIT)
attempt = 10
print("Отгадайте число от 0 до 1000. У вас 10 попыток.")

for _ in range(attempt):
    num = int(input("Введите число: "))
    if num < secret_num:
        print("Загаданное число больше")
    elif num > secret_num:
        print("Загаданное число меньше")
    else:
        print(f"Поздравляем! Вы угадали число {secret_num}")
        break
else:
    print(f"Вы проиграли. Загаданное число было {secret_num}")

