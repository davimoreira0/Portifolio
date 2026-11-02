"""Usa request() para escolher o método HTTP."""

import requests

# request() permite informar o método como argumento.
resposta = requests.request("GET", "https://httpbin.org/get", timeout=10)
print(resposta.status_code)
print(resposta.text)
