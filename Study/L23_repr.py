class Bear:

    def __init__(self) -> None:
        self.__repr__ = lambda: "self repr"
        self.__str__ = lambda: "self str"

    def __str__(self) -> str:
        return "Bear str"

    def __repr__(self) -> str:
        return "Bear repr"


oski = Bear()
print(oski)
print(repr(oski))


def repr(x):
    return type(x).__repr__(x)


def str(x):
    t = type(x)
    if hasattr(x, "__str__"):
        return t.__str__(x)
    else:
        return repr(x)
