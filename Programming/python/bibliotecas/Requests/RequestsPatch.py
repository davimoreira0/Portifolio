"""Envia uma alteração parcial."""

import requests

# PATCH altera apenas os campos informados.
resposta = requests.patch("https://httpbin.org/patch", json={"idade": 30}, timeout=10)
print(resposta.json())
