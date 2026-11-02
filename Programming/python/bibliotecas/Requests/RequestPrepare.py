"""Prepara uma requisição e exibe seus campos."""

import requests

requisicao = requests.Request("GET", "https://httpbin.org/get")
preparada = requisicao.prepare()
print(preparada.method)
print(preparada.url)
print(preparada.headers)
