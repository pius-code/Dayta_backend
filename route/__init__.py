from fastapi import APIRouter
from route.buy_routes import router as buy_data_router
from route.check_balance_route import router as check_balance_router


router = APIRouter()
router.include_router(buy_data_router)
router.include_router(check_balance_router)
