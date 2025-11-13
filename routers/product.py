from fastapi import APIRouter, Depends
from starlette import status

from database import Product
from schemas.product import ProductSchema
from schemas.user import ResponseSchema
from utils.jwt_token import get_current_user
from utils.utils import save_photo

product_router = APIRouter(tags=["Product"])


@product_router.post("/products", response_model=ResponseSchema, status_code=status.HTTP_201_CREATED)
async def create_tour(
        data: ProductSchema,
        current_user=Depends(get_current_user)):

    await Product.create(
        name=data.name,
        price=data.price,
        description=data.description,
        photo_url=save_photo(data.image),
        category=data.category,
        user=current_user.id

    )

