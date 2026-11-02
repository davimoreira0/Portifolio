"""Cria sessão e reutiliza conexões entre requisições."""

import requests

# A sessão mantém estado e deve ser fechada ao terminar.
with requests.Session() as sessao:
    resposta = sessao.get("https://httpbin.org/get", timeout=10)
    print(resposta.status_code)
