from fastapi import Request
from fastapi.responses import JSONResponse
import jwt
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("NEXTAUTH_SECRET", "DEV_SECRET")
ALGORITHM = "HS256"


async def verify_token(request: Request, call_next):
    public_paths = ["/", "/check_balance/"]
    if request.url.path in public_paths:
        return await call_next(request)

    auth_header = request.headers.get("Authorzation")
    if not auth_header or not auth_header.startswith("Bearer "):
        return JSONResponse(
            status_code=401, content={"detail": "Missing or invalid token"}
        )

    token = auth_header.split(" ")[1]
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        request.state.user = payload
    except jwt.ExpiredSignatureError:
        return JSONResponse(
            status_code=401, content={"detail": "User's Token is expired"}
        )
    except jwt.InvalidTokenError:
        return JSONResponse(
            status_code=401, content={"details": "Users token is invalid"}
        )

    response = await call_next(request)
    return response
