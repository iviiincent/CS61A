import math


def is_prime(x):
    """
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(5)
    True
    >>> is_prime(6)
    false
    """

    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False

    return True


def print_prime(x):
    """
    Print the list with the value which is prime and within x (inclusive).
    """
    L = [i for i in range(2, x + 1) if is_prime(i)]
    print(L)


print_prime(100)


def print_multipy(x, y):
    for i in range(1, x + 1):
        for j in range(i + 1, y + 1):
            print(i, "*", j, "=", i * j)


print_multipy(3, 4)
