# * Напишите программу, которая
# 1. принимает на вход 2 числа.
# 2. Получите значение N, для пустого списка,
# 3. заполните числами в диапзоне [-N, N].
# 4. Найдите произведение элементов на указанных позициях(не индексах).
# Enter the value of N: 5
# Position one: 1
# Position two: 2
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 20

# Enter the value of N: 4
# Position one: 20
# Position two: 22
# -> [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# -> There are no values for these indexes!
n = int(input('Введите N: '))
pos_one = int(input('Позиция 1: '))
pos_two = int(input('Позиция 2: '))

new_pos = 0
new_list = []

for i in range(-n, n+1):
    new_list.append(i)

print(new_list)

if pos_two == 0 or pos_one == 0:
    print('На нулевой позиции нет значения')
elif pos_one > len(new_list) or pos_two > len(new_list):
    if  pos_one > len(new_list):
        if pos_two > len(new_list):
            print(f"На позициях {pos_one} и {pos_two} нет значения!")
        else:
            print(f"На позиции {pos_one} нет значения!")
    else:
        print(f"На позиции {pos_two} нет значения!")
       
elif new_list[pos_one-1] in new_list and new_list[pos_two-1] in new_list:
    new_pos = new_list[pos_one-1]*new_list[pos_two-1]
    print(new_pos)
