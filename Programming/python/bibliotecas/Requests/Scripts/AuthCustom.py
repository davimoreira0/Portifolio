"""Acrescenta um cabeçalho com autenticação personalizada."""

import requests

class MinhaAutenticacao(requests.auth.AuthBase):
    def __call__(self, requisicao):
        requisicao.headers["X-Autenticacao"] = "exemplo"
        return requisicao

resposta = requests.get("https://httpbin.org/headers", auth=MinhaAutenticacao(), timeout=10)
print(resposta.json())
