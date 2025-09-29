from src.airplane import Airplane

class AirPortManagementSystem:
    def get_airplane_by_id(self, registration_number: str):
        for airplane in self.airplanes:
            if airplane.registration_number == registration_number:
                return airplane
        return None
    def remove_airplane(self, registration_number: str):
        self.airplanes = [a for a in self.airplanes if a.registration_number != registration_number]
    def __init__(self, airplanes: list[Airplane] = None):
        self.airplanes = airplanes if airplanes is not None else []

    def add_airplane(self, airplane: Airplane):
        self.airplanes.append(airplane)

    def get_airplanes(self):
        return self.airplanes