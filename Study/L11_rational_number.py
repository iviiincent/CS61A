from math import gcd


# Constructor
def make_rat(n, d):
    """
    The rational number N/D,
    assuming N, D are intergers and D != 0

    >>> make_rat(3,1)
    (3, 1)
    >>> make_rat(2,4)
    (1, 2)
    """
    g = gcd(n, d)
    n //= g
    d //= g
    return (n, d)


# Accessor
def numer(r):
    """
    The numerator of rational number R in lowest terms.
    """
    return r[0]


# Accessor
def denom(r):
    """
    The denominator of rational number R in lowest terms.
    Always positive.
    """
    return r[1]


def add_rat(x, y):
    """
    The sum of rational numbers X and Y.
    """
    return make_rat(numer(x) * denom(y) + numer(y) * denom(x), denom(x) * denom(y))


def mul_rat(x, y):
    """
    The product of rational numbers X and Y.
    """
    return make_rat(numer(x) * numer(y), denom(x) * denom(y))


def str_rat(r):
    """
    Return R as a string containing a rational fraction.

    >>> str_rat(make_rat(2,4))
    '1/2'
    >>> str_rat(make_rat(3,1))
    '3'
    """
    if denom(r) == 1:
        return str(numer(r))
    return "{numer(r)}/{denom(r)}"


def equal_rat(x, y):
    """
    Return True iff X == Y.
    """
    x = make_rat(numer(x), denom(x))
    y = make_rat(numer(y), denom(y))
    return numer(x) == numer(y) and denom(x) == denom(y)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
