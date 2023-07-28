from sqlalchemy import Column, ForeignKey, Integer, String, TIMESTAMP, Enum, text, ARRAY, func, Float, Boolean, DATETIME
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import sqlalchemy

Base = sqlalchemy.orm.declarative_base()


class User(Base):
    __tablename__ = 'user'

    user_id = Column(String(1024), primary_key=True)
    username = Column(String(1024))
    email = Column(String(1024))
    password_hash = Column(String(1024))
    address = Column(String(1024))
    phone = Column(String(1024))
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())


class Owner(Base):
    __tablename__ = 'owner'

    owner_id = Column(String(1024), primary_key=True)
    owner_name = Column(String(1024))
    owner_email = Column(String(1024))
    owner_password_hash = Column(String(1024))
    owner_address = Column(String(1024))
    owner_phone = Column(String(1024))
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())


class Vehicle(Base):
    __tablename__ = 'vehicle'

    vehicle_id = Column(String(1024), primary_key=True)
    owner_id = Column(String(1024), ForeignKey("owner.owner_id"))
    registration_number = Column(String(1024))
    type = Column(Enum('Car', 'Motorcycle'))
    brand = Column(String(1024))
    model = Column(String(1024))
    year = Column(String(1024))
    color = Column(String(1024))
    amount_per_hour = Column(String(1024))
    is_available = Column(Boolean)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())


class Rent(Base):
    __tablename__ = 'rent'

    rent_id = Column(String(1024), primary_key=True)
    user_id = Column(String(1024), ForeignKey("user.user_id"))
    vehicle_id = Column(String(1024))
    duration = Column(Integer)
    start_date = Column(DATETIME)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())
