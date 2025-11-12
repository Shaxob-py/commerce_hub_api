from typing import Generic, TypeVar

from pydantic import BaseModel, EmailStr, Field

T = TypeVar('T', bound=BaseModel)


class ResponseSchema(BaseModel, Generic[T]):
    message: str
    data: T | None = None


class RegisterForm(BaseModel):
    email: EmailStr = Field(..., examples=['xunuddinovshaxob@gmail.com'])
    username: str


class LoginForm(BaseModel):
    email: EmailStr = Field(..., examples=['xunuddinovshaxob@gmail.com'])



class VerifyForm(BaseModel):
    email: EmailStr = Field(..., examples=['xunuddinovshaxob@gmail.com'])
    code: str