# Задайте список, состоящий из произвольных чисел,
# 1. количество задаёт пользователь.
# 2. Напишите программу, которая
# 3. найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
#
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22
from random import sample

n = int(input('Введите N: '))
new_list = sample(range(1, (n + 1) * 2), k=n)


def find_summ(list):
    summ = 0
    for i in range(0, (len(list)), 2):
        summ += list[i]
    return summ


print(new_list)
result = find_summ(new_list)


print(result)
