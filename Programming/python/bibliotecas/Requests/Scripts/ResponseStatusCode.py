"""Lê o código HTTP da resposta."""

import requests

resposta = requests.get("https://httpbin.org/get", timeout=10)
print(resposta.status_code)  # Ex.: 200 indica sucesso.
