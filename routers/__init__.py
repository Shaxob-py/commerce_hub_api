from fastapi import APIRouter

from routers.auth import auth_router
from routers.product import product_router
from routers.category import category_router
from routers.users import user_router

router = APIRouter()
router.include_router(auth_router)
router.include_router(product_router)
router.include_router(category_router)
router.include_router(user_router)
