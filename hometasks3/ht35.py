# ** 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Негафибоначчи
#
# in
# 8
# out
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21
#
# in
# 5
# out
# 5 -3 2 -1 1 0 1 1 2 3 5
import collections

n = int(input('Введите число N :'))
def fibonacci(n):
    fib_list = [0,]
    fib_list_new = []
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
        fib_list.append(a)
        fib_list_new.append(a)
    for j in range(1,n,2):
        fib_list_new[j]*=(-1)
    fib_list_new.reverse()
    fib_list_new.extend(fib_list)
    return fib_list_new

result_list = fibonacci(n)
print(f'↓ Последовательность Фибоначчи,в том числе для отрицательных индексов от числа {n} ↓\n {result_list}')