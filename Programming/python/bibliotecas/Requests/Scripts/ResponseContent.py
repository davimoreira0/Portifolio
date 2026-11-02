"""Lê o corpo da resposta como bytes."""

import requests

resposta = requests.get("https://httpbin.org/image/png", timeout=10)
print(resposta.content)
