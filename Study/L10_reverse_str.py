def reverse_str(str):
    """
    >>> reverse_str('321')
    '123'
    >>> reverse_str('abc')
    'cba'
    >>> reverse_str('ab12cd34')
    '43dc21ba'
    """
    return str[::-1]


# Use str method.
def reverse_digit(num):
    """
    Return the number whose base-10 representation is the reverse of that of NUM,
    assuming NUM >= 0.

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

    return int(str(num)[::-1])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
