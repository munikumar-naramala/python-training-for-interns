from fastapi import APIRouter
from crud import user, owner, vehicle, rent, get_total_amount

router = APIRouter()
router.include_router(user.router)
router.include_router(owner.router)
router.include_router(vehicle.router)
router.include_router(rent.router)
router.include_router(get_total_amount.router)
