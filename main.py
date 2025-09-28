from fastapi import FastAPI
from src.airplane import Airplane
from src.airport_management_system import AirPortManagementSystem
from fastapi import Request
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
	app.state.airport_system = AirPortManagementSystem()
	yield

app = FastAPI(lifespan=lifespan)



@app.post("/airplanes")
def add_airplane(airplane: Airplane, request: Request):
	request.app.state.airport_system.add_airplane(airplane)
	return {"message": "Samolot dodany", "airplane": airplane}


@app.get("/airplanes")
def get_airplanes(request: Request):
    airplanes = request.app.state.airport_system.get_airplanes()
    return [
        {
            "model": a.model,
            "capacity": a.capacity,
            "registration_number": a.registration_number
        } for a in airplanes
    ]
