class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

class Covid5GPerson():
    def __init__(self, first, last, chip, bat_dna):
        self.first = first
        self.last = last
        self.chip = chip
        self.bat_dna = bat_dna
        print(".Covid5GPerson__init__()")


class FullnamePerson(Person):
    def __init__(self, first, last):
        print("FullnamePerson.__init__()")
        super().__init__(first, last)
        self.fullname = f'{self.first} {self.last}'
        print("FullnamePerson.__init__()")

class AbbrevPerson(Person, Covid5GPerson):
    def __init__(self, first, last):
        print("AbbrevPerson.__init__()")
        super().__init__(first, last)
        self.abbrev = f'{self.first[0]} {self.last[0]}'
        print("AbbrevPerson.__init__()")

class RealPerson(FullnamePerson, AbbrevPerson):
    def __init__(self, first, last, chip, bat_dna):
        chip = chip
        bat_dna = bat_dna
        self.chip = chip
        self.bat_dna = bat_dna
        print("RealPerson.__init__()")
        super().__init__(first, last, chip, bat_dna)
        print("RealPerson.__init__()")

print(RealPerson.mro())
real_person = RealPerson("Baby", "Groggo", chip, bat_dna)
print('----------------')
print(real_person.first)
print('fasef')
print(real_person.last)
print(real_person.fullname)
print(real_person.abbrev)

class Human1:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class FullnamePerson1(Human1):
    def __init__(self, first, last):
        print("FullnamePerson1.__init__()")
        super().__init__(first, last)
        self.fullname = f'{self.first} {self.last}'
        print("FullnamePerson1.__init__()")

class AbbrevPerson1(Human1):
    def __init__(self, first, last):
        print("AbbrevPerson1.__init__()")
        super().__init__(first, last)
        self.abbrev = f'{self.first[0]} {self.last[0]}'
        print("AbbrevPerson1.__init__()")

class RealPerson1(FullnamePerson1, AbbrevPerson1):
    def __init__(self, first, last):
        print("RealPerson1.__init__()")
        super().__init__(first, last)
        print("RealPerson1.__init__()")

print(RealPerson1.mro())
real_person = RealPerson1("Stepan", "Kravchenko")
print('----------------')
print(real_person.first)
print('fasef')
print(real_person.last)
print(real_person.fullname)
print(real_person.abbrev)
