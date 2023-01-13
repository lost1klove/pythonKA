# 1. Задайте натуральное число N.
# 2. Напишите программу, которая составит список простых множителей числа N.
# in
# 54
# out
# [2, 3, 3, 3]
# in
# 9990
# out
# [2, 3, 3, 3, 5, 37]
# in
# 650
# out
# [2, 5, 5, 13]

def facts_int(n):
    i = 2
    facts_list = []
    while i ** 2 <= n:
        while n % i == 0:
            facts_list.append(int(i))
            n = n / i
        i = i + 1
    if n > 1:
        facts_list.append(int(n))
    return facts_list


number = int(input('Введите число N: '))
result = facts_int(number)
print(f'Простые множители числа {number} =>\n{result}')
