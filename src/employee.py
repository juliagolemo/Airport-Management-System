class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def __str__(self):
        return f"{self.position}: {self.name}"


class Pilot(Employee):
    def __init__(self, name, license_number):
        super().__init__(name, "Pilot")
        self.license_number = license_number

    def __str__(self):
        return f"{self.position}: {self.name}, Licencja: {self.license_number}"


class Stewardessa(Employee):
    def __init__(self, name, languages):
        super().__init__(name, "Stewardessa")
        self.languages = languages

    def __str__(self):
        langs = ", ".join(self.languages)
        return f"{self.position}: {self.name}, Języki: {langs}"
class Mechanik(Employee):
    def __init__(self, name, specjalizacja):
        super().__init__(name, "Mechanik")
        self.specjalizacja = specjalizacja

    def __str__(self):
        return f"{self.position}: {self.name}, Specjalizacja: {self.specjalizacja}"

class Sprzatacz(Employee):
    def __init__(self, name, zmiana):
        super().__init__(name, "Sprzątacz")
        self.zmiana = zmiana

    def __str__(self):
        return f"{self.position}: {self.name}, Zmiana: {self.zmiana}"