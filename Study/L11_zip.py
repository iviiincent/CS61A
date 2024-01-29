L = list(zip([1, 2, 5, 3], [9, 2, 6, 3, 10]))
print(L)

L = list(zip([1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9, 12, 15]))
print(L)
# Length of result is that of shortest sequence

print()

print("animals")
animals = ["lion", "dog", "owl", "pig"]
for n, animal in zip(range(1, len(animals) + 1), animals):
    print(n, animal)

# what zip return is generator
