from fastapi import APIRouter, Query
from model.payload2 import InPayload2
from utils.paystack import get_payment_url
import uuid
from route.order_store import pending_orders, orders_status

router = APIRouter(prefix="/buy_x", tags=["BuyX"])


@router.post(
    "/",
    summary="Use this route to buy a data for a given network,"
    " MTN and Telecel. for AT use the /buy route"
    "From datahub",
    description="the route just buys data from datahub",
)
async def buy_data(data: InPayload2):
    network = data.network
    if network is None:
        return {"error": "Network required"}
    else:
        print(data)
        try:
            reference = str(uuid.uuid4())
            print("Generated reference:", reference)
            response = await get_payment_url(
                data.email, amount=data.amount * 100, reference=reference
            )
            print("Paystack response:", response)
            # Store the order details using the reference
            pending_orders[reference] = data.model_dump()
            return {
                "payment_url": response.get("data", {}).get(
                    "authorization_url"
                ),  # noqa
                "reference": reference,
            }
        except Exception as e:
            print("Error:", e)
            return {"error": "Payment initiation failed"}


@router.get("/order_status")
async def order_status(reference: str = Query(...)):
    if reference in orders_status:
        print("Order found for reference:", reference)
        return orders_status[reference]
    elif reference in pending_orders:
        print("Order is still pending for reference:", reference)
        return {"status": "pending"}
    else:
        print("Order not found for reference:", reference)
        return {"status": "not_found"}
