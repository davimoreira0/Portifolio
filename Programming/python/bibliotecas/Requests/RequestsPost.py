"""Envia dados JSON com POST."""

import requests

# POST envia dados para o servidor.
dados = {"nome": "Davi", "idade": 16}
resposta = requests.post("https://httpbin.org/post", json=dados, timeout=10)
print(resposta.status_code)
print(resposta.json())
