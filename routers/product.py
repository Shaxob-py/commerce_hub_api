from uuid import UUID

from fastapi import APIRouter, HTTPException
from fastapi import UploadFile, File, Form, Depends, status
from fastapi.responses import ORJSONResponse

from database import Product
from schemas.product import ReadProductSchema
from schemas.user import ResponseSchema
from utils.jwt_token import get_current_user
from utils.utils import save_photo

product_router = APIRouter(tags=["Product"])


@product_router.post("/products", response_model=ResponseSchema, status_code=status.HTTP_201_CREATED)
async def create_product_view(
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


@product_router.get("/products/{product_id}", response_model=ResponseSchema[ReadProductSchema],
                    status_code=status.HTTP_200_OK)
async def get_product_view(product_id: UUID):
    product = await Product.get(product_id)

    if product:
        return ResponseSchema[ReadProductSchema](
            message=f"Product {product_id} was found",
            data=product,
        )
    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )


@product_router.delete("/products/{product_id}",
                       status_code=status.HTTP_204_NO_CONTENT)
async def get_product_view(product_id: UUID, current_user=Depends(get_current_user)):
    product = await Product.get(product_id)
    if product.user_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="Forbidden",
        )

    if product:
        await Product.delete(product_id)
        return None
    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )
