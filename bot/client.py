from binance.client import Client
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_client():
    api_key = os.getenv("API_KEY")
    api_secret = os.getenv("API_SECRET")
    base_url = os.getenv("BASE_URL")

    client = Client(api_key, api_secret)
    client.FUTURES_URL = base_url

    return client


# Test run
if __name__ == "__main__":
    client = get_client()
    print("Client created successfully ✅")