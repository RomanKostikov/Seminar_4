# 1. Задайте строку из набора чисел. Напишите программу,
# которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.
"""Doc."""
import os
os.system('cls')

# первое решение
# line = '1, 2, 3, 4, 5'
# list = []

# for i in range(len(line)):
#     if line[i] != ',' and line[i] != ' ':
#         list.append(int(line[i]))

# print(*list)
# print(f'Min: {min(list)}')
# print(f'Max: {max(list)}')

# второе решение(групповое)
my_list = input('Enter numbers in space: ').split()
# print(my_list)
num = list(map(int, my_list))
# print(num)
print(f'Min: {min(num)}')
print(f'Max: {max(num)}')

# третье решение(без map)
# number_list = input('Enter numbers in space: ').split()

# max_num = int(number_list[0])
# min_num = int(number_list[0])
# for el in number_list:
#     el = int(el)
#     if max_num < el:
#         max_num = el
#     if min_num > el:
#         min_num = el

# # print(number_list)
# print(max_num, min_num)

# четвертое решение (с функциями)
# def String_Min_and_Max(str):
#     list1 = str.split(' ')
#     #print(list1)
#     min = int(list1[0])
#     max = int(list1[0])
#     for i in range(len(list1)):
#         list1[i] = int(list1[i])
#         if list1[i]<min:
#             min = list1[i]
#         if list1[i]>max:
#             max = list1[i]
#     return min, max
#     #print(f'Минимум равен {min}, максимум равен {max}')


# a = input('Enter numbers in space: ')
# print(String_Min_and_Max(a))
