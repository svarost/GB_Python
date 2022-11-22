# Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

## -*- coding: utf-8 -*-

for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            print(f'¬({bool(x)} ⋁ {bool(y)} ⋁ {bool(z)}) = ¬{bool(x)} ⋀ ¬{bool(y)} ⋀ ¬{bool(z)}', end=' ')
            print(f' --> {(not(x or y or z) == (not x and not y and not z))}')