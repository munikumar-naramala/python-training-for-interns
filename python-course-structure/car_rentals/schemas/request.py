from pydantic import BaseModel, EmailStr, Field, datetime_parse
from typing import List
from datetime import datetime


class UserRequest(BaseModel):
    username: str = Field(None, title="User Name", max_length=1000)
    email: EmailStr = Field(None, title="User email")
    password_hash: str = Field(None, title="User password")
    address: str = Field(None, title="User address")
    phone: str = Field(None, title="Contact User")


class UserUpdateRequest(BaseModel):
    username: str = Field(
        None, title="User Name", max_length=1000
    )
    email: str = Field(
        None, title="email", max_length=1000
    )
    password_hash: str = Field(
        None, title="password", max_length=1000
    )
    address: str = Field(
        None, title="address", max_length=1000
    )
    phone: str = Field(
        None, title="phone", max_length=1000
    )


class Token(BaseModel):
    access_token: str
    token_type: str


class OwnerRequest(BaseModel):
    owner_name: str = Field(None, title="Owner Name", max_length=1000)
    owner_email: EmailStr = Field(None, title="Owner email")
    owner_password_hash: str = Field(None, title="Owner password")
    owner_address: str = Field(None, title="Owner address")
    owner_phone: str = Field(None, title="Contact Owner")


class OwnerUpdateRequest(BaseModel):
    owner_name: str = Field(
        None, title="Owner Name", max_length=1000
    )
    owner_email: str = Field(
        None, title="email", max_length=1000
    )
    owner_password_hash: str = Field(
        None, title="password", max_length=1000
    )
    owner_address: str = Field(
        None, title="address", max_length=1000
    )
    owner_phone: str = Field(
        None, title="phone", max_length=1000
    )


class VehicleRequest(BaseModel):
    owner_id: str = Field(None, title="Owner id", max_length=1000)
    registration_number: str = Field(None, title="Registration Number", max_length=1000)
    type: str = Field(None, title="type")
    brand: str = Field(None, title="Brand")
    model: str = Field(None, title="Model")
    year: int = Field(None, title="year")
    color: str = Field(None, title="Color")
    amount_per_hour: float = Field(None, title="Amount Per Hour")
    is_available: bool = Field(None, title="availability")


class VehicleUpdateRequest(BaseModel):
    registration_number: str = Field(
        None, title="Registration Number", max_length=1000
    )
    type: str = Field(
        None, title="type", max_length=1000
    )
    brand: str = Field(
        None, title="brand", max_length=1000
    )
    model: str = Field(
        None, title="model", max_length=1000
    )
    year: str = Field(
        None, title="year", max_length=1000
    )
    color: str = Field(
        None, title="color", max_length=1000
    )
    amount_per_hour: str = Field(
        None, title="Amount Per Hour", max_length=1000
    )
    is_available: bool = Field(
        None, title="Availability"
    )


class RentRequest(BaseModel):
    user_id: str = Field(None, title="User id", max_length=1000)
    vehicle_id: str = Field(None, title="Vehicle id", max_length=1000)
    duration: int = Field(None, title="number of days")
    start_date: datetime = Field(None, title="rental_end_date")
