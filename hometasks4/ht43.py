# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
# in
# 7
# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]
# in
# -1
# out
# Negative value of the number of numbers!
# []
# in
# 10
# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]

from collections import Counter as ct


def fill_list():
    enter_list = list(input('Введите числа через пробел: ').split())
    new_list = []
    for i in range(len(enter_list)):
        if enter_list[i].isdigit() and (enter_list[i] not in new_list):
            new_list.append(enter_list[i])
    return enter_list, new_list


def search_unique(list):
    sort_lst = []
    copy_lst = []
    for i in range(len(list)):
        if (list.count(list[i])) != 1:
            sort_lst.append(i)
    for i in range(len(list)):
        if i not in sort_lst:
            copy_lst.append(list[i])
    return copy_lst


lst = fill_list()
print(f"Исходный список: {lst[0]}")
new_lst = search_unique(lst[0])
print(f"Список из неповторяющихся элементов: {new_lst}")
