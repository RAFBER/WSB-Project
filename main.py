
from entities.rocket import Rocket
from people.student_engineer import StudentEngineer

def main():
    # Tworzenie obiektu rakiety
    rocket = Rocket(thrust_power=1000)
    # Ustawienie poziomu paliwa w rakiecie
    rocket.fuel_level = 60
    # Wywołanie sekwencji startowej
    rocket.launch_sequence()

    # Tworzenie obiektu studenta-inżyniera
    engineer = StudentEngineer(first_name="Rafał", last_name="Bertolassi", specialization="Astronautyka")
    # Wywołanie metody report_status(), używając MRO
    print(engineer.report_status())

# Punkt startowy programu
if __name__ == "__main__":
    main()