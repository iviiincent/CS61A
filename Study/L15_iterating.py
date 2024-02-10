# list
my_order = ["Pizza", "Beef", "Cola", "Flat White Coffe"]
for item in my_order:
    print(item)
lowered = [item.lower() for item in my_order]

print()

# dictionary
prices = {"pineapple": 9.99, "pen": 2.99, "pineapple-pen": 19.99}
for product in prices:
    print(product, "costs", prices[product])
discounted = {item: round(prices[item] * 0.75, 2) for item in prices}

print()
print("discounted:")
print(discounted)

print()
# iter
print("iterator:")
it = iter(my_order)

try:
    while True:
        print(next(it))
except:
    print()
