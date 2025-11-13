from fastapi import APIRouter

from database import Product
from schemas.product import ProductSchema
from schemas.user import ResponseSchema
from utils.jwt_token import get_current_user
from utils.utils import save_photo

category_router = APIRouter(tags=["Category"])



@category_router.get("/categories/{category_id}/products")
async def get_products_by_category(
    category_id: str,
    limit: int = 10,
    offset: int = 0
):
    products = await Product.filter(Product.category_id == category_id)
    return products
