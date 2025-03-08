
# Importujemy klasę bazową SpaceVehicleBase z pliku .space_vehicle_base 
from .space_vehicle_base import SpaceVehicleBase

# Importujemy stałą LAUNCH_CODE z pliku utilities.constants w folderze utyliites
from utilities.constants import LAUNCH_CODE

# Tworzymy klasę reprezentujacą rakietę, dziedzicząca po SpaceVehicleBase
class Rocket(SpaceVehicleBase):
    def __init__(self, thrust_power):
        # Zmienna prywatna do przechowywania poziomu paliwa
        self._fuel_level = 0
        # Zmienna publiczna do przechowywania mocy ciągu
        self.thrust_power = thrust_power
        
    # Getter dla zmiennej prywatnej _fuel_level
    @property
    def fuel_level(self):
        return self._fuel_level
    
    # Setter dla zmiennej prywatnej _fuel_level
    @fuel_level.setter
    def fuel_level(self, value):
        # Sprawdzenie, czy poziom paliwa nie jest ujemny
        if value < 0:
            raise ValueError("Poziom paliwa nie może być ujemny!")
        self._fuel_level = value
        
    # Implementacja metody abstrakcyjnej launch_sequence #
    def launch_sequence(self):
        # Sprawdzenie, czy poziom paliwa jest wystarczający
        if self._fuel_level > 50:
            # Wypisanie komunikatu o rozpoczęciu sekwencji startowej
            print(f"Rozpoczynamy sekwencję startową! Kod startowy: {LAUNCH_CODE}")
            print(f"Thrust power: {self.thrust_power}")
        else:
            # Wypisanie ostrzeżenia o niewystarczającym paliwie
            print("Niewystarczający poziom paliwa do startu!")