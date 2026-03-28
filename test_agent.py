import os
import requests

# Тестируем Qwen API
print("Testing Qwen API...")
response = requests.post(
    "http://localhost:42005/v1/chat/completions",
    headers={"Authorization": "Bearer sk-73a7a78c98f74625914a5a969b084089"},
    json={
        "model": "coder-model",
        "messages": [{"role": "user", "content": "What is 2+2?"}]
    }
)
print("Response:", response.json()["choices"][0]["message"]["content"])
