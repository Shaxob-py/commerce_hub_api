from fastapi import APIRouter, HTTPException
from fastapi import Depends, status
from uuid import UUID

from fastapi.responses import ORJSONResponse

from database import User, Comment
from schemas.product import CommentPostSchema, ReadCommentSchema
from schemas.user import ResponseSchema
from utils.jwt_token import get_current_user

comment_router = APIRouter(tags=["Comment"])




@comment_router.delete("/comments/{comments_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_comment_view(comments_id: UUID, current_user: User = Depends(get_current_user)):
    comment = await Comment.get(comments_id)
    if comment.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Forbidden",
        )

    await Comment.delete(comments_id)
    return None


@comment_router.get("/products/{product_id}/comments", status_code=status.HTTP_200_OK,
                    response_model=ResponseSchema[list[ReadCommentSchema]])
async def delete_comment_view(product_id: UUID):
    comment = await Comment.filter(Comment.product_id == product_id)
    if not comment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Comment not found",
        )

    return ResponseSchema[list[ReadCommentSchema]](
        message="Comments",
        data=comment,
    )


@comment_router.post("/products/{product_id}/comments", response_model=ResponseSchema,
                     status_code=status.HTTP_201_CREATED)
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
