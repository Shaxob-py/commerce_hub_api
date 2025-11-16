from fastapi import APIRouter, Depends, Body, HTTPException
from fastapi.responses import ORJSONResponse
from starlette import status

from database import User
from schemas.user import RegisterSchema, ResponseSchema, LoginSchema, VerifySchema
from services.otp_services import OtpService
from utils.jwt_token import create_access_token, create_refresh_token
from utils.utils import generate_code

auth_router = APIRouter(prefix='/auth', tags=["Auth"])


def otp_service():
    return OtpService()


@auth_router.post('/register', status_code=status.HTTP_201_CREATED, response_model=ResponseSchema)
async def register_view(data: RegisterSchema, service: OtpService = Depends(otp_service)):
    user = await User.get_by_email(data.email)
    if user is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Bad request",
        )

    service.save_user_before_registration(data.email, data.model_dump())  # noqa
    code = generate_code()
    print(code)
    service.send_otp_by_email(data.email, str(code))  # noqa

    return ResponseSchema(
        message='Check your email',
        data=None)


@auth_router.post('/login', status_code=status.HTTP_200_OK, response_model=ResponseSchema)
async def login_view(data: LoginSchema, service: OtpService = Depends(otp_service)):
    user = await User.get_by_email(data.email)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not Authorized",
        )

    code = generate_code()
    print(code)
    service.save_user_before_registration(data.email, data.model_dump())  # noqa
    service.send_otp_by_email(data.email, str(code))  # noqa
    return ResponseSchema(
        message='Check your email',
        data=None)


@auth_router.post('/verification-email', status_code=status.HTTP_200_OK)
async def verifi_view(data: VerifySchema, service: OtpService = Depends(otp_service)):
    is_verified, user_data = service.verify_email(data.email, data.code)  # noqa

    if is_verified:
        user = await User.get_by_email(data.email)
        if user is None:
            user = await User.create(**user_data)

        access_token = create_access_token({"sub": str(user.id)})
        refresh_token = create_refresh_token({"sub": str(user.id)})

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
        }

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Invalid or expired code"
    )
