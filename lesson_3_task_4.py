# Напишите программу, которая будет преобразовывать
# десятичное число в двоичное.
#
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def int_to_bin(num:int):
    if num == 0:
        return str(0)
    elif num == 1:
        return str(1)
    else:
        return str(f'{int_to_bin(int(num / 2))}{num % 2}')

num = int(input('Введите десятичное число: '))
print(int_to_bin(num))