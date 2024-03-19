def invert(x):
    res = 1 / x
    print("Never printed if x is 0")
    return res


def invert_safe(x):
    try:
        return invert(x)
    except ZeroDivisionError as e:
        return 0
