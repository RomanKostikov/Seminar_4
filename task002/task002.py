# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения
# 2) с помощью дополнительных библиотек Python
"""Doc."""
# import math
from math import sqrt
import os
os.system('cls')

# первое решение(групповое)
a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
x1 = 0
x2 = 0

disc = b**2 - 4*a*c
print(sqrt(disc))
if disc < 0:
    print("Корней нет.")
elif disc == 1:
    x1 = -b/(2*a)
    print(x1)
elif disc > 0:

    x1 = (-b - sqrt(disc))/(2*a)
    x2 = (-b + sqrt(disc))/(2*a)
    print(x1, x2)

# второе решение(с функциями)


# def findRoots(a, b, c):

#     dis_form = b * b - 4 * a * c
#     sqrt_val = math.sqrt(abs(dis_form))

#     if dis_form > 0:
#         print(" real and different roots ")
#         print((-b + sqrt_val) / (2 * a))
#         print((-b - sqrt_val) / (2 * a))

#     elif dis_form == 0:
#         print(" real and same roots")
#         print(-b / (2 * a))

#     else:
#         print("Complex Roots")
#         print(- b / (2 * a), " + i", sqrt_val)
#         print(- b / (2 * a), " - i", sqrt_val)


# a = int(input('Enter a:'))
# b = int(input('Enter b:'))
# c = int(input('Enter c:'))

# # If a is 0, then incorrect equation
# if a == 0:
#     print("Input correct quadratic equation")

# else:
#     findRoots(a, b, c)

# третье решение при помощи модуля Sympy
