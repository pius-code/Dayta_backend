from fastapi import APIRouter
from model.payload import InPayload
from utils.safe_request import safe_post
from core.config import provider1_base_url
from utils.outload_constructor import outload_constructor

router = APIRouter(prefix="/buy", tags=["Buy"])


@router.post(
    "/",
    summary="Use this route to buy a data for a given network, MTN airteltigo",
    description="the route just buys data",
)
async def buy_data(data: InPayload):
    network = data.network
    if network is None:
        return {"error": "Network required"}
    else:
        url = f"{provider1_base_url}/{network}-new-transaction"
        outload = outload_constructor(data)
        response = await safe_post(url, outload)
        print(response)
        return response
