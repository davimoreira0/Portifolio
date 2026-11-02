"""Constrói um objeto Request sem enviá-lo."""

import requests

requisicao = requests.Request("GET", "https://httpbin.org/get", params={"nome": "Davi"}, headers={"Accept": "application/json"})
print(requisicao)
