from pydantic import BaseModel, EmailStr, Field


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
    order_id: int = Field(..., description='order number')
    user_id: int = Field(..., description='ordered by')
    delivery_status: str = Field(..., description='delivery status')
    payment_status: str = Field(..., description='payment status')


class MenuRequest(BaseModel):
    menu_id: int = Field(..., description='menu number')
    restaurant_id: int = Field(..., description='restaurant number')
    item_name: str = Field(..., description='food name')
    description: str = Field(..., description='description')
    amount: int = Field(..., description='order number')


class MenuUpdateRequest(BaseModel):
    menu_id: int
    item_name: str = Field(
        None, title="food Name", max_length=1000
    )
    description: str = Field(
        None, title="food description", max_length=1000
    )
    category: str = Field(
        None, title="food category", max_length=1000
    )
    amount: int = Field(..., gt=0,
                        description="The price of the food must be greater than zero")
    updated_by: int = Field(None, title="Updater Id")


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
    updated_by: int = Field(None, title="Updater Id")


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
