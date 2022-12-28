# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.
"""Doc."""
import os
os.system('cls')


def return_unique(lst):
    result = []
    for char in lst:
        if lst.count(char) < 2:
            result.append(char)
    return result


def main():
    lst1 = list(map(int, input("Enter numbers in space:\n").split()))
    print(f"Original list: {lst1}")
    lst2 = return_unique(lst1)
    print(f"List of non-repeating elements: {lst2}")


if __name__ == '__main__':
    main()
