def gcd(n, d):
    while n != d:
        n, d = min(n, d), abs(n - d)
    return n


class Ratio:
    def __init__(self, n, d) -> None:
        assert d != 0, "Demon must not be 0."
        self.numer = n
        self.demon = d

    def __repr__(self) -> str:
        return f"Ratio({self.numer}, {self.demon})"

    def __str__(self) -> str:
        return f"{self.numer}/{self.demon}"

    def __add__(self, other):
        """
        >>> Ratio(1, 3) + Ratio(1, 6)
        Ratio(1, 2)
        >>> Ratio(1, 3) + Ratio(1, 1)
        Ratio(4, 3)
        >>> Ratio(1, 3) + 1
        Ratio(4, 3)
        """
        if isinstance(other, int):
            other = Ratio(other, 1)
        elif isinstance(other, float):
            return float(self) + other
        n = self.numer * other.demon + self.demon * other.numer
        d = self.demon * other.demon
        g = gcd(n, d)
        return Ratio(n // g, d // g)

    """
    >>> 1 + Ratio(1, 3)
    Ratio(4, 3)
    """
    __radd__ = __add__

    def __float__(self):
        """
        >>> float(Ratio(1,2))
        0.5
        >>> 0.2 + Ratio(1,5)
        0.4
        """
        return self.numer / self.demon
