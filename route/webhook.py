from fastapi import APIRouter, Request
from utils.paystack import verify_transaction
from utils.safe_request import safe_post
from core.config import provider1_base_url
from utils.outload_constructor import outload_constructor
from route.order_store import pending_orders, orders_status
from model.payload import InPayload

router = APIRouter(prefix="/webhook", tags=["webhook"])


@router.post(
    "/",
    summary="Webhook endpoint for external services",
)
async def webhook_handler(request: Request):
    payload = await request.json()
    # Extract the reference
    reference = payload.get("data", {}).get("reference")
    print("Payment reference:", reference)
    if reference:
        verification_response = await verify_transaction(reference)
        print("Verification response:", verification_response)
        # Process the verification response as needed

        order_data = pending_orders.pop(reference, None)
        if order_data:
            order_obj = InPayload(**order_data)
            network = order_obj.network
            url = f"{provider1_base_url}/{network}-new-transaction"
            outload = outload_constructor(order_obj)
            response = await safe_post(url, outload)
            print("Order fulfilled:", response)
            response = {"status": "fulfilled", "details": response}
            orders_status[reference] = response
            return response
        else:
            print("No pending order found for reference:", reference)
            return {"status": "no order"}
    return {"status": "ok"}


@router.post("", include_in_schema=False)
async def webhook_handler_no_slash(request: Request):
    return await webhook_handler(request)
