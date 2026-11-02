"""Converte o corpo JSON em objeto Python."""

import requests

resposta = requests.get("https://httpbin.org/json", timeout=10)
dados = resposta.json()
print(dados)
print(type(dados))
