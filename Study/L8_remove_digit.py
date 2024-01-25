def remove_digit(n, digit):
    """
    Assuming N >= 0, 0 <= DIGIT <= 9,
    return the number base-10 repersentation is same as N,
    but with all instances of DIGIT removed.
    If all digits removed, return 0.

    >>> remove_digit(31415926535, 5)
    31419263
    >>> remove_digit(31415926535, 3)
    141592655
    >>> remove_digit(1234, 5)
    1234
    >>> remove_digit(888, 8)
    0
    """
    if n == 0:
        return 0
    elif n % 10 == digit:
        return remove_digit(n // 10, digit)
    else:
        return n % 10 + remove_digit(n // 10, digit) * 10


if __name__ == "__main__":
    import doctest

    doctest.testmod()
