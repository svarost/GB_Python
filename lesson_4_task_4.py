# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# - k=4 => 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0 или 8*(x**4) + 5*x + 4 = 0 и т.д.

from random import randint
from pathlib import Path

def gen_polynom(k):
    if k == 0:
        return f'{randint(0, 100)} = 0'
    elif k == 1:
        return f'{randint(0, 100)}*x + {gen_polynom(k - 1)}'
    else:
        return f'{randint(0, 100)}*x^{k} + {gen_polynom(k - 1)}'

k = int(input('Введите степень k: '))
f_path = Path('data', 'out.txt')

with open(f_path, 'w') as f_data:
    f_data.write(gen_polynom(k))