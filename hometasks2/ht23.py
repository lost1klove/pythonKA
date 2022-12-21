# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# in
# 6

# out
# [2.0, 2.25, 2.37, 2.441, 2.488, 2.522]
# 14.071

n = int(input('Введите N: '))


def lists_summ (n):
    num_list =[]
    summ = 0
    for i in range (1,n+1):
        result = (1+1/i)**i
        round_result = round(result,3)
        num_list.append(round_result)
        summ += round_result
    return num_list,summ


print(lists_summ(n)[0])
print(lists_summ(n)[1])