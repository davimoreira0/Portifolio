"""Define autenticação básica na sessão."""

import requests

with requests.Session() as sessao:
    sessao.auth = ("usuario", "senha")
    resposta = sessao.get("https://httpbin.org/basic-auth/usuario/senha", timeout=10)
    print(resposta.status_code)
