
from .person import Person
from utilities.mission_member import MissionMember

# Klasa reprezentująca studenta-inżyniera, dziedzicząca po Person i MissionMember
class StudentEngineer(Person, MissionMember):
    def __init__(self, first_name, last_name, specialization):
        # Wywołanie konstruktora klasy bazowej (Person)
        super().__init__(first_name, last_name)
        # Specjalizacja studenta
        self.specialization = specialization