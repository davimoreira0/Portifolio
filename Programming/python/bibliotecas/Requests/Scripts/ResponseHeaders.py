"""Consulta os cabeçalhos recebidos."""

import requests

resposta = requests.get("https://httpbin.org/get", timeout=10)
print(resposta.headers)
print(resposta.headers.get("Content-Type"))
