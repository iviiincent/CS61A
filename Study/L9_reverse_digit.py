def reverse_digit(n):
    """
    Assuming N >= 0 is an integer,
    return the number whose base-10 repersentation is the reverse of that of N.

    >>> reverse_digit(0)
    0
    >>> reverse_digit(1)
    1
    >>> reverse_digit(12045)
    54021
    >>> reverse_digit(1100)
    11
    >>> reverse_digit(12321)
    12321
    >>> reverse_digit(1111)
    1111
    """

    assert type(n) == int and n >= 0
    if n < 10:
        return n
    return reverse_digit(n // 10) + (n % 10) * 10 ** (num_digit(n) - 1)


def num_digit(n):
    cnt = 1
    while n > 10:
        n //= 10
        cnt += 1
    return cnt


if __name__ == "__main__":
    import doctest

    doctest.testmod()
