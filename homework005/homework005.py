# Даны два файла, в каждом из которых находится запись многочлена.
#  Задача - сформировать файл, содержащий сумму многочленов.
"""Doc."""
import random
import os
os.system('cls')


# запись в файл


def write_file(name, st):
    with open(name, 'w') as data:
        data.write(st)

# создание случайного числа от 0 до 100


def rnd():
    return random.randint(0, 101)

# создание коэффициентов многочлена


def create_mn(k):
    lst = [rnd() for i in range(k+1)]
    return lst

# создание многочлена в виде строки


def create_str(sp):
    lst = sp[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0 or lst[i+2] != 0:
                    wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}x'
                if lst[i+1] != 0 or lst[i+2] != 0:
                    wr += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += ' = 0'
    return wr

# получение степени многочлена


def sq_mn(k):
    if 'x^' in k:
        i = k.find('^')
        num = int(k[i+1:])
    elif ('x' in k) and ('^' not in k):
        num = 1
    else:
        num = -1
    return num

# получение коэффицента члена многочлена


def k_mn(k):
    if 'x' in k:
        i = k.find('x')
        num = int(k[:i])
    return num

# разбор многочлена и получение его коэффициентов


def calc_mn(st):
    st = st[0].replace(' ', '').split('=')
    st = st[0].split('+')
    lst = []
    size = len(st)
    if sq_mn(st[-1]) == -1:
        lst.append(int(st[-1]))
        size -= 1
    i = 1  # степень
    ii = size-1  # индекс
    while ii >= 0:
        if sq_mn(st[ii]) != -1 and sq_mn(st[ii]) == i:
            lst.append(k_mn(st[ii]))
            ii -= 1
            i += 1
        else:
            lst.append(0)
            i += 1

    return lst


def main():
    # создание двух файлов
    k1 = int(input("Enter the natural degree for file 1: k = "))
    k2 = int(input("Enter the natural degree for file 2: k = "))
    coefficient1 = create_mn(k1)
    coefficient2 = create_mn(k2)
    write_file("file1.txt", create_str(coefficient1))
    write_file("file2.txt", create_str(coefficient2))

    # нахождение суммы многочлена

    with open('file1.txt', 'r') as data:
        st1 = data.readlines()
    with open('file2.txt', 'r') as data:
        st2 = data.readlines()
    print(f"First polynomial: {st1}")
    print(f"Second polynomial: {st2}")
    lst1 = calc_mn(st1)
    lst2 = calc_mn(st2)
    ll = len(lst1)
    if len(lst1) > len(lst2):
        ll = len(lst2)
    lst_new = [lst1[i] + lst2[i] for i in range(ll)]
    if len(lst1) > len(lst2):
        mm = len(lst1)
        for i in range(ll, mm):
            lst_new.append(lst1[i])
    else:
        mm = len(lst2)
        for i in range(ll, mm):
            lst_new.append(lst2[i])
    write_file("file_res.txt", create_str(lst_new))
    with open('file_res.txt', 'r') as data:
        st3 = data.readlines()
    print(f"Resulting polynomial: {st3}")


if __name__ == '__main__':
    main()
