def num_partitions(n, k):
    """
    >>> num_partitions(1, 1)
    1
    >>> num_partitions(1, 5)
    1
    >>> num_partitions(6, 3)
    7
    """
    if n < 0:
        return 0
    elif k == 1:
        return 1
    else:
        return num_partitions(n - k, k) + num_partitions(n, k - 1)
