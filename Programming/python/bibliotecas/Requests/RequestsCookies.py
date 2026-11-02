"""Envia cookies ao servidor."""

import requests

# cookies envia pares nome e valor.
cookies = {"usuario": "davi", "tema": "escuro"}
resposta = requests.get("https://httpbin.org/cookies", cookies=cookies, timeout=10)
print(resposta.json())
