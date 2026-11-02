"""Envia documento.txt como arquivo multipart."""

import requests

# Crie documento.txt antes de executar este exemplo.
with open("documento.txt", "rb") as arquivo:
    resposta = requests.post("https://httpbin.org/post", files={"arquivo": arquivo}, timeout=15)
print(resposta.status_code)
print(resposta.json())
