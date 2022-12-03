# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением
# дробной части элементов.
#
# Пример:
# - [1.1, 1.2, 3.1, 10.01] => 0.19

def min_max(lst_num:list):
    for i in range(len(lst_num)):
        lst_num[i] = float('{:.2f}'.format(lst_num[i] - int(lst_num[i])))
    rez = {'min': min(lst_num), 'max': max(lst_num)}
    return rez

nums = [1.1, 1.2, 3.1, 10.01]

print(f"{nums} => {min_max(nums)['max'] - min_max(nums)['min']}")