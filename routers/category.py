from fastapi import APIRouter, HTTPException
from fastapi.responses import ORJSONResponse
from starlette import status

from database import Product, Category
from schemas.product import ReadProductSchema, ReadCategorySchema
from schemas.user import ResponseSchema

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
