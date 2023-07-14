from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


class Cars(BaseModel):
    name: str
    model: Union[str, None] = None
    horsepower: int
    top_speed: float


app = FastAPI()


@app.put("/cars/{car_id}")
async def create_item(car_id: int, car: Cars):
    return {"car_id": car_id, **car}
