from fastapi import FastAPI
from models import Gender, Role, User
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()


class UpdateUser(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    roles: Optional[List[Role]]


db: List[User] = [
    User(
        id=1,
        first_name="Bhavana",
        last_name="V",
        gender=Gender.female,
        roles=[Role.user],
    ),
    User(
        id=2,
        first_name="Meghana",
        last_name="V",
        gender=Gender.female,
        roles=[Role.user],
    ),
    User(
        id=3,
        first_name="Abhinav",
        last_name="C",
        gender=Gender.male,
        roles=[Role.user],
    ),
    User(
        id=4,
        first_name="Prakash",
        last_name="V",
        gender=Gender.male,
        roles=[Role.admin, Role.user],
    ),
]


@app.get("/")
async def root():
    return {"Hello": "World", }


@app.get("/api/v1/users")
async def get_users():
    return db


@app.post("/api/v1/users")
async def create_user(user: User):
    db.append(user)
    return {"id": user.id}


@app.delete("/api/v1/users/{id}")
async def delete_user(id_2: int):
    for user in db:
        if user.id == id_2:
            db.remove(user)
        return


@app.put("/api/v1/users/{id}")
async def update_user(user_update: UpdateUser, id_1: int):
    for user in db:
        if user.id == id_1:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
    if user_update.last_name is not None:
        user.last_name = user_update.last_name
    if user_update.roles is not None:
        user.roles = user_update.roles
    return user.id
