# Задайте строку из набора чисел. Напишите программу,
# 1.которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

def check():
    enter_list = input('Введите числа через пробел: ').split()
    new_list = []
    for i in range(len(enter_list)):
        enter_list[i] = enter_list[i].strip("'![,;.")
        if enter_list[i].isdigit:
            new_list.append(enter_list[i])
    return new_list


def max_min_finder(list):
    if list:
        return max(list, key=int), min(list, key=int)
    return []


print(max_min_finder(check()))
