from fastapi import APIRouter
from core.config import provider1_base_url
from utils.safe_request import safe_get


router = APIRouter(prefix="/check_balance", tags=["check_balance"])


@router.get(
    "/",
    summary="Use this to get the balance of your account",
    description="returns the balance you have in your account and you can use"
    "that information to do whatever you'd want",
)
async def get_balance():
    print("hit this route")
    url = f"{provider1_base_url}/check_balance"
    response = await safe_get(url=url)
    print(response)
    return response
