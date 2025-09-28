from src.airplane import Airplane

class AirPortManagementSystem:
    def __init__(self, airplanes: list[Airplane] = None):
        self.airplanes = airplanes if airplanes is not None else []

    def add_airplane(self, airplane: Airplane):
        self.airplanes.append(airplane)

    def get_airplanes(self):
        return self.airplanes