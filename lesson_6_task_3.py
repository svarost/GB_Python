# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах.
# Индексы вводятся одной строкой, через пробел.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# --> 0 2 3
# -3 * -1 * 0 = 0
# Вывод: 0

# n = int(input('Введите N: '))
# ls = [num for num in range(-n, n + 1)]
# print(ls)
# index = [int(i) for i in input('Введите индексы: ').split()]
# print(index)
#
# s = 1
# for i in index:
#     s *= ls[i]
# print(f'Вывод: {s}')

import math

n = int(input('Введите N: '))
ls_1 = [num for num in range(-n, n + 1)]
ind = [int(i) for i in input('Введите индексы: ').split()]
mul = math.prod(list(filter(lambda i: ls_1.index(i) in ind, ls_1)))
print(ls_1)
print(mul)
