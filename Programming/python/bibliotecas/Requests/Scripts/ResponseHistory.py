"""Mostra as respostas de redirecionamento anteriores."""

import requests

resposta = requests.get("https://httpbin.org/redirect/3", timeout=10)
print(resposta.history)
