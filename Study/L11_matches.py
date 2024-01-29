def matches(a, b):
    """
    Return the number of values k such that
    A[k] == B[k]

    >>> matches([1,2,3,4,5], [3,2,3,0,5])
    3
    >>> matches("abcd", "dcba")
    0
    >>> matches("abcde", "edcba")
    1
    >>> matches("abdomens", "indolence")
    4
    >>> matches("indolence", "abdomens")
    4
    """
    return sum(1 for x, y in zip(a, b) if x == y)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
