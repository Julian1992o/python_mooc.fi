# Write your solution here:
class Item:
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight

    def name(self):
        return self.__name
    
    def weight(self):
        return self.__weight
    
    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"
    
class Suitcase:
    def __init__(self, max_weight: int):
        self.max_weight = max_weight
        self.total_weight = 0
        self.items = []

    def add_item(self, item: Item):
        if (self.total_weight + item.weight()) < self.max_weight:
            self.items.append(item)
            self.total_weight += item.weight()

    def __str__(self):
        i = "item"
        if len(self.items) == 0 or len(self.items) > 1:
            i = "items"

        return f"{len(self.items)} {i} ({self.total_weight} kg)"
    
    def print_items(self):
        for item in self.items:
            print(item)

    def weight(self):
        return self.total_weight
    
    def heaviest_item(self):
        if len(self.items) == 0:
            return None
        heaviest = None
        heaviest_weight = 0
        for item in self.items:
            if item.weight() > heaviest_weight:
                heaviest = item
                heaviest_weight = item.weight()
        return heaviest
    
class CargoHold:
    def __init__(self, max_weight: int):
        self.max_weight = max_weight
        self.suitcases = []
        self.current_weight = 0

    def add_suitcase(self, suitcase: Suitcase):
        if (self.current_weight + suitcase.weight()) < self.max_weight:
            self.suitcases.append(suitcase)
            self.current_weight += suitcase.weight()
    
    def __str__(self):
        i = "suitcase"
        if len(self.suitcases) == 0 or len(self.suitcases) > 1:
            i = "suitcases"
        return f"{len(self.suitcases)} {i}, space for {self.max_weight - self.current_weight} kg"
    
    def print_items(self):
        for suitcase in self.suitcases:
            suitcase.print_items()
        


if __name__ == "__main__":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()