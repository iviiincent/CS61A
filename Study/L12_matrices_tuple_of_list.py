def matrix(rows, cols):
    """
    >>> matrix(2,3)
    [(0, 0, 0), (0, 0, 0)]
    >>> matrix(3,2)
    [(0, 0), (0, 0), (0, 0)]
    >>> matrix(3,3)
    [(0, 0, 0), (0, 0, 0), (0, 0, 0)]
    >>>
    """
    return [tuple(0 for col in range(cols)) for row in range(rows)]


def value(matrix, row, col):
    return matrix[row][col]


def set_value(matrix, row, col, val):
    matrix[row] = matrix[row][:col] + (val,) + matrix[row][col + 1 :]
    # elements before the element + the element which need to be changed + elements after it


if __name__ == "__main__":
    import doctest

    doctest.testmod()
