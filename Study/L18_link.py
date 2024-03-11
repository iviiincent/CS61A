class Link:
    empty = ()

    def __init__(self, first, rest=empty) -> None:
        self.first = first
        self.rest = rest

    def __str__(self):
        res = []
        p = self
        while p != ():
            res.append(p.first)
            p = p.rest
        return str(res)

    def __repr__(self) -> str:
        if self.rest:
            rest_repr = f", {repr(self.rest)}"
        else:
            rest_repr = ""
        return f"Link({repr(self.first)}{rest_repr})"


def range_link(start, end):
    if start >= end:
        return Link.empty
    return Link(start, range_link(start + 1, end))


def map_link(f, ll):
    if ll is Link.empty:
        return Link.empty
    return Link(f(ll.first), map_link(f, ll.rest))


l15 = range_link(1, 5)
print(l15)
print(map_link(lambda x: x**2, l15))
