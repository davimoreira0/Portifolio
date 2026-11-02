"""Percorre o corpo em blocos de bytes."""

import requests

with requests.get("https://httpbin.org/bytes/1024", stream=True, timeout=10) as resposta:
    for bloco in resposta.iter_content(chunk_size=256):
        if bloco:
            print(len(bloco))
