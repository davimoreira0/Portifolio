"""Obtém codificação a partir dos cabeçalhos."""

import requests

resposta = requests.get("https://httpbin.org/get", timeout=10)
codificacao = requests.utils.get_encoding_from_headers(resposta.headers)
print(codificacao)
