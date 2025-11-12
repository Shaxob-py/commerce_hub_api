from fastapi import APIRouter, Depends

from utils.jwt_token import get_current_user

product = APIRouter()



@product.post("/trips")
async def create_tour(
        data: TripSchema,
        current_user=Depends(get_current_user),
):