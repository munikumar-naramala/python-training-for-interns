import uuid
from fastapi import APIRouter
from schemas.request import VehicleRequest, VehicleUpdateRequest
from schemas.response import response
from db.database import Database
from sqlalchemy import and_, desc
from models.models import Vehicle

router = APIRouter(
    prefix="/vehicle",
    tags=["Vehicle"],
    responses={404: {"description": "Not found"}},
)

database = Database()
engine = database.get_db_connection()


@router.post("/add_vehicle", response_description="Add a vehicle")
async def add_vehicle(vehicle_req: VehicleRequest):
    new_vehicle = Vehicle()
    new_vehicle.vehicle_id = str(uuid.uuid4())
    new_vehicle.owner_id = vehicle_req.owner_id
    new_vehicle.registration_number = vehicle_req.registration_number
    new_vehicle.type = vehicle_req.type
    new_vehicle.brand = vehicle_req.brand
    new_vehicle.model = vehicle_req.model
    new_vehicle.year = vehicle_req.year
    new_vehicle.color = vehicle_req.color
    new_vehicle.amount_per_hour = vehicle_req.amount_per_hour
    new_vehicle.is_available = vehicle_req.is_available
    session = database.get_db_session(engine)
    session.add(new_vehicle)
    session.flush()

    session.refresh(new_vehicle, attribute_names=['vehicle_id'])
    data = {"vehicle_id": new_vehicle.vehicle_id}
    session.commit()
    session.close()
    return response(data, 200, "Vehicle added successfully.", False)


@router.put("/update_vehicle/{vehicle_id}")
async def update_vehicle(vehicle_update_req: VehicleUpdateRequest, vehicle_id: str):
    session = database.get_db_session(engine)
    try:
        is_vehicle_updated = session.query(Vehicle).filter(Vehicle.vehicle_id == vehicle_id).update({
            Vehicle.registration_number: vehicle_update_req.registration_number,
            Vehicle.type: vehicle_update_req.type,
            Vehicle.brand: vehicle_update_req.brand,
            Vehicle.model: vehicle_update_req.model,
            Vehicle.year: vehicle_update_req.year,
            Vehicle.color: vehicle_update_req.color,
            Vehicle.amount_per_hour: vehicle_update_req.amount_per_hour,
            Vehicle.is_available: vehicle_update_req.is_available
        }, synchronize_session=False)
        session.flush()
        session.commit()
        response_msg = "Vehicle details updated successfully"
        response_code = 200
        error = False
        if is_vehicle_updated == 1:
            data = session.query(Vehicle).filter(
                Vehicle.vehicle_id == vehicle_id).one()

        elif is_vehicle_updated == 0:
            response_msg = "Vehicle not updated. No Vehicle found with this id :" + \
                           str(vehicle_id)
            error = True
            data = None
        return response(data, response_code, response_msg, error)
    except Exception as ex:
        print("Error : ", ex)


@router.get("/{vehicle_id}")
async def read_vehicle(vehicle_id: str):
    session = database.get_db_session(engine)
    response_message = "Vehicle retrieved successfully"
    data = None
    try:
        data = session.query(Vehicle).filter(
            and_(Vehicle.vehicle_id == vehicle_id)).one()
    except Exception as ex:
        print("Error", ex)
        response_message = "Vehicle Not found"
    error = False
    return response(data, 200, response_message, error)


@router.get("/")
async def read_all_vehicles():
    session = database.get_db_session(engine)
    data = session.query(Vehicle).order_by(
        desc(Vehicle.vehicle_id)).all()
    return response(data, 200, "Vehicles retrieved successfully.", False)
