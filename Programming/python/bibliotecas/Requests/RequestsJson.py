"""Envia um objeto JSON."""

import requests

# requests serializa o dicionário como JSON.
dados = {"produto": "Computador", "preco": 3500, "estoque": True}
resposta = requests.post("https://httpbin.org/post", json=dados, timeout=10)
print(resposta.json())
