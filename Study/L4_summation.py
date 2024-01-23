def summation(n, term, next):
    sum, k = 0, 1
    while k <= n:
        sum += term(k)
        k = next(k)
    return sum

def sum_cubes(n):
    """
    >>> sum_cubes(1)
    1
    >>> sum_cubes(3)
    14
    """
    return summation(n, lambda x: x ** 2, lambda x: x + 1)

def pi_sum(n):
    """
    >>> pi_sum(100)
    3.121594652591009
    """
    return summation(n, lambda x: 8 / (x * (x + 2)), lambda x: x + 4)