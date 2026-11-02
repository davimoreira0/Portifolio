"""Configura adaptador, pool e tentativas da sessão."""

import requests

with requests.Session() as sessao:
    adaptador = requests.adapters.HTTPAdapter(pool_connections=10, pool_maxsize=20, max_retries=3, pool_block=True)
    sessao.mount("https://", adaptador)
    resposta = sessao.get("https://httpbin.org/get", timeout=10)
    print(resposta.status_code)
