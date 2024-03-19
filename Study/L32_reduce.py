from operator import add, mul, truediv


def reduce(func, s, initial):
    """
    >>> reduce(mul, [2, 4, 8], 1)
    64
    >>> reduce(add, [1, 2, 3], 4)
    10
    """
    if not s:
        return initial
    else:
        return reduce(func, s[1:], func(initial, s[0]))


def divide_all(n, ds):
    """
    >>> divide_all(64, [2 ,2, 2])
    8.0
    >>> divide_all(64, [2 ,2, 2, 0])
    inf
    """
    try:
        return reduce(truediv, ds, n)
    except ZeroDivisionError as e:
        return float("inf")
