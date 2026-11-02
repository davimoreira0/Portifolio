"""Aplica parâmetros padrão às requisições da sessão."""

import requests

with requests.Session() as sessao:
    sessao.params.update({"linguagem": "python", "versao": "3"})
    resposta = sessao.get("https://httpbin.org/get", timeout=10)
    print(resposta.url)
