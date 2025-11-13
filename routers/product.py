from uuid import UUID

from fastapi import APIRouter
from fastapi import UploadFile, File, Form, Depends, status

from database import Product
from schemas.user import ResponseSchema
from utils.jwt_token import get_current_user
from utils.utils import save_photo

product_router = APIRouter(tags=["Product"])


@product_router.post("/products", response_model=ResponseSchema, status_code=status.HTTP_201_CREATED)
async def create_product(
        name: str = Form(...),
        price: float = Form(...),
        lat: float = Form(...),
        lng: float = Form(...),
        currency: str = Form(...),
        description: str = Form(...),
        category_id: UUID = Form(...),
        photo: UploadFile = File(...),
        current_user=Depends(get_current_user)):

    photo_url = await save_photo(photo)

    await Product.create(
        name=name,
        price=price,
        description=description,
        lat=lat,
        lng=lng,
        photo_url=photo_url,
        category_id=category_id,
        user_id=current_user.id,
        currency=currency,
        views=0,
    )

    return ResponseSchema(
        message="Product created successfully",
        data=None,
    )
