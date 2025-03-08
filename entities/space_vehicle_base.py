
# Import modułu do tworzenia klas abstrakcyjnych
from abc import ABC, abstractmethod 

# Definiujemy klasę abstrakcyjną, która definiuje bazowy interfejs dla pojazdów kosmicznych
class SpaceVehicleBase(ABC):
    @abstractmethod
    def launch_sequence(self):
        """Metoda abstrakcyjna, którą muszą zaimplementować klasy dziedziczące.
        Służy do uruchomienia sekwencji startowej rakiety."""
        pass
    
    