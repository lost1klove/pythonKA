# 1.1 Напишите программу, которая
# принимает на вход два числа
# и проверяет, является ли одно число квадратом другого.

num1 = int(input('input num A: '))
num2 = int(input('input num B: '))

if num1 == num2 ** 2 or num2 == num1**2:
    print('Yes')
else:
    print('no')