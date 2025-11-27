import os
from dotenv import load_dotenv

load_dotenv()

provider1_base_url = os.getenv("PROV1_URL")
provider2_base_url = os.getenv("PROV2_URL")
