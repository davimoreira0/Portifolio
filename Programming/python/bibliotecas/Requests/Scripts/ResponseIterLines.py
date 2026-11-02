"""Percorre uma resposta transmitida linha por linha."""

import requests

with requests.get("https://httpbin.org/stream/5", stream=True, timeout=10) as resposta:
    for linha in resposta.iter_lines(decode_unicode=True):
        if linha:
            print(linha)
