def if_function(then_expr, condition, else_expr):
    return then_expr() if condition else else_expr()


x = -1
print(if_function(lambda: 1 / x, x > 0, lambda: 0))
x = 0
print(if_function(lambda: 1 / x, x > 0, lambda: 0))
x = 10
print(if_function(lambda: 1 / x, x > 0, lambda: 0))
