from src.airplane import Airplane

def main():
    # Tworzenie przykładowych samolotów
    airplanes = [
        Airplane("Boeing 737", 180, "SP-ABC"),
        Airplane("Airbus A320", 150, "SP-DEF"),
        Airplane("Embraer E190", 100, "SP-GHI")
    ]

    print("System uruchamiania samolotów:")
    for airplane in airplanes:
        print(f"Model: {airplane.model}, Pojemność: {airplane.capacity}, Rejestracja: {airplane.registration_number}")

if __name__ == "__main__":
    main()

from src.airplane import Airplane
from src.employee import Pilot, Stewardessa

def main():
    # Samoloty
    airplanes = [
        Airplane("Boeing 737", 180, "SP-ABC"),
        Airplane("Airbus A320", 150, "SP-DEF"),
        Airplane("Embraer E190", 100, "SP-GHI")
    ]

    print("System uruchamiania samolotów:")
    for airplane in airplanes:
        print(f"Model: {airplane.model}, Pojemność: {airplane.capacity}, Rejestracja: {airplane.registration_number}")

    # Pracownicy
    employees = [
        Pilot("Jan Kowalski", "PL12345"),
        Stewardessa("Anna Nowak", ["Polski", "Angielski", "Hiszpański"])
    ]

    print("\nPracownicy lotniska:")
    for emp in employees:
        print(emp)

if __name__ == "__main__":
    main()
