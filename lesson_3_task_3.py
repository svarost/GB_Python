# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной идексах.
#
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных идексах элементы 3 и 9, ответ: 12

def odd_sum(lst: list):
    s = 0
    for i in range(1, len(lst), 2):
        s += lst[i]
    return s
lst = [2, 3, 5, 9, 3]
print(f'{lst} -> на нечётных индексах элементы ', end='')
for i in range(1, len(lst), 2):
    print(lst[i], end=', ')
print(f'ответ: {odd_sum(lst)}')