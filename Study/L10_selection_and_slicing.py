t = (2, 0, 9, 10, 11)
L = [2, 0, 9, 10, 11]
R = range(2, 13)
E = range(2, 13, 2)
S = "Hello, world!"

# selection
print("selection")
print(t[2], L[2], R[2], E[2])
print(t[-1], t[len(t) - 1])
print(S[1])
print()


# slicing
print("slicing")
print(t[1:4], (t[1], t[2], t[3]))
print(t[2:], t[2 : len(t)])
print(t[::2], t[0 : len(t) : 2], (t[0], t[2], t[4]))
print(t[::-1], (t[4], t[3], t[2], t[1], t[0]))
print(S[0:5])
print(S[0:5:2])
print(S[4::-1])
print(S[1:2], S[1])
