import uuid
from fastapi import APIRouter
from schemas.request import RentRequest
from schemas.response import response
from db.database import Database
from sqlalchemy import and_, desc
from models.models import Rent

router = APIRouter(
    prefix="/rent",
    tags=["Rent"],
    responses={404: {"description": "Not found"}},
)

database = Database()
engine = database.get_db_connection()


@router.post("/add_rent", response_description="Add a rent")
async def add_rent(rent_req: RentRequest):
    new_rent = Rent()
    new_rent.rent_id = str(uuid.uuid4())
    new_rent.user_id = rent_req.user_id
    new_rent.vehicle_id = rent_req.vehicle_id
    new_rent.duration = rent_req.duration
    new_rent.start_date = rent_req.start_date
    session = database.get_db_session(engine)
    session.add(new_rent)
    session.flush()

    session.refresh(new_rent, attribute_names=['rent_id'])
    data = {"rent_id": new_rent.rent_id}
    session.commit()
    session.close()
    return response(data, 200, "Rent added successfully.", False)


@router.get("/{rent_id}")
async def read_rent(rent_id: str):
    session = database.get_db_session(engine)
    response_message = "Rent retrieved successfully"
    data = None
    try:
        data = session.query(Rent).filter(
            and_(Rent.rent_id == rent_id)).one()
    except Exception as ex:
        print("Error", ex)
        response_message = "Rent Not found"
    error = False
    return response(data, 200, response_message, error)


@router.get("/")
async def read_all_rents():
    session = database.get_db_session(engine)
    data = session.query(Rent).order_by(
        desc(Rent.rent_id)).all()
    return response(data, 200, "Rents retrieved successfully.", False)
