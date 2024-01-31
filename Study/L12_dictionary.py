states = {
    "NSW": "New South Wales",
    "VIC": "Victoria",
    "QLD": "Queensland",
    "WA": "Western Australia",
    "SA": "South Australia",
    "TAS": "Tasmania",
}

print(len(states))
print("WA" in states)
print("haha" in states)

print()

print(states["WA"])
try:
    print(states["tank"])
except KeyError:
    print('key error when print(states["tank"])')

word = states.get("tank", "😡")
print(word)

print()

spiders = {
    "smeringopus": {"name": "Pale Daddy Long-leg", "length": 7},
    "holocnemus pluchei": {"name": "Marbled cellar spider", "length": (5, 7)},
}

insects = {"spiders": 8, "centipedes": 100, "bees": 6}

print("print insects:")
for name in insects:
    print(insects[name])
