"""Baixa um arquivo e salva no diretório atual."""

import requests

resposta = requests.get("https://httpbin.org/image/png", timeout=15)
resposta.raise_for_status()
with open("imagem.png", "wb") as arquivo:
    arquivo.write(resposta.content)
print("Download concluído!")
