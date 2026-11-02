"""Mostra o tempo até a chegada dos cabeçalhos."""

import requests

resposta = requests.get("https://httpbin.org/get", timeout=10)
print(resposta.elapsed)
print(resposta.elapsed.total_seconds())
