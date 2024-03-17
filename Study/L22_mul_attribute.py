class A:
    i = "a"


class B:
    i = "b"


class C(A, B):
    def __init__(self) -> None:
        print("init")

    def print(self):
        print(self.i)


class D(B, A):
    def __init__(self) -> None:
        print("init")

    def print(self):
        print(self.i)


c, d = C, D
print(c.i, d.i)
