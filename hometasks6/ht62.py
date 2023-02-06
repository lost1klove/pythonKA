# 2. Для чисел в пределах от 20 до n найти числа,
#    кратные 20 или 21. Use comprehension.

def fractional_list(n):
    return [(i,(f'{i} кратно 20')) for i in range(20, n + 1) if i % 20 == 0 or i % 21 == 0]
    # TODO допилить вывод
    # [i for i in range(20, n + 1) if i % 20 == 0 and print([f'{i} кратно 20']) or i % 21 == 0 and print([f'{i} кратно 21'])]


num = int(input('Введите число N : '))

print(fractional_list(num))
