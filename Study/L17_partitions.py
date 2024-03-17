def yield_partitions(n, m):
    """
    >>> for p in yield_partitions(6, 4): print(p)
    2 + 4
    1 + 1 + 4
    3 + 3
    1 + 2 + 3
    1 + 1 + 1 + 3
    2 + 2 + 2
    1 + 1 + 2 + 2
    1 + 1 + 1 + 1 + 2
    1 + 1 + 1 + 1 + 1 + 1
    """

    if n > 0 and m > 0:
        if n == m:
            yield f"{m}"
        for p in yield_partitions(n - m, m):
            yield f"{p} + {m}"
        yield from yield_partitions(n, m - 1)
