# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
#
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


# def multiply_num(n: int):
#     if n == 1:
#         return 1
#     else:
#         return n * multiply_num(n - 1)
#
# # N = int(input('Введите число N: '))
# rez = []
# str = ['1']
#
# for i in range(N):
#     rez.append(multiply_num(i + 1))
# for i in range(2, N + 1):
#     str.append(str[i - 2] + f'*{i}')
#
# print(f'Пусть N = {N}, тогда ', end='')
# print(rez, end=' ')
# print('(' + ', '.join(str) + ')')

import math

N = int(input('Введите число N: '))

nums = list(map(lambda i: math.prod([j for j in range(1, i + 1)]), [el for el in range(1, N + 1)]))
st = list(map(lambda i: "*".join([str(j) for j in range(1, i + 1)]), [el for el in range(1, N + 1)]))

print(f'Пусть N = {N}, тогда {nums} ({", ".join(st)})', end='')



