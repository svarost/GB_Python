# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов
# (складываются числа, у которых "х" в одинаковых степенях).
# Пример того, что будет в итогвом файле: 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0

# file_1: 19*x^5 + 43*x^4 + 95*x^3 + 7*x^2 + 11*x + 56 = 0
# file_2: 3*x^4 + 6*x^3 + 2*x^2 + 3*x + 1 = 0

from pathlib import Path

def pol_to_dic(lst):
    d = {}
    for el in lst:
        if 'x' in el:
            k = el[el.find('*') + 1:].strip()
            v = int(el[:el.find('*')])
        else:
            k = 'not'
            v = int(el[:el.find(' =')])
        d[k] = v
    return d

def dic_to_pol(dic):
    s = ''
    for key, value in dic.items():
        if 'x' in key:
            s += f'{value}*{key} + '
        else:
            s += f'{value} = 0'
    return s

def sum_dic(d1, d2):
    rez = d1
    for key, value in rez.items():
        if key in d2:
            rez[key] += d2[key]
        else:
            rez.update({key: value})
    return rez

f_path_1 = Path('data', '5_1.txt')
f_path_2 = Path('data', '5_2.txt')

with open(f_path_1, 'r') as file_1:
    f_data_1 = [i for i in file_1.read().split('+')]

with open(f_path_2, 'r') as file_2:
    f_data_2 = [i for i in file_2.read().split('+')]

sum = sum_dic(pol_to_dic(f_data_1), pol_to_dic(f_data_2))

f_path = Path('data', 'result')
with open(f_path, 'w') as file:
    file.write(dic_to_pol(sum))