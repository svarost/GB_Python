# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def rle_encode(data):
    count = 0
    prev_char = data[0]
    res = ''
    for char in data:
        if char == prev_char:
            count += 1
        else:
            res += f"{count}{prev_char}"
            count = 1
            prev_char = char
    return res + f"{count}{prev_char}"

def rle_decode(data):
    count = ''
    res = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            res += char * int(count)
            count = ''
    return res

data = "AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE"
print(data)

print(rle_encode(data))

print(rle_decode(rle_encode(data)))
