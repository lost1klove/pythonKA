# 1. Представлен список чисел. Необходимо вывести элементы
#    исходного списка, значения которых больше предыдущего элемента.
#    Use comprehension.


from random import randint


def biggest_pre(n):
    list = [randint(0, 100) for _ in range(n)]
    print(list)
    return [n for i, n in enumerate(list[1:]) if n > list[i]]


num = int(input('Введите количество чисел в списке : '))
print(biggest_pre(num))
