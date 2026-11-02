"""Gera HTTPError quando o servidor retorna erro."""

import requests

resposta = requests.get("https://httpbin.org/status/404", timeout=10)
try:
    resposta.raise_for_status()
except requests.exceptions.HTTPError as erro:
    print("Erro:", erro)
