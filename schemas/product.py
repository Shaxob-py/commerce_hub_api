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




class ReadProductSchema(BaseModel):
    id : UUID
    name : str
    price : float
    lat : float
    user_id : UUID
    lng : float
    photo_url : str
    currency : str
    description : str
    category_id : UUID

    class Config:
        from_attributes = True


class ReadCategorySchema(BaseModel):
    id : UUID
    name : str

    class Config:
        from_attributes = True


class CommentPostSchema(BaseModel):
    text : str
    product_id : UUID
    user_id : UUID

    @field_validator('text')
    def password_validator(cls, value):
        if len(value) > 200 :
            raise ValueError('len too long')
        return value

    class Config:
        from_attributes = True