# 費波那契數字為 0、1、1、2、3、5、8、13、21 等等，每個數字與前一個數字的比例逐漸接近 1.618，即 phi。


# iter_improve(golden_update, golden_test)
def iter_improve(update, test, guess=1):
    while not test(guess):
        guess = update(guess)
    return guess


def near(x, f, g):
    return approx_eq(f(x), g(x))


def approx_eq(x, y, tolerance=1e-6):
    return abs(x - y) < tolerance


def golden_update(guess):
    return 1 / guess + 1


def golden_test(guess):
    return near(guess, square, successor)


def square(x):
    return x**2


def successor(x):
    return x + 1


print(iter_improve(golden_update, golden_test))
