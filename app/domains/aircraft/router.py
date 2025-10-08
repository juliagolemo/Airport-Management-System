from fastapi import APIRouter, Depends, status
from typing import List

from .schemas import AircraftCreate, AircraftOut, AircraftUpdate
from .repo import AircraftRepo, IN_MEMORY_DB
from .service import AircraftService

router = APIRouter(prefix="/aircraft", tags=["aircraft"])


def get_service() -> AircraftService:
	repo = AircraftRepo(IN_MEMORY_DB)
	return AircraftService(repo)


@router.get("/", response_model=List[AircraftOut])
def list_aircraft(service: AircraftService = Depends(get_service)):
	return service.list_aircraft()


@router.post("/", response_model=AircraftOut, status_code=status.HTTP_201_CREATED)
def create_aircraft(payload: AircraftCreate, service: AircraftService = Depends(get_service)):
	return service.create_aircraft(payload)


@router.get("/{aircraft_id}", response_model=AircraftOut)
def get_aircraft(aircraft_id: int, service: AircraftService = Depends(get_service)):
	return service.get_aircraft(aircraft_id)


@router.put("/{aircraft_id}", response_model=AircraftOut)
def update_aircraft(aircraft_id: int, payload: AircraftUpdate, service: AircraftService = Depends(get_service)):
	return service.update_aircraft(aircraft_id, payload)


@router.delete("/{aircraft_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_aircraft(aircraft_id: int, service: AircraftService = Depends(get_service)):
	service.delete_aircraft(aircraft_id)
	return None

