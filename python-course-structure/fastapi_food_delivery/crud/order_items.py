from fastapi import APIRouter
from schemas.request import OrderItemRequest
from schemas.response import response
from models.models import OrderItem
from db.database import Database
from sqlalchemy import and_
import uuid

router = APIRouter(
    prefix="/order_items",
    tags=["OrderItems"],
    responses={404: {"description": "Not found"}},
)

database = Database()
engine = database.get_db_connection()


@router.post("/place_order/")
async def place_order(order_item_request: OrderItemRequest):
    order_items_id = str(uuid.uuid4())
    order_id = order_item_request.order_id
    user_id = order_item_request.user_id
    menu_ids = ','.join(order_item_request.menu_ids)
    restaurant_id = order_item_request.restaurant_id
    food_names = ','.join(order_item_request.food_names)
    amounts = ','.join(order_item_request.amounts)
    quantities = ','.join(order_item_request.quantities)

    new_order_item = OrderItem(
        order_items_id=order_items_id,
        order_id=order_id,
        user_id=user_id,
        restaurant_id=restaurant_id,
        menu_ids=menu_ids,
        food_names=food_names,
        amounts=amounts,
        quantities=quantities
    )

    session = database.get_db_session(engine)
    session.add(new_order_item)
    session.commit()

    return {"message": "Order placed successfully!"}


@router.get("/{order_items_id}")
async def read_orders(order_items_id: str):
    session = database.get_db_session(engine)
    response_message = "Order Items  retrieved successfully"
    data = None
    try:
        data = session.query(OrderItem).filter(
            and_(OrderItem.order_items_id == order_items_id)).one()
    except Exception as ex:
        print("Error", ex)
        response_message = "Order item Not found"
    error = False
    return response(data, 200, response_message, error)


@router.get("/")
async def read_all_orders():
    session = database.get_db_session(engine)
    data = session.query(OrderItem).all()
    session.close()
    return response(data, 200, "Order items retrieved successfully.", False)
