def tree(label, children=[]):
    """
    >>> tree(19, [tree(8), tree(9)])
    (19, [(8, []), (9, [])])
    """
    return (label, children)


def label(tree):
    return tree[0]


def children(tree):
    return tree[1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
