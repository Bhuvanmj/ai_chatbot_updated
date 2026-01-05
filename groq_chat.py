import os
import httpx
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
API_URL = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "http://localhost",
    "X-Title": "CharMinds AI Chatbot"
}

async def ask_groq(messages: list):
    data = {
        "model": "meta-llama/llama-3.1-8b-instruct",
        "messages": [{"role": "system", "content": "You are a helpful assistant."}] + messages,
        "temperature": 0.6,
        "top_p": 0.9
    }

    async with httpx.AsyncClient(timeout=60) as client:
        res = await client.post(API_URL, headers=headers, json=data)
        res.raise_for_status()
        return res.json()["choices"][0]["message"]["content"]

# keep this for compatibility
async def ask_groq_single(message: str):
    return await ask_groq([{"role": "user", "content": message}])
