class Parent:
    def f(s):
        print("Parent.f")

    def g(s):
        s.f()


class Child(Parent):
    def f(me):
        print("Child.f")


a_child = Child()
a_child.g()
