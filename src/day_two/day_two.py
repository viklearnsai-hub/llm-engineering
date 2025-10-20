import os
import requests
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"

api_key = os.getenv("OPEN_AI_API_KEY")
gemini_key = os.getenv("GOOGLE_API_KEY")


client = OpenAI(base_url=GEMINI_BASE_URL, api_key=gemini_key)
headers = {"Authorization": f"Bearer {api_key}", "Content-type": "application/json"}

payload = {
    "model": "gpt-5-nano",
    "messages": [{"role": "user", "content": "Tell me whom am i talking to"}],
}

response = requests.post(
    "https://api.openai.com/v1/chat/completions",
    headers=headers,
    json=payload,
    timeout=30,
)

print(f"Response from GPT {response.json()["choices"][0]["message"]["content"]}")

gresponse = client.chat.completions.create(
    model="gemini-2.5-flash", messages=[{"role": "user", "content": "Tell me whom am i talking to"}]
)

print(f"Response from Gemini {gresponse.choices[0].message.content}")
