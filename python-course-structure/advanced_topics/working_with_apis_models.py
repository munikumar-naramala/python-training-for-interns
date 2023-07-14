from typing import Optional
from pydantic import BaseModel


class Car(BaseModel):
    id: int
    brand: str
    model: str
    horsepower: int
    top_speed: int


class UpdateCar(BaseModel):
    brand: Optional[str]
    model: Optional[str]
    horsepower: Optional[int]
    top_speed: Optional[int]
