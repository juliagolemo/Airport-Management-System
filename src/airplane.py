from pydantic import BaseModel

class Airplane(BaseModel):
    model: str
    capacity: int
    registration_number: str