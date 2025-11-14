from uuid import UUID

from fastapi import APIRouter
from fastapi import status
from fastapi.responses import ORJSONResponse

from schemas.user import ResponseSchema, UserSchema

user_router = APIRouter(tags=["User"])


@user_router.get('/users/{id}', status_code=status.HTTP_200_OK, response_model=ResponseSchema[UserSchema])
async def get_user_by_id(id_: UUID):
    user = await get_user_by_id(id_)
    if not user:
        ORJSONResponse(status_code=status.HTTP_404_NOT_FOUND,
                       content={"message": "user not found"})
    return ResponseSchema[UserSchema](
        message=f'User {id_}',
        data=user
    )
