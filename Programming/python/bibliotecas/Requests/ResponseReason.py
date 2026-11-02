"""Mostra a descrição associada ao status HTTP."""

import requests

resposta = requests.get("https://httpbin.org/get", timeout=10)
print(resposta.reason)
