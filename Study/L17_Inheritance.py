# class Food(object)
class Food:

    def __init__(self, name, type, calories):
        self.name = name
        self.type = type
        self.calories = calories


# class Animal(object)
class Animal:
    species_name = "Animal"
    scientific_name = "Animalia"
    play_multiplier = 2
    interact_increment = 1

    def __init__(self, name, age=0) -> None:
        self.name = name
        self.age = age
        self.calories_eaten = 0
        self.happiness = 0

    def play(self, num_hours):
        self.happiness += num_hours * self.play_multiplier
        print(f"Play for {num_hours} hours.")

    def eat(self, food):
        self.calories_eaten += food.calories
        print(f"Eat {food.name}.")
        if self.calories_eaten > self.calories_needed:
            self.happiness -= 1
            print(f"{self.name} is full!")

    def interact_with(self, animal2):
        if animal2.species_name == "Giant Panda":
            print(f"{self.name} meats a panda which is solitary.")
            return
        self.happiness += self.interact_increment
        print(f"{self.name} has happy time with {animal2.name}.")

    def mate_with(self, animal2):
        if animal2 is not self and animal2.species_name == self.species_name:
            self.mate = animal2
            animal2.mate = self


class Herbivore(Animal):

    def eat(self, food):
        if food.type == "meat":
            self.happiness -= 5
        else:
            super().eat(food)


class Carnivore(Animal):

    def eat(self, food):
        if food.type == "meat":
            super().eat(food)
        else:
            self.happiness -= 5


class Elephant(Carnivore):
    species_name = "African Savanna Elephant"
    scientific_name = "Loxodonta africana"
    calories_needed = 8000
    play_multiplier = 4

    # super in __init__
    def __init__(self, name, age=0) -> None:
        super().__init__(name, age)
        if age < 1:
            self.calories_needed = 1000
        elif age < 5:
            self.calories_needed = 3000


class Rabbit(Carnivore):
    species_name = "European rabbit"
    scientific_name = "Oryctolagus cuniculus"
    calories_needed = 200
    play_multiplier = 8
    interact_increment = 2


# Simplest
class Human(Animal):
    pass


# Override
class Panda(Herbivore):
    species_name = "Giant Panda"
    scientific_name = "Ailuropoda melanoleuca"
    calories_needed = 6000

    def interact_with(self, animal2):
        self.happiness -= 1
        print(f"I'm a Panda. I'm solitary, go away, {animal2.name}.")


# super()
class Lion(Carnivore):
    species_name = "Lion"
    scientific_name = "Panthera"
    calories_needed = 3000

    def eat(self, food):
        """Only eat food which is meat."""
        if food.type == "meat":
            # Animal.eat(food)
            # super() is Animal
            super().eat(food)


def partytime(animals):
    for i in range(len(animals)):
        for j in range(i + 1, len(animals)):
            animals[i].interact_with(animals[j])


jane = Rabbit("Jane", 2)
scar = Lion("Scar", 12)
elly = Elephant("Elly", 5)
pandy = Panda("PandeyBear", 4)

animals = [jane, scar, elly, pandy]
partytime(animals)
