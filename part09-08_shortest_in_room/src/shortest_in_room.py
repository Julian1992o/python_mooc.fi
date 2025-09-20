# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return f"{self.name} ({self.height} cm)"
    
class Room:
    def __init__(self):
        self.persons = []
        self.total_height = 0

    def add(self, person: Person):
        self.persons.append(person)
        self.total_height += person.height

    def is_empty(self):
        if len(self.persons) == 0:
            return True
        return False

    def print_contents(self):
        print(f"There are {len(self.persons)} persons in the room, and their combined height is {self.total_height} cm")
        for person in self.persons:
            print(person)

    def shortest(self):
        shortest_name = ""
        shortest_height = 500


        if len(self.persons) == 0:
            return None
        for person in self.persons:
            if person.height < shortest_height:
                shortest_height = person.height
                shortest_name = person
        return shortest_name
    
    def remove_shortest(self):
        if len(self.persons) == 0:
            return None
        shortest = self.shortest()
        self.persons.remove(self.shortest())
        self.total_height -= shortest.height
        return shortest
        
    
if __name__ == "__main__":
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()