from uuid import UUID

from fastapi import APIRouter
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


@product_router.get("/products/{id_}", response_model=ResponseSchema[ReadProductSchema],
                    status_code=status.HTTP_200_OK) 
async def get_product_view(id_: UUID):
    product = await Product.get(id_)

    if product:
        return ResponseSchema[ReadProductSchema](
            message=f"Product {id_} was found",
            data=product,
        )
    return ORJSONResponse(
        {"message": "Product not found"},
                status_code=status.HTTP_404_NOT_FOUND)


@product_router.delete("/products/{id_}",response_model=ResponseSchema,
                    status_code=status.HTTP_204_NO_CONTENT)
async def get_product_view(id_: UUID,current_user=Depends(get_current_user)):
    product = await Product.get(id_)
    if product.user_id != current_user.id:
        return ORJSONResponse({
            "message": "You are not the owner of this product",
        },status_code=status.HTTP_403_FORBIDDEN)
    await Product.delete(id_)
    return ResponseSchema(
        message="Product deleted successfully",
        data=None,
    )



