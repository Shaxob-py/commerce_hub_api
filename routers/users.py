from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from fastapi import status

from database import User, SupportMessage
from schemas.user import ResponseSchema, UserSchema, UserUpdateSchema, UserSupportSchema
from utils.jwt_token import get_current_user

user_router = APIRouter(tags=["User"])


@user_router.get('/users/{user_id}', status_code=status.HTTP_200_OK, response_model=ResponseSchema[UserSchema])
async def get_user_by_id_view(user_id: UUID):
    user = await User.get(user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    return ResponseSchema[UserSchema](
        message=f'User {user_id}',
        data=user
    )


@user_router.patch('/users/me', status_code=status.HTTP_202_ACCEPTED, response_model=ResponseSchema)
async def user_update_me_view(data: UserUpdateSchema, current_user=Depends(get_current_user)):
    user = await User.update(current_user.id, username=data.username)
    return ResponseSchema(
        message=f'User {user.id} updated',
        data=None
    )


@user_router.get('/users/me', status_code=status.HTTP_200_OK, response_model=ResponseSchema[UserSchema])
async def user_get_me_view(current_user=Depends(get_current_user)):
    user = await User.get(current_user.id)
    return ResponseSchema(
        data=user
    )


@user_router.post('/users/support-message', status_code=status.HTTP_201_CREATED,response_model=ResponseSchema)
async def user_support_message_view(data: UserSupportSchema, current_user=Depends(get_current_user)):
    await SupportMessage.create(
        message=data.message,
        user_id=current_user.id,
    )
    return ResponseSchema(
        message=f'Support message created',
        data=None
    )
