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

nums = [1, 2, 3]
eng_nums = ["one", "two", "three"]
cn_nums = ["一", "二", "三"]


def nums_gen():
    yield from nums
    yield from eng_nums
    yield from cn_nums


def nums_zip():
    return zip(nums, eng_nums, cn_nums)


print(list(nums_gen()))

print()

for num in nums_zip():
    print(num)
