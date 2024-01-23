def isprime(n):
    """
    >>> isprime(1)
    False
    >>> isprime(2)
    True
    >>> isprime(17)
    True
    >>> isprime(25)
    False
    """
    return n >= 1 and smallest_factor(n) == n


def smallest_factor(n):
    """
    >>> smallest_factor(2)
    2
    >>> smallest_factor(3)
    3
    >>> smallest_factor(8)
    2
    """
    i = 2
    while i <= n:
        if n % i == 0:
            return i
        i += 1


def print_factors(n):
    """
    >>> print_factors(2)
    2
    >>> print_factors(10)
    2
    5
    >>> print_factors(40)
    2
    2
    2
    5
    """
    while n > 1:
        f = smallest_factor(n)
        print(f)
        n //= f