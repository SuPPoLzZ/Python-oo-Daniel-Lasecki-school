class SuperHero:
    def __init__(self, name: str, power: str):
        self._name = name
        self._power = power

    def get_name(self):
        return self._name

    def get_power(self):
        return self._power


class SuperGroup(SuperHero):
    def __init__(self, name: str, location: str):
        super().__init__(name, "")
        self._location = location
        self._members = []

    def get_name(self):
        return self._name

    def get_location(self):
        return self._location

    def add_member(self, hero: SuperHero):
        self._members.append(hero)

    def print_group(self):
        print(f"Group Name: {self._name}")
        print(f"Location: {self._location}")
        print("Members:")
        for member in self._members:
            print(f" - Name: {member.get_name()}, Power: {member.get_power()}")


superperson = SuperHero("SuperPerson", "Superspeed, superstrength")
invisible = SuperHero("Invisible Inca", "Invisibility")
revengers = SuperGroup("Revengers", "Emerald City")

revengers.add_member(superperson)
revengers.add_member(invisible)
revengers.print_group()
