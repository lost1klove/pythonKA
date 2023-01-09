# ** 5. Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]
from random import randrange

size = int(input('Введите размер списка: '))

new_list = []
for i in range(size):
    new_list.append(i)

def mix_lists(orig_list):
    mixed_list = orig_list[:]
    for i in range(len(new_list)):
        random_index = randrange(0,(len(new_list)-1))
        temp = mixed_list[i]
        mixed_list[i] = mixed_list[random_index]
        mixed_list[random_index] = temp
    return mixed_list

print(new_list)
print(mix_lists(new_list))

