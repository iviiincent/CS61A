def combine_functions(op):
    """combine_functions(op)(f(x), g(x)) = op(f(x), g(x))"""

    def combine(f, g):
        def val(x):
            return op(f(x), g(x))

        return val

    return combine


add_function = combine_functions(lambda x, y: x + y)

from math import sin, cos, pi

h = add_function(sin, cos)

print("sin(pi/4) + cos(pi/4) =", h(pi / 4))  # sin(pi/4) + cos(pi/4) = sqrt(2)
