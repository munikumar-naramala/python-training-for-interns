from fastapi import APIRouter, HTTPException
from models.models import Order, DeliveryPartner
from db.database import Database
from schemas.request import DeliveryPartnerRequest
import uuid
from schemas.response import response
from static.send_mail import send_email

router = APIRouter(
    prefix="/delivery",
    tags=["delivery"],
    responses={404: {"description": "Not found"}},
)

database = Database()
engine = database.get_db_connection()
db = database.get_db_session(engine)


@router.post("/assign_partner/{order_id}")
def assign_delivery_partner(order_id: str):
    try:

        delivery_partner = db.query(DeliveryPartner).filter_by(status=0).first()

        if not delivery_partner:
            raise HTTPException(status_code=404, detail="No available delivery partner")

        order = db.query(Order).filter_by(order_id=order_id).first()
        if not order:
            raise HTTPException(status_code=404, detail="Order not found")

        order.delivery_partner = delivery_partner

        db.commit()

        subject = "Delivery partner assigned successfully"
        message = f"Hello,\n\nYour delivery partner is assigned successfully for the order number {order_id}."
        send_email(subject, message, delivery_partner.contact_info)

        return {"message": "Delivery partner assigned successfully!"}

    except HTTPException as e:
        raise e
    except Exception as e:

        db.rollback()
        raise HTTPException(status_code=500, detail="Error assigning delivery partner") from e


@router.post("/register_delivery_partner", response_description="Add a delivery partner")
async def add_delivery_partner(delivery_partner_req: DeliveryPartnerRequest):
    new_delivery_partner = DeliveryPartner()
    new_delivery_partner.id = str(uuid.uuid4())
    new_delivery_partner.contact_info = delivery_partner_req.contact_info
    new_delivery_partner.status = delivery_partner_req.status

    db.add(new_delivery_partner)
    db.flush()

    db.refresh(new_delivery_partner, attribute_names=['id'])
    data = {"id": new_delivery_partner.id}
    db.commit()
    db.close()
    return response(data, 200, "Delivery Partner added successfully.", False)


@router.get("/")
async def read_all_delivery_partners():
    session = database.get_db_session(engine)
    data = session.query(DeliveryPartner).all()
    return response(data, 200, "DPs retrieved successfully.", False)
