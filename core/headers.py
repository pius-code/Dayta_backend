import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
Prov2_API_KEY = os.getenv("PROV2_API_KEY")
if not API_KEY:
    raise ValueError("API KEY NOT FOUND")

headers = {"token": f"Bearer {API_KEY}", "Content-Type": "application/json"}

headers2 = {"content-Type": "application/json", "X-API-Key": f"{Prov2_API_KEY}"}  # noqa
