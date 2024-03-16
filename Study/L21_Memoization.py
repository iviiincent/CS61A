# Without memoization
def count_change1(amount, coins=(50, 25, 10, 5, 1)):
    if amount == 0:
        return 1
    elif len(coins) == 0 or amount < 0:
        return 0
    return count_change1(amount - coins[0], coins) + count_change1(amount, coins[1:])
    # choose coins[0] + do not choose coins[0], start with coins[1]


# With memoization
def count_change2(amount, coins=(50, 25, 10, 5, 1)):
    """
    >>> count_change(1)
    1
    >>> count_chang(5)
    2
    """

    # memo_table[amt][k] contains the value computed for
    # count_change(amt, k)
    memo_table = [[-1] * len(coins) for i in range(amount + 1)]

    def count_change(amount, coins):
        if amount < 0:
            return 0
        elif memo_table[amount][len(coins)] == -1:
            memo_table[amount][len(coins)] = full_count_change(amount, coins)
        return memo_table[amount][len(coins)]

    # Same as count_chang1(amount, coins)
    def full_count_change(amount, coins):
        if amount == 0:
            return 1
        elif len(coins) == 0 or amount < 0:
            return 0
        return full_count_change(amount - coins[0], coins) + full_count_change(
            amount, coins[1:]
        )


def fib(n):

    def fib(n):
        if n >= len(cache):
            cache[n] = fib(n - 1) + fib(n - 2)
        return cache[n]

    cache = [0, 1]
    return fib(n)
