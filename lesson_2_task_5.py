from random import randint

def mix_list(lst: list):
    indexes = []
    for i in range(len(lst)):
        index = randint(0, len(lst) - 1)
        while index in indexes:
            index = randint(0, len(lst) - 1)
        indexes.append(index)
        temp = lst[i]
        lst[i] = lst[indexes[i]]
        lst[indexes[i]] = temp
    return  lst

lst = [randint(0, 9) for _ in range(int(input('Введите количество элементов в массиве: ')))]
print(lst)
print(mix_list(lst))