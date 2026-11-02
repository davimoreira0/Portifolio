"""Faz uma requisição GET e mostra status e texto."""

import requests

# GET consulta dados no servidor.
resposta = requests.get("https://httpbin.org/get", timeout=10)
print(resposta.status_code)
print(resposta.text)
