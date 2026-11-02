"""Configura um proxy HTTP local."""

import requests

# Requer um proxy ativo no endereço configurado.
proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}
resposta = requests.get("https://httpbin.org/get", proxies=proxies, timeout=10)
print(resposta.status_code)
