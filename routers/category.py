from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import ORJSONResponse
from starlette import status
from uuid import UUID

from database import Product, Category, User
from schemas.product import ReadProductSchema, ReadCategorySchema
from schemas.user import ResponseSchema
from utils.jwt_token import get_current_user

category_router = APIRouter(tags=["Category"])


@category_router.get("/categories/{category_id}/products", response_model=ResponseSchema[list[ReadProductSchema]],
                     status_code=status.HTTP_200_OK)
async def get_products_by_category_view(
        category_id: str,
        limit: int = 10,
        offset: int = 0
):
    products = await Product.get_products_by_category(
        category_id=category_id,
        limit=limit,
        offset=offset
    )
    if products:
        return ResponseSchema[list[ReadProductSchema]](
            message='Category products',
            data=products,
        )
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Product not found"
    )


@category_router.get("/categories", response_model=ResponseSchema[list[ReadCategorySchema]],
                     status_code=status.HTTP_200_OK)
async def get_categories_view():
    categories = await Category.get_all()
    return ResponseSchema[list[ReadCategorySchema]](
        message='Categories',
        data=categories,
    )


@category_router.post("/categories", response_model=ResponseSchema[list[ReadCategorySchema]],
                      status_code=status.HTTP_201_CREATED)
async def create_categories_view(data: ReadCategorySchema, current_user=Depends(get_current_user)):
    if current_user.role == await User.role.ADMIN:
        await Category.create(name=data.name)
        return ResponseSchema(
            message='Category created',
            data=None,
        )
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="User does not have permission to create category"
    )


@category_router.delete("/categories/{category_id}",
                        status_code=status.HTTP_204_NO_CONTENT)
async def delete_categories_view(category_id: UUID, current_user=Depends(get_current_user)):
    if current_user.role == await User.role.ADMIN:
        await Category.delete(category_id)
        return ResponseSchema(
            message='Category deleted',
            data=None,
        )
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="User does not have permission to delete category"
    )
