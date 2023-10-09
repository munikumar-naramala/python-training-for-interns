from fastapi import APIRouter, HTTPException, Query
from schemas.request import RestaurantRequest, RestaurantUpdateRequest
from schemas.response import response
from models.models import Restaurant
from db.database import Database
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import and_, desc
import uuid
from pydantic import BaseModel
from datetime import datetime, timedelta
from jose import jwt
from static.send_mail import send_email

router = APIRouter(
    prefix="/restaurants",
    tags=["Restaurant"],
    responses={404: {"description": "Not found"}},
)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

database = Database()
engine = database.get_db_connection()


class Token(BaseModel):
    access_token: str
    token_type: str


SECRET_KEY = '867b6d70449e152a6d3363c1c6f35430bca7359ffd6128504e8f6710c48614af'
ALGORITHM = "HS256"


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


@router.post("/register_restaurant", response_description="Add a restaurant")
async def add_restaurant(restaurant_req: RestaurantRequest):
    new_restaurant = Restaurant()
    new_restaurant.restaurant_id = str(uuid.uuid4())
    new_restaurant.restaurant_name = restaurant_req.restaurant_name
    new_restaurant.address = restaurant_req.address
    new_restaurant.phone = restaurant_req.phone
    new_restaurant.email = restaurant_req.email
    new_restaurant.opening_hours = restaurant_req.opening_hours
    new_restaurant.description = restaurant_req.description
    new_restaurant.rating = restaurant_req.rating
    new_restaurant.created_by = restaurant_req.created_by
    session = database.get_db_session(engine)
    session.add(new_restaurant)
    session.flush()

    session.refresh(new_restaurant, attribute_names=['restaurant_id'])
    data = {"restaurant_id": new_restaurant.restaurant_id}
    session.commit()
    subject = "Registration Successful"
    message = f"Hello {new_restaurant.restaurant_name},\n\nYour have successfully registered your restaurant."
    send_email(subject, message, new_restaurant.email)
    session.close()
    return response(data, 200, "Restaurant added successfully.", False)


@router.post("/login")
def login(email: str):
    session = database.get_db_session(engine)
    restaurant = session.query(Restaurant).filter_by(email=email).first()
    if restaurant is None or restaurant.email != email:
        raise HTTPException(status_code=401, detail="Invalid restaurant user")
    session.flush()
    session.commit()
    session.close()

    data = {
        'info': 'secret information',
        'from': 'GFG'
    }
    token = create_access_token(data=data)
    return {'token': token, 'login status: ': 'success'}


@router.put("/update_restaurant/{restaurant_id}")
async def update_restaurant(restaurant_update_req: RestaurantUpdateRequest, restaurant_id: str):
    session = database.get_db_session(engine)
    try:
        is_restaurant_updated = session.query(Restaurant).filter(Restaurant.restaurant_id == restaurant_id).update({
            Restaurant.restaurant_name: restaurant_update_req.restaurant_name,
            Restaurant.description: restaurant_update_req.description,
            Restaurant.rating: restaurant_update_req.rating
        }, synchronize_session=False)
        session.flush()
        session.commit()
        response_msg = "Restaurant details updated successfully"
        response_code = 200
        error = False
        if is_restaurant_updated == 1:
            data = session.query(Restaurant).filter(
                Restaurant.restaurant_id == restaurant_id).one()

        elif is_restaurant_updated == 0:
            response_msg = "Restaurant not updated. No restaurant found with this id :" + \
                           str(restaurant_id)
            error = True
            data = None
        return response(data, response_code, response_msg, error)
    except Exception as ex:
        print("Error : ", ex)


@router.get("/search")
def search_restaurant(query: str = Query(..., description="Search cuisine")):
    results = []
    session = database.get_db_session(engine)
    data = session.query(Restaurant).all()

    for item in data:
        if query.lower() in item.description.lower():
            results.append(item)

    return {"results": results}


@router.get("/search_location")
def search_restaurant_location(query: str = Query(..., description="Search location")):
    results = []
    session = database.get_db_session(engine)
    data = session.query(Restaurant).all()

    for item in data:
        if query.lower() in item.address.lower():
            results.append(item)

    return {"results": results}


@router.get("/{restaurant_id}")
async def read_restaurant(restaurant_id: str):
    session = database.get_db_session(engine)
    response_message = "Restaurant retrieved successfully"
    data = None
    try:
        data = session.query(Restaurant).filter(
            and_(Restaurant.restaurant_id == restaurant_id)).one()
    except Exception as ex:
        print("Error", ex)
        response_message = "Restaurant Not found"
    error = False
    return response(data, 200, response_message, error)


@router.get("/")
async def read_all_restaurants():
    session = database.get_db_session(engine)
    data = session.query(Restaurant).order_by(
        desc(Restaurant.rating)).all()
    return response(data, 200, "Restaurants retrieved successfully.", False)
