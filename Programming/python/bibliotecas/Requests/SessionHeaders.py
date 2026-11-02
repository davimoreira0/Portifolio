"""Aplica cabeçalhos padrão a uma sessão."""

import requests

with requests.Session() as sessao:
    sessao.headers.update({"User-Agent": "Python", "Accept": "application/json"})
    resposta = sessao.get("https://httpbin.org/headers", timeout=10)
    print(resposta.json())
