# 3. Задайте два числа. Напишите программу,
# которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
"""Doc."""
import os
os.system('cls')

number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))
max_num = max(number_1, number_2)
min_num = min(number_1, number_2)
for num in range(max_num, number_1*number_2 + 1, max_num):
    if num % min_num == 0:
        print(num)
        break
