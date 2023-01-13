# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001
#
# out
# 9.000000
from decimal import Decimal as d

number = d(input('Введите число: '))
accuracy = str(input('Введите точность в формате 0.00001: '))

number = number.quantize(d(accuracy))

print(number)
