# 1.3. Напишите программу, которая
# 1. будет на вход принимать число N и
# 2. выводить числа от -N до N

n = int(input('Введите число N: '))

print(*range(- n, n + 1))