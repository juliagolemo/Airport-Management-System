from typing import Optional

from pydantic import BaseModel


class AircraftBase(BaseModel):
	registration: str
	model: str
	seats: int


class AircraftCreate(AircraftBase):
	pass


class AircraftUpdate(BaseModel):
	registration: Optional[str] = None
	model: Optional[str] = None
	seats: Optional[int] = None


class AircraftOut(AircraftBase):
	id: int

