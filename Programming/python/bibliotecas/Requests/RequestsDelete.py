"""Envia uma solicitação de exclusão."""

import requests

# DELETE solicita a remoção do recurso.
resposta = requests.delete("https://httpbin.org/delete", timeout=10)
print(resposta.status_code)
print(resposta.json())
