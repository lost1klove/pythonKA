# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000
# in
# 11
# out
# 1011

n = int(input('Введите число, которое хотите перевести в двоичную систему: '))


def double_ns(num):
    double_list = []
    while num > 0:
        double_list.append(num % 2)
        num //= 2
    double_list.reverse()
    return double_list


result = double_ns(n)
print(*result)
