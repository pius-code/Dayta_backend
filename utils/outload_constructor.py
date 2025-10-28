from model.payload import InPayload
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
