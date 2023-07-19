from fastapi import APIRouter
from endpoints import user, restaurant

router = APIRouter()
router.include_router(user.router)
router.include_router(restaurant.router)
