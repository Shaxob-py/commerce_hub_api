from pydantic import BaseModel, EmailStr, Field


class RegisterForm(BaseModel):
    email: EmailStr =  Field(..., examples=['xunuddinovshaxob@gmail.com'])
    username: str