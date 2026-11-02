"""Mostra a URL final da resposta."""

import requests

resposta = requests.get("https://httpbin.org/get", timeout=10)
print(resposta.url)
