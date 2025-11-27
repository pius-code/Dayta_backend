from pydantic import BaseModel
from typing import Optional


class OutPayload(BaseModel):
    networkKey: str
    recipient: str
    capacity: str


class InPayload2(BaseModel):
    network: str
    phone: str
    volume: str
    amount: float
    email: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "network": "MTN",
                "phone": "0241234567",
                "amount": 5.0,
                "email": "dayta@user.com",
            }  # noqa
        }
