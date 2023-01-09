# 1. Напишите программу, которая
# 2. найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]
# in
# 5
# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

from random import sample
n = int(input('Введите N: '))
new_list = sample(range(1, (n+1)*2), k=n)


def mult(list):
    multiple = []
    j=0
    k=len(list)-1
    if len(list) % 2 == 1:
        for i in range((len(list)//2)):
            multiple.append(list[j] * list[k])
            j=j+1
            k=k-1
            if j==k: multiple.append(list[j])
    if len(list)%2 == 0:
        for i in range(len(list)//2):
            multiple.append(list[j] * list[k])
            j=j+1
            k=k-1
    return multiple

result = mult(new_list)
print(new_list)
print(result)