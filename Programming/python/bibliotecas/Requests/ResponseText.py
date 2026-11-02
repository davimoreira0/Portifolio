"""Lê o corpo da resposta como texto."""

import requests

resposta = requests.get("https://httpbin.org/get", timeout=10)
print(resposta.text)
