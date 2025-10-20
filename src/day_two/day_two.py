import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPEN_AI_API_KEY")

headers = {"Authorization": f"Bearer {api_key}", "Content-type": "application/json"}

payload = {
    "model": "gpt-5-nano",
    "messages": [{"role": "user", "content": "Tell me a joke"}],
}

response = requests.post(
    "https://api.openai.com/v1/chat/completions",
    headers=headers,
    json=payload,
    timeout=30,
)

print(response.json()["choices"][0]["message"]["content"])
