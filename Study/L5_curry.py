def curry2(f):
    return lambda x: lambda y: f(x, y)


from operator import add

print("\n", curry2(add))  # funtion : add
print("\n", curry2(add)(10))  # function : one number add 10
print("\n", curry2(add)(10)(20))  # val : 10 + 20
