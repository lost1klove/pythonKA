# 3. На вход программе подается число n.
# Программа печатает численный треугольник.
# Используем вложенные циклы.

iteration = int(input('Введите число n: '))

for i in range(1,iteration+1):
    for j in range(i):
        print(i, end='')
    print()
