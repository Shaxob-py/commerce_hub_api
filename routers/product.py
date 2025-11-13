from fastapi import APIRouter, Depends
from starlette import status

from schemas.product import ProductSchema
from schemas.user import ResponseSchema
from utils.jwt_token import get_current_user

product = APIRouter()



@product.post("/product", response_model=ResponseSchema , status_code=status.HTTP_201_CREATED)
async def create_tour(
        data : ProductSchema,
        current_user=Depends(get_current_user)):
    pass