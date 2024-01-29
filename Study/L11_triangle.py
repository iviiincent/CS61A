def triangle(n):
    """
    Assuming N >= 0,
    return the list consiting of N lists:
    [1], [1, 2], ..., [1, 2, ... , N]

    >>> triangle(1)
    [[1]]
    >>> triangle(2)
    [[1], [1, 2]]
    >>> triangle(5)
    [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5]]
    >>> triangle(10)
    [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    """

    # res = []
    # for i in range(1, n + 1):
    #     cur = []
    #     for j in range(1, i + 1):
    #         cur.append(j)
    #     res.append(cur)
    # return res

    return [list(range(1, i + 1)) for i in range(1, n + 1)]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
