import uuid
from fastapi import APIRouter
from schemas.request import OrderRequest
from schemas.response import response
from db.database import Database
from sqlalchemy import and_, desc
from models.models import Order

router = APIRouter(
    prefix="/orders",
    tags=["Orders"],
    responses={404: {"description": "Not found"}},
)

database = Database()
engine = database.get_db_connection()


@router.post("/add_order", response_description="Add an order")
async def add_order(order_req: OrderRequest):
    new_order = Order()
    new_order.order_id = str(uuid.uuid4())
    new_order.user_id = order_req.user_id
    new_order.restaurant_id = order_req.restaurant_id
    new_order.order_status = order_req.order_status
    new_order.amount = order_req.amount
    new_order.payment_status = order_req.payment_status
    session = database.get_db_session(engine)
    session.add(new_order)
    session.flush()

    session.refresh(new_order, attribute_names=['order_id'])
    data = {"order_id": new_order.order_id}
    session.commit()
    session.close()
    return response(data, 200, "Order added successfully.", False)


@router.get("/{order_id}")
async def read_order(order_id: str):
    session = database.get_db_session(engine)
    response_message = "Order retrieved successfully"
    data = None
    try:
        data = session.query(Order).filter(
            and_(Order.restaurant_id == order_id)).one()
    except Exception as ex:
        print("Error", ex)
        response_message = "Order Not found"
    error = False
    return response(data, 200, response_message, error)


@router.get("/")
async def read_all_orders():
    session = database.get_db_session(engine)
    data = session.query(Order).order_by(
        desc(Order.order_id)).all()
    return response(data, 200, "Orders retrieved successfully.", False)
