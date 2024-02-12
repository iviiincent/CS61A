class Product:

    def __init__(self, name, price, nutrition_info):
        self._name = name
        self._price = price
        self._nutrition_info = nutrition_info
        self._inventory = 0

    def get_label(self):
        return "Foxolate Store: " + self._name

    def increse_inventory(self, amount):
        self._inventory += amount

    def reduce_inventory(self, amount):
        if self._inventory < amount:
            print("Sold out!")
            return
        self._inventory -= amount

    def get_nutrition_label(self):
        return " | ".join(self._nutrition_info)

    def get_inventory_report(self):
        if self._inventory == 0:
            return "Sold out!"
        return f"We have {self._inventory} bars left."


pina_bar = Product("pina chocolate", 7.99, ["24 g sugar", "200 calories"])
