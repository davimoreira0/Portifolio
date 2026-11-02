"""Monta adaptador com tentativas de repetição."""

import requests

with requests.Session() as sessao:
    adaptador = requests.adapters.HTTPAdapter(max_retries=3)
    sessao.mount("https://", adaptador)
    resposta = sessao.get("https://httpbin.org/get", timeout=10)
    print(resposta.status_code)
