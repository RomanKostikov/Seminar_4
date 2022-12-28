# Вычислить число pi c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
"""Doc."""
import math
import os
os.system('cls')

# первое решение оформлено в функции


# def calc_pi(eps=1.0e-5):
#     s = 0
#     d = 1
#     sgn = 1
#     while True:
#         a = 4/d
#         s = s+sgn*a
#         if a < eps:
#             return s
#         sgn = -sgn
#         d = d+2


# def main():
#     print(calc_pi())


# if __name__ == "__main__":
#     main()

# второе решение(math)

d = input('Enter rounding exponence'
          'in 0.01 format from 10 ^ -1 to 10 ^ -10 -> ')
d = d[2:len(d)]
print(round(math.pi, len(d)))
