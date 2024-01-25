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
