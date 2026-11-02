"""Consulta a codificação estimada para o conteúdo."""

import requests

resposta = requests.get("https://httpbin.org/get", timeout=10)
print(resposta.apparent_encoding)
