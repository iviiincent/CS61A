def interleaving_digits(a, b):
    """
    Assuming A >= 0 and B >= 0 have same number of digits,
    return the number whose base-10 repersentation is the interleaving of A's and B's digits,
    starting with A.

    >>> interleaving_digits(0,1)
    1
    >>> interleaving_digits(1,0)
    10
    >>> interleaving_digits(1357,2468)
    12345678
    """

    if a < 10:
        return a * 10 + b
    return interleaving_digits(a // 10, b // 10) * 100 + interleaving_digits(
        a % 10, b % 10
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
