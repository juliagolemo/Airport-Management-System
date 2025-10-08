from fastapi import FastAPI

from domains.aircraft.router import router as aircraft_router

app = FastAPI()

app.include_router(aircraft_router)

@app.get("/health")
def health():
	return {"status": "ok"}

