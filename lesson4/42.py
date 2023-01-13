# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0,
# с помощью дополнительных библиотек python. Запросите значения А, В, С 3 раза.
# Уравнения и корни запишите в файл.
from math import sqrt


def find_disc(list):
    for i in range(3):
        d = (list[i + 3] ** 2) - 4 * (list[i]) * (list[i + 6])
        with open('Discr.txt', 'a', encoding='utf-8') as file:
            file.write(f'{list[i]}x² + {list[i + 3]}x + {list[i + 6]} = 0\n')
            if d > 0:
                x1 = (-(list[i + 3]) - sqrt(d)) / (2 * list[i])
                x2 = (-list[i + 3] + sqrt(d)) / (2 * list[i])
                file.write(f'(x1, x2) => {round(x1, 3), round(x2, 3)}\n')
            elif d == 0:
                x = -list[i + 3] // (2 * list[i])
                file.write(f'x = {x}\n')
            else:
                file.write('Нет корней!\n')


new_list = []

for i in range(3):
    for j in range(3):
        if i == 0:
            new_list.append(int(input(f'Введите число А{j + 1}: ')))
        if i == 1:
            new_list.append(int(input(f'Введите число B{j + 1}: ')))
        if i == 2:
            new_list.append(int(input(f'Введите число C{j + 1}: ')))

find_disc(new_list)
