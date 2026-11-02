"""Prepara e envia uma requisição com uma sessão."""

import requests

with requests.Session() as sessao:
    requisicao = requests.Request("GET", "https://httpbin.org/get")
    preparada = sessao.prepare_request(requisicao)
    resposta = sessao.send(preparada, timeout=10)
    print(resposta.status_code)
