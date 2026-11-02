"""Envia dados para criar ou substituir um recurso."""

import requests

# PUT envia uma representação do recurso.
dados = {"nome": "Carlos", "idade": 25}
resposta = requests.put("https://httpbin.org/put", json=dados, timeout=10)
print(resposta.status_code)
print(resposta.json())
