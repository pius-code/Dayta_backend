import httpx
from core.headers import headers2 as default_headers
from typing import Optional


async def safe_get(url: str, headers: Optional[dict] = None):
    """safely make a get request"""
    headers = headers or default_headers
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url=url, headers=headers)
            response.raise_for_status()

            try:
                return response.json()
            except ValueError:
                return {"error": "Invalid JSON response", "raw": response.text}
    except Exception as e:
        print(e)
        return {"error": str(e)}


async def safe_post(
    url,
    payload: dict,
    headers: Optional[dict] = None,
):
    headers = headers or default_headers
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url=url, headers=headers, json=payload)  # noqa
            response.raise_for_status()

            try:
                return response.json()
            except ValueError:
                return response.json()
    except Exception as e:
        if hasattr(e, "response") and e.response is not None:
            print("Error responser:", e.response.text)
        print(e)
        return {"error": str(e.response.text)}
