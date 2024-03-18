def memo_dic(func):
    """Memoization version function for function using dictionary as cache."""
    cache = {}

    def memoized(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]

    return memoized


def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)


def count(func):
    """Count version function for recursive function with ONE argument."""

    def counted(n):
        counted.call_count += 1
        return func(n)

    counted.call_count = 0
    return counted


fib = count(memo_dic(fib))
print(fib(5), fib.call_count)
print(fib(10), fib.call_count)
print(fib(20), fib.call_count)
print(fib(30), fib.call_count)
