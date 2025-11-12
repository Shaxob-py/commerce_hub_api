from fastapi import APIRouter, Depends
from fastapi.responses import ORJSONResponse
from starlette import status

from database import User
from schemas.user import RegisterForm
from services.otp_services import OtpService
from utils.utils import generate_code

auth_router = APIRouter(prefix='/auth', tags=["Auth"])


def otp_service():
    return OtpService()


@auth_router.post('/register')
async def login_view(data: RegisterForm, service: OtpService = Depends(otp_service)):
    user = await User.get_by_email(data.email)
    if user is not None:
        return ORJSONResponse(
            {'message': 'Username already registered'},
            status.HTTP_400_BAD_REQUEST
        )

    service.save_user_before_registration(data.email, data.model_dump())
    code = generate_code()
    print(code)
    service.send_otp_by_email(data.email, str(code))
    return ORJSONResponse(
        {'message': 'Check your email to verify your account'},
    )



@auth_router.get('/verification-email')
async def login_view(email: str, code: str, service: OtpService = Depends(otp_service)):
    is_verified, user_data = service.verify_email(email, code)
    if is_verified:
        await User.create(**user_data)
        return ORJSONResponse(
            {'message': 'User successfully registered'}
        )
    return ORJSONResponse(
        {'message': 'Invalid or expired code'},
        status.HTTP_400_BAD_REQUEST
    )
