from typing import List

from fastapi import HTTPException, status

from .repo import AircraftRepo
from .schemas import AircraftCreate, AircraftUpdate


class AircraftService:
	def __init__(self, repo: AircraftRepo):
		self.repo = repo

	def list_aircraft(self) -> List[dict]:
		return self.repo.list()

	def get_aircraft(self, aircraft_id: int) -> dict:
		item = self.repo.get(aircraft_id)
		if not item:
			raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aircraft not found")
		return item

	def create_aircraft(self, payload: AircraftCreate) -> dict:
		data = payload.dict()
		return self.repo.create(data)

	def update_aircraft(self, aircraft_id: int, payload: AircraftUpdate) -> dict:
		updated = self.repo.update(aircraft_id, payload.dict())
		if not updated:
			raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aircraft not found")
		return updated

	def delete_aircraft(self, aircraft_id: int) -> None:
		ok = self.repo.delete(aircraft_id)
		if not ok:
			raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aircraft not found")

