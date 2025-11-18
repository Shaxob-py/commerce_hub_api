from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from fastapi import status

from database import User, SupportMessage, Product
from schemas.product import ProductSchema
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


@user_router.get('/users/me/products', status_code=status.HTTP_200_OK,
                 response_model=ResponseSchema[list[ProductSchema]])
async def get_user_products_view(current_user=Depends(get_current_user), limit: int = 10, offset=0):
    products = await Product.get_products_by_user_id(current_user.id, limit, offset)
    if not products:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )
    return ResponseSchema[list[ProductSchema]](
        message=f'User {current_user.id} products',
        data=products
    )


@user_router.get('/users/me', status_code=status.HTTP_200_OK, response_model=ResponseSchema[UserSchema])
async def user_get_me_view(current_user=Depends(get_current_user)):
    user = await User.get(current_user.id)
    return ResponseSchema(
        data=user
    )


@user_router.post('/users/support-message', status_code=status.HTTP_201_CREATED, response_model=ResponseSchema)
async def user_support_message_view(data: UserSupportSchema, current_user=Depends(get_current_user)):
    await SupportMessage.create(
        message=data.message,
        user_id=current_user.id,
    )
    return ResponseSchema(
        message=f'Support message created',
        data=None
    )


@user_router.get('/users/{user_id}/products', status_code=status.HTTP_200_OK,
                 response_model=ResponseSchema[list[ProductSchema]])
async def get_user_products_view(user_id: UUID, limit: int = 10, offset: int = 0):
    products = await Product.get_products_by_user_id(user_id, limit, offset)
    if not products:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )
    return ResponseSchema[list[ProductSchema]](
        message=f'User {user_id} products',
        data=products
    )
