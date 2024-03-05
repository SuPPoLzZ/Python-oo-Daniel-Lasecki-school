class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height


class Room:
    def __init__(self):
        self.persons = []

    def add(self, person: Person):
        self.persons.append(person)

    def is_empty(self):
        return len(self.persons) == 0
    
    def print_contents(self):
        if self.is_empty():
            print("The room is empty")
        else:
            total_height = sum(person.height for person in self.persons)
            print(f"There are {len(self.persons)} persons in the room, and their combined height is {total_height} cm")
            for person in self.persons:
                print(f"{person.name} ({person.height} cm)")

    def shortest(self):
        if self.persons:
            shortest_person = min(self.persons, key=lambda x: x.height)
            return shortest_person  # Return the shortest person object
        else:
            return None
        
    def remove_shortest(self):
        shortest_person = self.shortest()
        if shortest_person:
            self.persons.remove(shortest_person)
            return shortest_person
        else:
            return None


room = Room()

print("Is the room empty?", room.is_empty())
print("Shortest:", room.shortest())

room.add(Person("Lea", 183))
room.add(Person("Kenya", 172))
room.add(Person("Nina", 162))
room.add(Person("Ally", 166))

print()

print("Is the room empty?", room.is_empty())
print("Shortest:", room.shortest())

print()

removed = room.remove_shortest()
if removed:
    print(f"Removed from room: {removed.name}")

print()

room.print_contents()
