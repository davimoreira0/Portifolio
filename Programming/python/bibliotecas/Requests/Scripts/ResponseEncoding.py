"""Lê e define a codificação do texto."""

import requests

resposta = requests.get("https://httpbin.org/get", timeout=10)
print(resposta.encoding)
resposta.encoding = "utf-8"
print(resposta.text)
