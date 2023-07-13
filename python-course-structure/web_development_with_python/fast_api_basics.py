from fastapi import FastAPI
from typing import Optional

app = FastAPI()

cars = {
    1: {
        'brand': 'Lamborghini',
        'model': 'huracan',
        'horsepower': 630
    }
}


@app.get('/')
async def index():
    return {'message': "first_data"}


@app.get('/get_car/{car_id}')
async def get_car(car_id: int):
    return cars[car_id]


@app.get('/get_by_name')
async def get_car_name(brand: Optional[str] = None):
    for car_id in cars:
        if cars[car_id]['brand'] == brand:
            return [cars][car_id]
    return {"Data": "Not Found"}


@app.get('/get_by_name/{brand}')
async def get_car_name(brand: Optional[str] = None):
    for car_id in cars:
        if cars[car_id] == brand:
            return [cars][car_id]
    return {"Data": "Not Found"}
