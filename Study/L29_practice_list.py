def min_abs_indices(ll):
    """
    >>> min_abs_indices([-4,-3,-2,3,2,5])
    [2, 4]
    >>> min_abs_indices([1,2,3,4,5])
    [0]
    """
    min_abs = min(map(abs, ll))
    return [i for i in range(len(ll)) if abs(ll[i]) == min_abs]


def largest_adj_sum(ll):
    """
    >>> largest_adj_sum([-4,-3,-2,3,2,4])
    6
    >>> largest_adj_sum([-4,3,-2,-3,2,-4])
    1
    """
    return max([ll[i] + ll[i + 1] for i in range(len(ll) - 1)])


def digit_dict(ll):
    """
    >>> digit_dict([5,8,13,21,34,55,89])
    {1: [21], 3: [13], 4: [34], 5: [5, 55], 8: [8], 9: [89]}
    """
    last_digits = [x % 10 for x in ll]
    return {d: [x for x in ll if x % 10 == d] for d in range(10) if d in last_digits}


def all_have_an_equal(ll: list):
    """
    >>> all_have_an_equal([4,3,2,3,2,4])
    True
    >>> all_have_an_equal([-4,3,2,3,2,4])
    False
    """

    return min([ll.count(x) for x in ll]) > 1
