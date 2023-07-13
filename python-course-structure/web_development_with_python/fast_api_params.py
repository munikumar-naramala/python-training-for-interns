from fastapi import FastAPI

app = FastAPI()

cars = {
    1: {
        'BMW': 'M5'
    }
}


@app.get("/cars/{car_id}")
async def read_car(car_id: int):
    return {"car_id": car_id}


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}
