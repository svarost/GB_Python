# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def mul_pair(lst: list):
    res = []
    back_indx = -1
    count = int(len(lst)/2) if len(lst) % 2 == 0 else int(len(lst) / 2 + 1)
    for i in range(count):
        res.append(lst[i] * lst[back_indx])
        back_indx-=1
    return res

lst = [2, 3, 4, 5, 6]
print(f'{lst} => {mul_pair(lst)}')