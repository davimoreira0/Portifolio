"""Lê links do cabeçalho Link, se houver."""

import requests

resposta = requests.get("https://httpbin.org/get", timeout=10)
print(resposta.links)
