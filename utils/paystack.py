import httpx
import os
from dotenv import load_dotenv

load_dotenv()

PSTCK_SECRET_KEY = os.getenv("PAYSTACK_SECRET_KEY")


async def get_payment_url(
    email: str = "dayta@user.com", amount: int = 5000, reference: str = None
):
    url = "https://api.paystack.co/transaction/initialize"
    headers = {
        "Authorization": "Bearer {}".format(PSTCK_SECRET_KEY),
        "Content-Type": "application/json",
    }
    payload = {
        "email": email,
        "amount": amount,
        "callback_url": "http://localhost:3000/dashboard/AT-retail",
    }
    if reference:
        payload["reference"] = reference

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload, headers=headers)
        return response.json()


async def verify_transaction(reference: str):
    async with httpx.AsyncClient() as client:
        url = f"https://api.paystack.co/transaction/verify/{reference}"
        headers = {
            "Authorization": "Bearer {}".format(PSTCK_SECRET_KEY),
            "Content-Type": "application/json",
        }
        response = await client.get(url, headers=headers)
        return response.json()
