"""Adiciona parâmetros à URL."""

import requests

# params transforma o dicionário em query string.
parametros = {"nome": "Davi", "pagina": 2, "categoria": "python"}
resposta = requests.get("https://httpbin.org/get", params=parametros, timeout=10)
print(resposta.url)
print(resposta.json())
