"""Lê a resposta gradualmente, linha por linha."""

import requests

# stream=True evita carregar todo o corpo de uma vez.
with requests.get("https://httpbin.org/stream/5", stream=True, timeout=10) as resposta:
    for linha in resposta.iter_lines():
        if linha:
            print(linha.decode("utf-8"))
