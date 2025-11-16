from typing import Generic, TypeVar
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field

from schemas.product import ProductSchema

T = TypeVar('T', bound=BaseModel)


class ResponseSchema(BaseModel, Generic[T]):
    message: str
    data: T | None = None


class RegisterSchema(BaseModel):
    email: EmailStr = Field(..., examples=['xunuddinovshaxob@gmail.com'])
    username: str


class LoginSchema(BaseModel):
    email: EmailStr = Field(..., examples=['xunuddinovshaxob@gmail.com'])



class VerifySchema(BaseModel):
    email: EmailStr = Field(..., examples=['xunuddinovshaxob@gmail.com'])
    code: str

class UserSchema(BaseModel):
    id : UUID
    username: str
    email: EmailStr
    products: list[ProductSchema]

class UserUpdateSchema(BaseModel):
    username: str

class UserSupportSchema(BaseModel):
    message: str