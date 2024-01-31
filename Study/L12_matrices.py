def matrix(rows, cols):
    """
    >>> matrix(2,3)
    [[0, 0, 0], [0, 0, 0]]
    >>> matrix(3,2)
    [[0, 0], [0, 0], [0, 0]]
    >>> matrix(3,3)
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    >>>
    """
    return [[0 for col in range(cols)] for row in range(rows)]


def value(matrix, row, col):
    return matrix[row][col]


def set_value(matrix, row, col, val):
    matrix[row][col] = val


if __name__ == "__main__":
    import doctest

    doctest.testmod()
