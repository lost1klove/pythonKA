# *  Задайте список из произвольных вещественных чисел,
# 1. количество задаёт пользователь.
# 2. Напишите программу, которая
# 3. найдёт разницу между максимальным и минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76
# in
# 3
# out
# [9.26, 8.5, 1.14]
# Min: 0.14, Max: 0.5. Difference: 0.36
import random
n = int(input('Введите количество чисел в списке: '))

float_list = []
for i in range(n):
    float_list.append(round(random.uniform(1, n*5), 2))


def decimal_nums(list):
    new_diff_list = []
    for i in list:
        new_diff_list.append(int(round(((i % 1)*100), 2)))
    return new_diff_list


def diff(list):
    min = list[0]
    max = list[0]
    diff_num = 0
    for i in list:
        if i > max:
            max = i
        elif i < min:
            min = i
    diff_num = max - min
    return diff_num


new_list = decimal_nums(float_list)
result = diff(new_list)
print(float_list)
print(result)
