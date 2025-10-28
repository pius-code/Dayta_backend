from pydantic import BaseModel
from typing import Optional  # noqa


class OutPayload(BaseModel):
    phone: str
    volume: str
    reference: str
    referrer: str
    # webhook: str


class InPayload(BaseModel):
    network: str
    phone: str
    volume: str

    class Config:
        json_schema_extra = {
            "example": {
                "network": "MTN",
                "phone": "0241234567",
                "amount": 5.0,
            }  # noqa
        }
