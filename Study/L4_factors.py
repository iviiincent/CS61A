def factor(n):
    """
    >>> factor(20)
    20
    10
    5
    4
    2
    1
    """
    i = n
    while i > 0:
        if n % i == 0:
            print(i)
        i -= 1
