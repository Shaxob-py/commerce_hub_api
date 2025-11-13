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
    photo_url : str
    currency : str
    description : str
    category_id : UUID

    @field_validator('price')
    def password_validator(cls, value):
        if value > 100000000:
            raise ValueError('Very big price')
        return value

    class Config:
        from_attributes = True


