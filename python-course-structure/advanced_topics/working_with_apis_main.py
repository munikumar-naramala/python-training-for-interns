from fastapi import FastAPI
from typing import List
from working_with_apis_models import Car, UpdateCar

app = FastAPI()

db: List[Car] = [
    Car(
        id=1,
        brand='Lamborghini',
        model='Urus',
        horsepower=660,
        top_speed=250,
    ),
    Car(
        id=2,
        brand='BMW',
        model='M5',
        horsepower=600,
        top_speed=200,
    ),
]


@app.get("/")
async def root():
    return {"Hello": "World", }


@app.get("/api/v1/cars")
async def get_cars():
    return db


@app.post("/api/v1/cars")
async def create_cars(car: Car):
    db.append(car)
    return {"id": car.id}


@app.delete("/api/v1/cars/{id}")
async def delete_cars(id_2: int):
    for car in db:
        if car.id == id_2:
            db.remove(car)
        return


@app.put("/api/v1/cars/{id}")
async def update_cars(car_update: UpdateCar, id_1: int):
    for car in db:
        if car.id == id_1:
            if car_update.brand is not None:
                car.brand = car_update.brand
    if car_update.model is not None:
        car.model = car_update.model
    if car_update.horsepower is not None:
        car.horsepower = car_update.horsepower
    return car.id
