"""Baixa um arquivo em blocos para poupar memória."""

import requests

with requests.get("https://httpbin.org/bytes/100000", stream=True, timeout=15) as resposta:
    resposta.raise_for_status()
    with open("arquivo.bin", "wb") as arquivo:
        for bloco in resposta.iter_content(chunk_size=8192):
            if bloco:
                arquivo.write(bloco)
print("Download concluído!")
