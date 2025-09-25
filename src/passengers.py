class Passengers:
     def __init__(self, name: str, passport_number: str, nationality: str):
         self.name = name
         self.passport_number = passport_number
         self.nationality = nationality

     def __str__(self):
         return f"{self.name} ({self.nationality}), Passport: {self.passport_number}"
