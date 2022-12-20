# 1.5 Напишите программу, которая 
# 1. принимает на вход координаты двух точек и 
# 2. находит расстояние между ними в 2D пространстве.
# in
# - 3
# - 6
# - 2
# - 1

# out
# 5.099
import math

xa = int(input('Введите Xa: '))
xb = int(input('Введите Xb: '))
ya = int(input('Введите Ya: '))
yb = int(input('Введите Yb: '))

def coordinate2D(x1,x2,y1,y2):
    result = round(math.sqrt((x1-y1)**2 + (x2-y2)**2),3)
    return result

res = coordinate2D(xa,xb,ya,yb)
print(f'Расстояние между точками X и Y = {res}')

# сделал для пулл реквеста