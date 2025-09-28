from src.airplane import Airplane
from src.passengers import Passengers

from src.airplane import Airplane
from src.employee import Pilot, Stewardessa, Mechanik, Sprzatacz

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
        Stewardessa("Anna Nowak", ["Polski", "Angielski", "Hiszpański"]),
        Mechanik("Piotr Zieliński", "mechanika lotnicza"),
        Sprzatacz("Maria Wiśniewska", "nocna zmiana")
    ]

    print("\nPracownicy lotniska:")
    for emp in employees:
        print(emp)

    # Passengers
    passengers = [
        Passengers("Julia Golemo", "AA1234567", "Polska"),
        Passengers("Carlos Ramirez", "BB9876543", "Hiszpania"),
        Passengers("Emily Smith", "CC1928374", "Wielka Brytania")
    ]

    print("\nLista pasażerów:")
    for passenger in passengers:
        print(passenger)

if __name__ == "__main__":
    main()
