from sqlalchemy.exc import SQLAlchemyError
from models.models import Order, OrderItem, User
from fastapi import APIRouter, HTTPException
from db.database import Database
from static.send_mail import send_email

router = APIRouter(
    prefix="/get_amount",
    tags=["getTotalAmount"],
    responses={404: {"description": "Not found"}},
)

database = Database()
engine = database.get_db_connection()
db = database.get_db_session(engine)


@router.get("/{user_id}/{order_id}")
def calculate_order_total(user_id: str, order_id: str):
    try:
        order = (
            db.query(Order)
            .filter(Order.user_id == user_id, Order.order_id == order_id)
            .first()
        )
        user = (
            db.query(User)
            .filter(User.user_id == user_id).first()
        )

        if not order:
            raise HTTPException(status_code=404, detail="Order not found")

        order_items = (
            db.query(OrderItem)
            .filter(OrderItem.order_id == order_id)
            .all()
        )

        amounts = [int(amount) for item in order_items for amount in item.amounts.split(',')]
        quantities = [int(quantity) for item in order_items for quantity in item.quantities.split(',')]

        total_amount = sum(amount * quantity for amount, quantity in zip(amounts, quantities))
        subject = "Payment success and order placed"
        message = f"Hello {user.user_name},\n\nYour have paid successfully. Your order is now placed."
        send_email(subject, message, user.email)
        db.close()

        return {"total_amount": total_amount}



    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="Database error") from e
