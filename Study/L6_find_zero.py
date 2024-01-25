def find_zero(lowest, highest, func):
    """still a tail recursion"""
    if lowest > highest:
        return None
    elif func(lowest) == 0:
        return lowest
    else:
        return find_zero(lowest + 1, highest, func)


# equivalent iterative solution
def find_zero_interative(lowest, highest, func):
    while func(lowest) <= 0:
        if func(lowest) == 0:
            return lowest
        lowest += 1
    return lowest


def find_zero_mid(lowest, highest, func):
    if lowest > highest:
        return None
    middle = (lowest + highest) // 2
    if func(middle) == 0:
        return middle
    elif func(middle) < 0:
        return find_zero_mid(middle + 1, highest, func)
    else:
        return find_zero_mid(lowest, middle - 1, func)
