# FastAPI
 - Framework w Pythonie do tworzenia API.
- Wykorzystuje dekoratory (@app.get(), @app.post() itd.) do definiowania endpointów.
- Automatycznie generuje walidację danych (na podstawie pydantic)

# uvicorn
```
uvicorn
```
- To serwer ASGI (Asynchronous Server Gateway Interface).

- Odpowiada za uruchomienie aplikacji FastAPI i obsługę żądań HTTP.

 - FastAPI to tylko logika, a uvicorn = „silnik”, który to uruchamia

 ## Jak odpalać API
 1. Zapisz plik, np. ```main.py```
 
 ```python
 from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"msg": "Hello World"}
```
2. Odpal serwer:
```python
uvicorn main:app --reload
```
## Jak testować za pomocą docs? ("docs" - opis jak coś działa)
Po uruchomieniu aplikacji wejdź w przeglądarce na:

 - Swagger UI: http://127.0.0.1:8000/docs

 - ReDoc: http://127.0.0.1:8000/redoc

Możesz tam:

- Wywoływać endpointy (GET, POST itd.) bez pisania klienta.

- Sprawdzać struktury JSON i wymagane parametry.