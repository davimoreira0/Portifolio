"""Envia campos de formulário no corpo da requisição."""

import requests

# data envia os campos como formulário.
dados = {"usuario": "davi", "senha": "exemplo"}
resposta = requests.post("https://httpbin.org/post", data=dados, timeout=10)
print(resposta.json())
