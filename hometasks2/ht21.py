# Напишите программу, которая
# 1. принимает на вход вещественное число и
# 2. показывает сумму его цифр.
# Без работы с методами строк.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27


num = float(input('Введите число : '))


def summ_numbers(n):
    n_len = len(str(num))
    n_new = num * 10 ** (n_len-2)
    total_num = 0
    while n_new != 0:
        total_num += n_new%10
        n_new //= 10
    return int(total_num)

result = str(summ_numbers(num))
print(result)
