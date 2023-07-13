from typing import Union

from fastapi import FastAPI

app = FastAPI()

Cars = {
    'Porsche': "911 Carreras",
    'Ferrari': 'f40',
    'BMW': 'M5 competition',
    'Aston Martin': 'Ventura'
}


@app.get("/cars/{car_name}")
async def read_item(car_name: str, q: Union[str, None] = None):
    if q:
        return {"car_name": car_name, "q": q}
    return {"car_name": car_name}

# http://127.0.0.1:8000/items/ere?q=23
