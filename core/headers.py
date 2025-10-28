import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise ValueError("API KEY NOT FOUND")

headers = {"token": f"Bearer {API_KEY}", "Content-Type": "application/json"}
