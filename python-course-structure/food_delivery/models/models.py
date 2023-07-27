from sqlalchemy import Column, ForeignKey, Integer, String, TIMESTAMP, Enum, text, ARRAY, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import sqlalchemy

Base = sqlalchemy.orm.declarative_base()


class User(Base):
    __tablename__ = 'user'

    user_id = Column(String(1024), primary_key=True)
    user_name = Column(String(1024), nullable=False)
    email = Column(String(1024), nullable=False)
    password = Column(String(1024))
    address = Column(String(1024))
    phone = Column(String(1024), nullable=False)
    created_by = Column(Integer)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_by = Column(Integer)
    updated_at = Column(TIMESTAMP, onupdate=func.now())


class Restaurant(Base):
    __tablename__ = "restaurant"
    restaurant_id = Column(String(1024), primary_key=True)
    restaurant_name = Column(String(1024), nullable=False)
    address = Column(String(1024), nullable=False)
    phone = Column(String(1024), nullable=False)
    email = Column(String(1024), nullable=False)
    opening_hours = Column(String(1024), nullable=False)
    description = Column(String(1024), nullable=False)
    rating = Column(Integer, nullable=False)
    created_by = Column(Integer)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_by = Column(Integer)
    updated_at = Column(TIMESTAMP, onupdate=func.now())


class Order(Base):
    __tablename__ = "orders"
    order_id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("user.user_id"))
    restaurant_id = Column(String, ForeignKey("restaurant.restaurant_id"))
    order_status = Column(
        Enum("Pending", "In Progress", "Delivered", "Canceled"),
        default="Pending",
    )
    amount = Column(Integer)
    payment_status = Column(
        Enum("Pending", "Paid", "Failed"), nullable=False, default="Pending"
    )

    user = relationship("User", backref="orders")
    restaurant = relationship("Restaurant", backref="orders")


class Menu(Base):
    __tablename__ = "menu"
    menu_id = Column(String, primary_key=True)
    restaurant_id = Column(String, ForeignKey("restaurant.restaurant_id"))
    food_name = Column(String(1024), nullable=False)
    cuisine = Column(String(1024), nullable=True)
    amount = Column(Integer, nullable=False)

    restaurant = relationship("Restaurant", backref="menu")


class OrderItem(Base):
    __tablename__ = "order_items"
    order_items_id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(String)
    user_id = Column(String)
    restaurant_id = Column(String)
    menu_ids = Column(ARRAY(String))
    food_names = Column(ARRAY(String))
    amounts = Column(ARRAY(String))
    quantities = Column(ARRAY(String))


class DeliveryPartner(Base):
    __tablename__ = "delivery_partners"

    id = Column(String, primary_key=True)
    order_id = Column(String)
    contact_info = Column(String)
    status = Column(Integer)
