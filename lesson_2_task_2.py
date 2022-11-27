# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
#
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def multiply_num(n: int):
    if n == 1:
        return 1
    else:
        return n * multiply_num(n - 1)

N = int(input('Введите число N: '))
rez = []
str = ['1']

for i in range(N):
    print(multiply_num(i))
    rez.append(multiply_num(i))
for i in range(2, N + 1):
    str.append(str[i - 2] + f'* {i}')

# print(f'Пусть N = {N}, тогда [ ')
# print(rez, sep=', ')
# print(f'] ({str})', sep=', ')