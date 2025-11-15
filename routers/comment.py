from fastapi import APIRouter, HTTPException
from fastapi import Depends, status
from uuid import UUID

from fastapi.responses import ORJSONResponse

from database import User, Comment
from schemas.product import CommentPostSchema
from schemas.user import ResponseSchema
from utils.jwt_token import get_current_user

comment_router = APIRouter(tags=["Comment"])


@comment_router.post("/comments", response_model=ResponseSchema, status_code=status.HTTP_201_CREATED)
async def create_comment_view(data: CommentPostSchema, current_user: User = Depends(get_current_user)):
    await Comment.create(
        message=data.message,
        product_id=data.product_id,
        user_id=current_user.id,
    )
    return ResponseSchema(
        message='Success',
        data=None
    )


@comment_router.delete("/comments/{comments_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_comment_view(comments_id: UUID, current_user: User = Depends(get_current_user)):
    comment = await Comment.get(comments_id)
    if comment.user_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="Forbidden",
        )

    await Comment.delete(comments_id)
    return None


@comment_router.get("/comments/{product_id}", status_code=status.HTTP_200_OK)
async def delete_comment_view(comments_id: UUID, current_user: User = Depends(get_current_user)):
    comment = await Comment.get(comments_id)
    if comment.user_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="Forbidden", )
    await Comment.delete(comments_id)
    return None
