import os
import requests
from dotenv import load_dotenv

load_dotenv()

response = requests.post(
    "https://openrouter.ai/api/v1/embeddings",
    headers={
        "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
        "Content-Type": "application/json"
    },
    json={
        "model": "liquid/lfm-2.5-embedding-350m:free",
        "input": "What is the capital of Pakistan?"
    }
)

response.raise_for_status()

result = response.json()["data"][0]["embedding"]

print(result)
print("Dimensions:", len(result))