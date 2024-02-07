def tree(tree, children=[]):
    return (tree, children)


def label(tree):
    return tree[0]


def children(tree):
    return tree[1]


#


def is_leaf(t):
    return children(t) == []


def set_label(tree, label):
    tree[0] = label


def count_leaves(t):
    """
    Return the number of leaf nodes in T.
    >>> count_leaves(tree(20,
    ...                  [tree(12,
    ...                      [tree(9,
    ...                          [tree(7),
    ...                          tree(2)]),
    ...                      tree(3)]),
    ...                  tree(8,
    ...                      [tree(4),
    ...                      tree(4)])]))
    5
    """
    if is_leaf(t):
        return 1
    else:
        return sum([count_leaves(leave) for leave in children(t)])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
