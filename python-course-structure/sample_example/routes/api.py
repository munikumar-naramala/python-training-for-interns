from fastapi import APIRouter
from sample_example.end_points import product, user

router = APIRouter()
router.include_router(product.router)
router.include_router(user.router)
