from pydantic import BaseModel, EmailStr, Field
from typing import List


class UserRequest(BaseModel):
    user_name: str = Field(
        None, title="User Name", max_length=1000
    )
    email: EmailStr = Field(None, title="User email")
    password: str = Field(None, title="User password")
    address: str = Field(None, title="User address")
    phone: str = Field(...,
                       description="Contact User")
    created_by: int = Field()


class RestaurantRequest(BaseModel):
    restaurant_name: str = Field(..., description='Restaurant Name')
    address: str = Field(..., description='Restaurant address')
    phone: str = Field(...,
                       description="Contact User")
    email: str = Field()
    opening_hours: str = Field()
    description: str = Field(...,
                             description="Contact User")
    rating: int = Field(..., title='rating')
    created_by: int = Field()


class OrderRequest(BaseModel):
    user_id: str = Field(..., description='user id')
    restaurant_id: str = Field(..., description='restaurant number')
    order_status: str = Field(..., description='delivery status')
    amount: int = Field(..., description='amount')
    payment_status: str = Field(..., description='payment status')


class MenuRequest(BaseModel):
    restaurant_id: str = Field(..., description='restaurant number')
    food_name: str = Field(..., description='food name')
    cuisine: str = Field(..., description='cuisine')
    amount: int = Field(..., description='order number')


class OrderItemRequest(BaseModel):
    order_id: str = Field(..., description='order id')
    user_id: str = Field(..., description='user id')
    restaurant_id: str = Field(..., description='restaurant id')
    menu_ids: List[str] = Field(..., description='menu id')
    food_names: List[str] = Field(..., description='food name')
    amounts: List[str] = Field(..., description='amount')
    quantities: List[str] = Field(..., description='quantity')


class DeliveryPartnerRequest(BaseModel):
    contact_info: str = Field(..., description='mail id')
    status: int = Field(..., description='status')


class MenuUpdateRequest(BaseModel):
    food_name: str = Field(
        None, title="food Name", max_length=1000
    )
    cuisine: str = Field(
        None, title="food category", max_length=1000
    )
    amount: int = Field(..., gt=0,
                        description="The price of the food must be greater than zero")


class RestaurantUpdateRequest(BaseModel):
    restaurant_name: str = Field(
        None, title="Restaurant Name", max_length=1000
    )
    description: str = Field(
        None, title="restaurant description", max_length=1000
    )
    category: str = Field(
        None, title="restaurant category", max_length=1000
    )
    rating: int = Field(..., ge=0,
                        description="restaurant rating")


class UserUpdateRequest(BaseModel):
    user_name: str = Field(
        None, title="Restaurant Name", max_length=1000
    )
    email: str = Field(
        None, title="restaurant description", max_length=1000
    )
    password: str = Field(
        None, title="restaurant category", max_length=1000
    )
    address: str = Field(
        None, title="restaurant category", max_length=1000
    )
    phone: str = Field(
        None, title="restaurant category", max_length=1000
    )
    updated_by: int = Field(None, title="Updater Id")


class Token(BaseModel):
    access_token: str
    token_type: str
