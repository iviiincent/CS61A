class Lamb:
    species_name = "Lamb"
    scientific_name = "Ovis aries"

    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"🐑 {self.name}"


class Human:
    species_name = "Human"
    scientific_name = "Homo sapiens"

    def __init__(self, name, pet=None) -> None:
        self.name = name
        self.pet = pet

    def adopt(self, pet):
        self.pet = pet


lamb = Lamb("lamb")
mary = Human("Mary", lamb)
print(str(lamb))
