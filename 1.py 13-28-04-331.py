class c:
    def __init__(self) -> None:
        self.i = 0

    def a(self):
        self.i += 1
        print(c.i, self.i)

    def b(self):
        c.i += 10
        print(c.i, self.i)


c0 = c()
c1 = c()

c0.a()
c1.a()

c0.b()
c1.b()
