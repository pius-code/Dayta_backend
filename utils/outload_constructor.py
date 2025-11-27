from model.payload import InPayload
from model.payload2 import InPayload2
import secrets

token = secrets.token_urlsafe(18)[:25]


def outload_constructor(in_payload: InPayload) -> dict:
    phone = in_payload.phone
    volume = in_payload.volume
    network = in_payload.network
    reference = token
    referrer = "0536287642"

    outload = {
        "phone": phone,
        "volume": volume,
        "network": network,
        "reference": reference,
        "referrer": referrer,
    }
    return outload


def outload_constructor2(in_payload: InPayload2) -> dict:
    recipient = in_payload.phone
    capacity = in_payload.volume
    networkKey = in_payload.network

    outload2 = {
        "recipient": recipient,
        "capacity": capacity,
        "networkKey": networkKey,
    }
    return outload2
