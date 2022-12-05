# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

def simpl_num(n:int):
    if n < 4:
        return [i for i in range(1, n + 1)]
    else:
        nums = [i for i in range(1, 4)]

        for i in range(4, n + 1):
            k = 0
            for el in nums[1:]:
                if i % el == 0:
                    k += 1
            if k == 0:
                nums.append(i)
        return nums

n = int(input('Введите натуральное число N: '))

print(f'Список простых чисел последовательности N => {simpl_num(n)}')
