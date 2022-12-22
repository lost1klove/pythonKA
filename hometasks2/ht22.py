# Напишите программу, которая
# 1. принимает на вход число N и
# 2. выдает набор произведений чисел от 1 до N в виде списка.

num = int(input('Введите число N: '))


def factorial(n):
    num_list = []
    fact = 1
    for i in range(1, n+1):
        fact *= i
        num_list.append(fact)
    return num_list


print(factorial(num))
