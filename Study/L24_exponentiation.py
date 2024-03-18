def exp(b, n):
    """
    Return b ^ n.

    exp(b, n) = 1 if n == 0
                exp(b, n//2) ** 2 if n is even
                b * exp(b, n-1) if n is odd
    >>> exp(5, 2)
    25
    >>> exp(5, 20)
    95367431640625
    >>> exp(5, 55)
    277555756156289135105907917022705078125
    """

    if n == 0:
        return 1
    elif n % 2 == 0:
        return (lambda x: x * x)(exp(b, n // 2))
    else:
        return b * exp(b, n - 1)
