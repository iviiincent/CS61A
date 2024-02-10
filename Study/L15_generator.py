def evens():
    num = 0
    print("hi")
    while num < 10:
        yield num
        num += 2


even_gen = evens()
try:
    while True:
        print(next(even_gen))
except:
    print("Stop generating")

print()


def evens(start, end):
    num = start + (start % 2)
    while num < end:
        yield num
        num += 2


for num in evens(9, 19):
    print(num)

print()

cn_nums = ["yi", "er", "san"]
eng_nums = ["one", "two", "three"]
nums = [1, 2, 3]


def nums_gen():
    yield from cn_nums
    yield from eng_nums
    yield from nums


def nums_zip():
    return zip(cn_nums, eng_nums, nums)


print(list(nums_gen()))

print()

for num in nums_zip():
    print(num)
