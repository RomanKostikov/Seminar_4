# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.
"""Doc."""
import os
os.system('cls')


def prime_factors(n):
    i = 2
    lst = []
    while i * i <= n:
        while n % i == 0:
            lst.append(i)
            n = n / i
        i = i + 1
    if n > 1:
        lst.append(n)
    return lst


def main():
    n = int(input("Enter number: "))
    lst = prime_factors(n)
    print(f"List of prime factors of {n}:{lst}")


if __name__ == "__main__":
    main()
