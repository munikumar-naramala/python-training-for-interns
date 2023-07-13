from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


class Cars(BaseModel):
    name: str
    model: Union[str, None] = None
    horses: float
    top_speed: Union[float, None] = None


cars = {
    'Porsche': "911 Carreras",
    'Ferrari': 'f40',
    'BMW': 'M5 competition',
    'Aston Martin': 'Ventura'

}

app = FastAPI()


@app.post("/cars/{car_name}")
async def create_car(car_name: str, car: cars):
    if car_name in Cars:
        return {'error': 'car exists'}
    cars[car_name] = car
    return cars[car_name]


@app.get("/cars/{car_name}")
async def read_file(car_name: str):
    try:
        return {"file_path": car_name}
    except BaseException as error:
        print('there is an exception: {}'.format(error))
