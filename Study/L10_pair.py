def pair(x, y):
    """
    Return the value represent the ordered pair of value (X, Y),
    X >= 0, Y >= 0
    """

    def pair_func(which, val=None):
        nonlocal x, y
        if which == 0:
            return x
        elif which == 1:
            return y
        elif which == 2:
            a = val
        else:
            b = val

    return pair_func


def left(p):
    """
    Assuming p was created by pair(x, y),
    return the value x.
    """
    return p(0)


def right(p):
    """
    Assuming p was created by pair(x, y),
    return the value y.
    """
    return p(1)


def set_left(p, val):
    """
    Given P represents the pair(X, Y),
    cause P to represent (VAL, Y),
    return None
    """
    p(2, val)
    return None


def set_right(p, val):
    """
    Given P represents the pair(X, Y),
    cause P to represent (X, VAL),
    return None
    """
    p(3, val)
    return None
