from uuid import UUID

from pydantic import BaseModel, field_validator

class CategorySchema(BaseModel):
    icon: str
    name: str

    class Config:
        from_attributes = True


class ProductSchema(BaseModel):
    name : str
    price : float
    lat : float
    lng : float
    photo : str
    currency : str
    user_id : UUID
    category_id : UUID

    @field_validator('price')
    def password_validator(cls, value):
        if len(value) < 12:
            raise ValueError('Price must be at least 12')
        return value

    class Config:
        from_attributes = True


