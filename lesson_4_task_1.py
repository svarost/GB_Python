# Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141

import math

d = str(float(input('Задайте точность числа π:'))).split('.')[1]

pi_ = str(math.pi)[:len(d) + 2]
print(f"π = {pi_}")

