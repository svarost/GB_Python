# Задайте число. Составьте список чисел Фибоначчи, в том числе
# для отрицательных индексов.
#
# Пример:
# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fib_positive(count:int):
    if count == 0:
        return 0
    elif count == 1:
        return 1
    else:
        return fib_positive(count - 1) + fib_positive(count - 2)

def fib_negative(count:int):
    if count == -1:
        return 1
    elif count == -2:
        return -1
    else:
        return fib_negative(count + 2) - fib_negative(count + 1)

k = int(input('Задайте число k: '))

positive = [fib_positive(i) for i in range(k + 1)]
negative = [fib_negative(i) for i in range(-1, -k - 1, -1)]
print(f'Для k = {k} список будет выглядеть так: {negative[::-1] + positive}')

