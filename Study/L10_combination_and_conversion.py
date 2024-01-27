A = [1, 2, 3, 4]
B = [7, 8, 9]

# combination
print("combination")
print(A + B)
print(A[1:3] + B[1:])
print("Hello," + " " + "world!")

try:
    print((1, 2, 3, 4) + 3)
except TypeError:
    print("TypeError")

print()


# conversion
print("conversion")
print(A, (tuple)(A))
print(list(range(0, 8)), tuple(list(range(0, 8))))
print(list("abcd"), tuple("abcd"))
