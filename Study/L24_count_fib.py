def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 2) + fib(n - 1)


def count(func):
    """Count version function for recursive function with ONE argument."""

    def counted(n):
        counted.call_count += 1
        return func(n)

    counted.call_count = 0
    return counted


fib = count(fib)
print(fib(10), fib.call_count)
print(fib(20), fib.call_count)
print(fib(30), fib.call_count)
