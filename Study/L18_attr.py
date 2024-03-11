from typing import Any


class Light:
    def __init__(self, v) -> None:
        self.v = v

    def __getattribute__(self, name) -> Any:
        print(name)
        return super().__getattribute__(name)


class Item:
    def __init__(self, label) -> None:
        self.__label = label

    def __str__(self):
        return self.__label


item = Item("abc")
# print(item.__label)
print(item)
