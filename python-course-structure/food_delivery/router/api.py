from fastapi import APIRouter
from crud import user, restaurant, menu, orders, order_items
from routers import delivery, get_total_amount

router = APIRouter()
router.include_router(user.router)
router.include_router(restaurant.router)
router.include_router(menu.router)
router.include_router(orders.router)
router.include_router(order_items.router)
router.include_router(get_total_amount.router)
router.include_router(delivery.router)
