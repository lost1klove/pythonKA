# 1. Задайте список, состоящий из произвольных чисел, 
# 2. количество задаёт пользователь.
# Напишите программу, которая 
# 3. определит, присутствует ли в заданном списке число,
# полученное от пользователя.
from random import sample
import os
clear = lambda: os.system('cls')
clear()

num_amount = int(input('Enter amount : '))
user_num = int(input('Enter desired number : '))


def find_number(amount, user_number):
    new_list = sample(range(1,(amount+1)*2), k=amount)
    print(new_list)
    if user_number in new_list:
        return "yes"
    return "no"

result = find_number(num_amount, user_num)
print (result)