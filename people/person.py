
# Klasa reprezentująca osobę związaną z misją
class Person:
    def __init__(self, first_name, last_name):
        # Inicjalizacja imienia i nazwiska
        self.first_name = first_name
        self.last_name = last_name

    # Metoda zgłaszająca gotowość osoby
    def report_status(self):
        return f"{self.first_name} {self.last_name} zgłasza gotowość!"