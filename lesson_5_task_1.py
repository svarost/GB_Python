# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

str_ = input('Введите строку: ')

out_str_ = ' '.join(list(filter(lambda item: 'абв' not in item, [i for i in str_.split()])))
print(out_str_)
