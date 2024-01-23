# summation function

def summation(n, term, next):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), next(k)
    return total

# 1

def cube(k):
    return pow(k, 3)

def successor(k):
    return k + 1

def sum_cubes(n):
    return summation(n, cube, successor)

print(sum_cubes(3)) # 1 + 8 + 27 = 36

# 2

def identity(k):
    return k

def sum_naturals(n):
    return summation(n, identity, successor)

print(sum_naturals(10)) # 1 + 2 + ... + 10 = 55

# 3

def pi_term(k):
    return 8 / (k * (k + 2))

def pi_next(k):
    return k + 4

def pi_sum(n):
    return summation(n, pi_term, pi_next)

print(pi_sum(1e6)) # 3.1415906535898936