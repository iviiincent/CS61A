def combine_functions(op):
    """combine_functions(op)(f(x), g(x)) = op(f(x), g(x))"""

    def combine(f, g):
        def val(x):
            return op(f(x), g(x))

        return val

    return combine


from operator import add

add_function = combine_functions(add)
from math import sin, cos, pi

h = add_function(sin, cos)
print("sin(pi/4) + cos(pi/4) =", h(pi / 4))  # sin(pi/4) + cos(pi/4) = sqrt(2)

# same
h2 = combine_functions(add)(sin, cos)
print(h2(pi / 4))
