"""Mantém cookies padrão na sessão."""

import requests

with requests.Session() as sessao:
    sessao.cookies.update({"usuario": "davi"})
    resposta = sessao.get("https://httpbin.org/cookies", timeout=10)
    print(resposta.json())
