# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#
# Пример:
# 0,56 -> 11

num = input('Введите вещественное число: ')
punctuation = [',', '.']

for p in punctuation:
    num = num.replace(p, '')

sum_num = 0
for n in num:
    sum_num += int(n)
print(sum_num)