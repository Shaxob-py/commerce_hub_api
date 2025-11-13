from fastapi import APIRouter

from routers.auth import auth_router
from routers.product import product_router

router = APIRouter()
router.include_router(auth_router)
router.include_router(product_router)
