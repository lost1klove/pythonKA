# 1.2 Напишите программу, которая
# 1. на вход принимает 5 чисел и 
# 2. находит максимальное из них.

max_number = 0
for i in range(5):
    num = int(input(f'Введите число {i+1}: '))
    if num > max_number:
        max_number = num
print(f'максимальное число = {max_number}')