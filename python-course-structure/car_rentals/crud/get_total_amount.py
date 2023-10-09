from fastapi import APIRouter
from schemas.response import response
from db.database import Database
from models.models import Rent, Vehicle

router = APIRouter(
    prefix="/get_total_amount",
    tags=["Get Amount"],
    responses={404: {"description": "Not found"}},
)

database = Database()
engine = database.get_db_connection()


@router.get("/{rent_id}", response_description="Get total amount for a rent")
async def get_total_amount(rent_id: str):
    session = database.get_db_session(engine)
    try:
        rent = session.query(Rent).filter(Rent.rent_id == rent_id).first()
        if not rent:
            return response(None, 404, "Rent not found.", True)

        vehicle = session.query(Vehicle).filter(Vehicle.vehicle_id == rent.vehicle_id).first()
        if not vehicle:
            return response(None, 404, "Vehicle not found.", True)

        duration = rent.duration
        rental_duration_hours = duration * 24

        amount_per_hour = float(vehicle.amount_per_hour)
        total_amount = rental_duration_hours * amount_per_hour

        data = {"total_amount": total_amount}
        return data


    except Exception as ex:
        print("Error:", ex)
        return response(None, 500, "Internal Server Error.", True)
    finally:
        session.close()
