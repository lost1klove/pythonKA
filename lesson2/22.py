# Создать список 
# 1. длины n, значения формируются по формуле 3k + 1,
# где k 
# 2. принимает значения от 1 до n включительно.

num = int(input('Введите N: '))
num_list =[]

for i in range (1,num+1):
    num_list.append((3*i)+1)
print(num_list)