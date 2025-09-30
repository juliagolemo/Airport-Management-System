# Airport-Management-System – FastAPI
# Co to jest FastAPI?

FastAPI to szybki framework do tworzenia API w Pythonie. Daje automatyczną dokumentację (/docs) i proste budowanie endpointów (GET, POST, DELETE).

# Start
```
pip install fastapi uvicorn
uvicorn main:app --reload
```

## Endpointy
**POST** /airplanes

Dodaje nowy samolot.
Body (JSON):
```
{
  "model": "Boeing 737",
  "capacity": 180,
  "registration_number": "SP-ABC"
}
```
**GET /airplanes**

Zwraca listę wszystkich samolotów.

```
GET /airplanes/{registration_number}
```

Zwraca dane samolotu o podanym numerze rejestracyjnym.

**DELETE** /airplanes
```
DELETE /airplanes/{registration_number}
```
Usuwa samolot o podanym numerze rejestracyjnym.

# Struktura projektu
**main.py** – aplikacja FastAPI z endpointami

**airplane.py** – model danych (Pydantic)

**airport_management_system.py** – logika zarządzania samolotami