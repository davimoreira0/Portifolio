"""Envia uma requisição OPTIONS usando uma sessão."""

import requests

with requests.Session() as sessao:
    resposta = sessao.options("https://httpbin.org/get", timeout=10)
    print(resposta.status_code)
    print(resposta.headers)
